import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import random

app = QApplication(sys.argv)
w = QWidget()
w.resize(450, 250)
w.move(900, 400)
w.setWindowTitle('Memory Card')

enterb = QPushButton('Ответить')
que = QLabel('Какой национальности не существует?')
grp = QGroupBox('Варианты ответов')
layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QVBoxLayout()
rb1 = QRadioButton('Дартвейдеры')
rb2 = QRadioButton('Чулымцы')
rb3 = QRadioButton('Смурфы')
rb4 = QRadioButton('Алеуты')
results = QLabel('Правильный ответ')
results.hide()
right = '!'
all_ques_cur = 0
all_right_cur = 0

ques = [{'вопрос': 'чего?', 'ответы': ['того', 'не того', 'моего', 'четвёртый'], 'верный': 'не того'}, 
        {'вопрос': 'когда?', 'ответы': ['вчера', 'завтра', 'ээээээээ', 'сегодня'], 'верный': 'ээээээээ'},
        {'вопрос': 'кто?', 'ответы': ['я', 'ты', 'мы', 'он'], 'верный': 'он'}]
cur_que = 0

def show_result():
    grp.hide()
    enterb.setText('Следующий вопрос')
    que.setText('Результат теста')
    check_answer()
    results.show()

def show_question():
    rb1.setAutoExclusive(False)
    rb2.setAutoExclusive(False)
    rb3.setAutoExclusive(False)
    rb4.setAutoExclusive(False)
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    rb1.setAutoExclusive(True)
    rb2.setAutoExclusive(True)
    rb3.setAutoExclusive(True)
    rb4.setAutoExclusive(True)
    grp.show()
    results.hide()
    enterb.setText('Ответить')

def ask():
    global cur_que
    if cur_que < len(ques):
        rand_que = ques[cur_que]
        cur_que = cur_que + 1
    else:
        cur_que = 0
        rand_que = ques[cur_que]
        cur_que = cur_que + 1
    random.shuffle(rand_que['ответы'])
    que.setText(rand_que['вопрос'])
    rb1.setText(rand_que['ответы'][0])
    rb2.setText(rand_que['ответы'][1])
    rb3.setText(rand_que['ответы'][2])
    rb4.setText(rand_que['ответы'][3])
    global right
    right = rand_que['верный']
    #print(right)
    show_question()
    
def start_test():
    if enterb.text() == 'Ответить':
        show_result()
    else:
        ask()
        
def show_correct(arg_ri):
    results.setText(arg_ri)
    
def check_answer(): 
    global all_ques_cur
    global all_right_cur
    text_ans = ""
    if rb1.isChecked() == True:
        text_ans = rb1.text()
    elif rb2.isChecked() == True:
        text_ans = rb2.text()
    elif rb3.isChecked() == True:
        text_ans = rb3.text()
    else:
        text_ans = rb4.text()
    if text_ans == right:
        show_correct('Правильно')
        all_right_cur = all_right_cur + 1
    else:
        show_correct('Неверно')
    all_ques_cur = all_ques_cur + 1
    print('Вопросов:', all_ques_cur)
    print('Верных ответов:', all_right_cur)
    print('Рейтинг:', all_right_cur / all_ques_cur * 100, '%')
    print('----------------------')
    #print(right)

random.shuffle(ques)

enterb.clicked.connect(start_test)

layout1.addWidget(rb1, alignment = Qt.AlignLeft)
layout1.addWidget(rb2, alignment = Qt.AlignRight)
layout2.addWidget(rb3, alignment = Qt.AlignLeft)
layout2.addWidget(rb4, alignment = Qt.AlignRight)
layout3.addLayout(layout1)
layout3.addLayout(layout2)
grp.setLayout(layout3)
layout.addWidget(que, alignment = Qt.AlignCenter)
layout.addWidget(grp) 
layout.addWidget(results, alignment = Qt.AlignCenter)
layout.addWidget(enterb, alignment = Qt.AlignCenter)
w.setLayout(layout)
w.show()
que.show()

ask()
sys.exit(app.exec_())
