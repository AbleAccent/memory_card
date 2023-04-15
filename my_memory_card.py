from random import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



class Questions():
    def __init__(self, questiontext, rightanswer, wronganswer1, wronganswer2, wronganswer3, points):
        self.questiontext = questiontext
        self.rightanswer = rightanswer
        self.wronganswer1 = wronganswer1
        self.wronganswer2 = wronganswer2
        self.wronganswer3 = wronganswer3
        self.points = points



# def win():
# mess = QMessageBox()
# mess.setText('Вы ответили ВЕРНО!')
# mess.exec_()
# answergroupbox.hide()

# def lose():
# mess = QMessageBox()
# mess.setText('Вы ответели НЕВЕРНО!')
# mess.exec_()
# answergroupbox.hide()



def showresoult():
    answergroupbox.hide()
    resoultgroupbox.show()
    button.setText('Следующий вопрос!')


def showqestion():
    resoultgroupbox.hide()
    radiogroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    answergroupbox.show()
    button.setText('Ответить!')


def starttest():
    if button.text() == 'Ответить!':
        showresoult()
    else:
        showqestion()


def nextqestion():
    questionindx = randint(0, len(question_list)-1)
    main_win.total += 1
    q = question_list[questionindx]
    ask(q)


def checkanswer():
    if answers[0].isChecked():
        resoulttext.setText('Правильно!')
        showresoult()
        main_win.score += 1
    else:
        resoulttext.setText('Неправильно!')
        showresoult()
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Рейтинг:', main_win.score / main_win.total * 100, '%')
    print()


def click_ok():
    if button.text() == 'Ответить!':
        checkanswer()
    else:
        nextqestion()


def ask(q:Questions):
    #global answers
    shuffle(answers)
    answers[0].setText(q.rightanswer)
    answers[1].setText(q.wronganswer1)
    answers[2].setText(q.wronganswer2)
    answers[3].setText(q.wronganswer3)
    questiontext.setText(q.questiontext)
    rightanswertext.setText(q.rightanswer)
    showqestion()


# создание элементов интерфейса

app = QApplication([])
main_win = QWidget()
main_win.resize(QSize(400, 200))
main_win.setWindowTitle('Memory Card')
main_win.curquestion = -1



questiontext = QLabel('Вопрос?')
answer1 = QRadioButton('1')
answer2 = QRadioButton('2')
answer3 = QRadioButton('3')
answer4 = QRadioButton('4')
answers = [answer1, answer2, answer3, answer4]

button = QPushButton('Ответить!')
answergroupbox = QGroupBox('Варианты ответов:')
resoultgroupbox = QGroupBox('Результат теста:')
resoulttext = QLabel('Правильно/Неправильно')
rightanswertext = QLabel()

# v_line ветрикальная напровляющая для main_win
v_line = QVBoxLayout()
v_line2 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
# v_line1 ветрикальная напровляющая для answergroupbox
v_line1 = QVBoxLayout()

h_line1.addWidget(questiontext, alignment=Qt.AlignCenter)
h_line2.addWidget(answer1, alignment=Qt.AlignCenter)
h_line2.addWidget(answer2, alignment=Qt.AlignCenter)
h_line3.addWidget(answer3, alignment=Qt.AlignCenter)
h_line3.addWidget(answer4, alignment=Qt.AlignCenter)
v_line1.addLayout(h_line2)
v_line1.addLayout(h_line3)
answergroupbox.setLayout(v_line1)
v_line.addLayout(h_line1)
v_line.addWidget(answergroupbox)
main_win.setLayout(v_line)
v_line2.addWidget(resoulttext, alignment=Qt.AlignLeft)
v_line2.addWidget(rightanswertext, alignment=Qt.AlignCenter)
resoultgroupbox.setLayout(v_line2)
v_line.addWidget(resoultgroupbox)
v_line.addWidget(button, alignment=Qt.AlignCenter)

radiogroup = QButtonGroup()
radiogroup.addButton(answer1)
radiogroup.addButton(answer2)
radiogroup.addButton(answer3)
radiogroup.addButton(answer4)


# обработка событий
# answer3.clicked.connect(win)
# answer1.clicked.connect(lose)
# answer2.clicked.connect(lose)
# answer4.clicked.connect(lose)

# запуск приложения
resoultgroupbox.hide()

button.clicked.connect(click_ok)



question1 = Questions('Сколько дней в году(невисокосном)?', '365', '1000', '265', '356', 1)
question2 = Questions('Сколько минут в часе?', '60', '76', '59', '61', 1)
question3 = Questions('Сколько часов в сутках?', '24', '25', '12', '48', 1)
question4 = Questions('Какого цвета нет в радуге?', 'Розовый', 'Желтый', 'Зеленый', 'Фиолетовый', 1)
question5 = Questions('Самая большая страна по площади?', 'Россия', 'США', 'Италия', 'Франция', 1)
question6 = Questions('Какой океан самый большой на Земле?', 'Тихий', 'Атлантический', 'Южный', 'Индийский', 1)
question7 = Questions('Какая планета самая горячая?', 'Венера', 'Сатурн', 'Меркурий', 'Марс', 1)
question8 = Questions('Fe — это символ какого химического элемента?', 'Железо', 'Золото', 'Водород', 'Фтор', 1)
question9 = Questions('Сколько градусов в круге?', '360', '90', '45', '180', 1)
question10 = Questions('Какой формы знак STOP?', 'Шестиугольник', 'Восьмиугольник', 'Треугольник', 'Треугольник', 1)
question11 = Questions('Какой континент на Земле самый большой?', 'Евразия', 'Африка', 'Южная Америка', 'Антарктида', 1)
question12 = Questions('Какая страна граничит с 14 странами и пересекает 8 часовых поясов?', 'Россия', 'Китай', 'Испания', 'Индия', 1)
question13 = Questions('Какая валюта Дании?', 'Крона', 'Доллар', 'Юань', 'Евро', 1)

question_list = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13]
shuffle(question_list)

main_win.total = 0
main_win.score = 0

nextqestion()
main_win.show()
app.exec_()

