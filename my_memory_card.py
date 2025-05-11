#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup,QApplication,QRadioButton, QWidget, QPushButton, QGroupBox,QLabel,QHBoxLayout, QMessageBox, QVBoxLayout
from random import shuffle ,randint

app = QApplication([])
window = QWidget()
window.setWindowTitle('Конкурс от Crazy People')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


class Question():
    def __init__(self, questions, right_answer, wrong1, wrong2, wrong3):
        self.questions = questions
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.questions)
    right_question.setText(q.right_answer)
    show_questions()


def show_correct(res):
    right_or_not.setText(res)
    show_result()
window.score = 0
window.total = 0

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score +=1
        print('Статистика\nвсего вопросов:', window.total, '\n Правильных ответов', window.score)
        print('Рейтинг', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')


def next_questions():
    window.total +=1
    print('Статистика всего вопросов:', window.total, '\n Правильных ответов', window.score)
    curquestion = randint(0, len(questions_list)-1)
    #window.cur_question = window.cur_question +1
    '''if window.cur_question >=len(questions_list):
        window.cur_question = 0'''
    q = questions_list[curquestion]
    ask(q)

def click_ok():
    if button.text()=='Ответить':
        check_answer()
    else:
        next_questions()
questions_list = []
q1 = Question('2+2=?', '4', '2', '3', '1')
q2 = Question('2+1=?', '3', '2', '1', '4')
q3 = Question('2-1=?', '1', '2', '3', '4')
q4 = Question('2+0=?', '2', '1', '3', '4')
q5 = Question('Кагого цвета нет в русском флаге?','Желтого', 'Синего', 'Красного', 'белого' )
q6 = Question('Кагого цвета нет в американском флаге?','Желтого', 'Синего', 'Красного', 'белого' )
q7 = Question('Кагого цвета нет в украинском флаге?','Черного', 'Синего', 'Красного', 'белого' )
q8 = Question('Кагого цвета нет в английском флаге?','Черного', 'Синего', 'Красного', 'белого' )
q9 = Question('Кагого цвета нет в беллоруском флаге?','Феолетового', 'Синего', 'Красного', 'белого' )


window.cur_question = -1
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)

RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox('Варианты ответов')
ans_layout = QVBoxLayout()
right_or_not = QLabel('Правильно/Не правильно')
right_question = QLabel('Правильный ответ')
ans_layout.addWidget(right_or_not)
ans_layout.addWidget(right_question)
AnsGroupBox.setLayout(ans_layout)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

main_layout = QVBoxLayout()
layout_window1 = QHBoxLayout()
layout_window2 = QHBoxLayout()
layout_window3 = QHBoxLayout()

question = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
layout_window1.addWidget(question)
layout_window2.addWidget(RadioGroupBox)
layout_window2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_window3.addWidget(button)
main_layout.addLayout(layout_window1)
main_layout.addLayout(layout_window2)
main_layout.addLayout(layout_window3)
window.resize(400, 250)
window.setLayout(main_layout)

def show_questions():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    #сбросить все преключатели

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def test():
    if 'Ответить'==button.text():
        show_result()
    else:
        show_questions()

q = Question('Как тебя зовут', 'Кирилл', 'Даниил', 'Диана', 'Влад')
ask(q)
button.clicked.connect(click_ok)
next_questions()
window.show()
app.exec_()
