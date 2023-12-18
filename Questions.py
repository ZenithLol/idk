#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QMessageBox
import json
import random

#declaring constants
win_width, win_height = 800, 500
win_x, win_y = 200, 200
txt_title = "Test practice"

class MainWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.Question_Dictionary = dict()
        #creating and customizing the graphical elements:
        self.initUI()
        #connects the elements
        self.connects()

        #determines how the window will look (text, size, location)
        self.set_appear()

        #start:
        self.show()

    def initUI(self):
        #creates graphical elements
        self.QuestionList = QListWidget()
        self.lable_intrebare = QLabel("Question")
        self.lable_raspunsC = QLabel('Correct answer')
        self.lable_raspunsG1 = QLabel('Wrong answer one')
        self.lable_raspunsG2 = QLabel('Wrong answer two')
        self.lable_raspunsG3 = QLabel('Wrong answer three')

        self.line_intrebare = QLineEdit()
        self.line_intrebareC = QLineEdit()
        self.line_intrebareG1 = QLineEdit()
        self.line_intrebareG2 = QLineEdit()
        self.line_intrebareG3 = QLineEdit()

        self.NewQuestion = QPushButton("New Question", self)
        self.DelQuestion = QPushButton("Delete Question", self)
        self.BeginButton = QPushButton("Begin practice", self)
        self.layout_main = QVBoxLayout()

        layoutHB = QHBoxLayout()
        layoutHB.addWidget(self.DelQuestion, alignment = Qt.AlignCenter) 
        layoutHB.addWidget(self.BeginButton, alignment = Qt.AlignCenter)  
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()
        my_elements = [self.lable_intrebare, self.lable_raspunsC, self.lable_raspunsG1, self.lable_raspunsG2, self.lable_raspunsG3]
        for elemet in my_elements:
            layoutV1.addWidget(elemet, alignment = Qt.AlignCenter)

        layoutV2.addWidget(self.line_intrebare, alignment = Qt.AlignCenter)
        layoutV2.addWidget(self.line_intrebareC, alignment = Qt.AlignCenter)
        layoutV2.addWidget(self.line_intrebareG1, alignment = Qt.AlignCenter)
        layoutV2.addWidget(self.line_intrebareG2, alignment = Qt.AlignCenter)
        layoutV2.addWidget(self.line_intrebareG3, alignment = Qt.AlignCenter)
        layoutHB2 = QHBoxLayout()
        layoutHB2.addLayout(layoutV1)
        layoutHB2.addLayout(layoutV2)

        layoutHBB = QHBoxLayout() 
        layoutHBB.addWidget(self.QuestionList)     
        layoutHBB.addLayout(layoutHB2)

        self.layout_main.addLayout(layoutHBB)
        self.layout_main.addLayout(layoutHB)
        self.layout_main.addWidget(self.NewQuestion, alignment = Qt.AlignCenter)

        self.setLayout(self.layout_main)

    def Save(self):
        JsonObject = json.dump(self.Question_Dictionary)
        with open("test.json", "w") as outfile:
            outfile.write(JsonObject)

    #Adds a new question
    def AddNewQuestion(self):
        Question = self.line_intrebare.text()
        Answer = self.line_intrebareC.text()
        Answerg1 = self.line_intrebareG1.text()
        Answerg2 = self.line_intrebareG2.text() 
        Answerg3 = self.line_intrebareG3.text() 

        if Question == "":
            Error = QMessageBox()
            Error.setWindowTitle("Error")
            Error.setText("The question is empty!")
            Error.setIcon(QMessageBox.Warning)
            Error.exec_()
            print("You forgot to add a question")
        else:
            if Answer == "" or Answerg1 == "" or Answerg2 == "" or Answerg3 == "":
                Error = QMessageBox()
                Error.setWindowTitle("Error")
                Error.setText("One of the answers is empty")
                Error.setIcon(QMessageBox.Warning)
                Error.exec_()
                print("You forgot to add an answer")
            else:
                print("Question -", Question)
                self.Question_Dictionary[Question] = {"Answer" : Answer,
                                            "WrongAnswer1" : Answerg1,
                                            "WrongAnswer2" : Answerg2,
                                            "WrongAnswer3" : Answerg3}
                print(self.Question_Dictionary)
                Success = QMessageBox()
                Success.setWindowTitle("Success")
                Success.setText("Question created succesfully")
                Success.setIcon(QMessageBox.Information)
                Success.exec_()

    def set_questions(self,questions):
        self.Question_Dictionary = questions
        self.questions_list = list(self.Question_Dictionary.keys())
        self.changeQuestion()
 
 
    def changeQuestion(self):
        self.currenct_question = random.choice(self.questions_list) #alegere random
        # question = self.questions_list[0] # aceeasi ordine tot timpul

        self.questions_list.remove(self.currenct_question)

        self.lable_intrebare.setText(self.currenct_question) #alegere random
        answer_dict = self.Question_Dictionary[self.currenct_question]
        self.Answer.setText(answer_dict['answer'])
        self.Answerg1.setText(answer_dict['answer_g1'])
        self.Answerg2.setText(answer_dict['answer_g2'])
        self.Answerg3.setText(answer_dict['answer_g3'])


    def check_answer(self, bt):
        answer_dict = self.Question_Dictionary[self.currenct_question]
        if bt.text == self.Question_Dictionary[answer_dict['answer']]:
            # popup window cu raspuns correct
            pass
        else:
            # popup window cu raspuns correct
            pass
        self.questions_list.remove(self.currenct_question)
        self.changeQuestion()
 
    def bt_1(self):
        self.check_answer(self.r1)
    def bt_2(self):
        self.check_answer(self.r2)
    def bt_3(self):
        self.check_answer(self.r3)
    def bt_4(self):
        self.check_answer(self.r4)
 
 
    def connects(self):
        self.r1.clicked.connect(self.bt_1)
        self.r2.clicked.connect(self.bt_2)
        self.r3.clicked.connect(self.bt_3)
        self.r4.clicked.connect(self.bt_4)
        self.NewQuestion.clicked.connect(self.AddNewQuestion)

    #Determines how the window will look (text, size, location)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()

main()
