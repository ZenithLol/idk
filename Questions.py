#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit
 
#declaring constants
win_width, win_height = 1500, 750
win_x, win_y = 225, 175
txt_title = "List of questions"

class MainWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        # creating and customizing the graphical elements:
        self.initUI()
        #connects the elements
        self.connects()
 
        #determines how the window will look (text, size, location)
        self.set_appear()
 
        # start:
        self.show()
 
    def initUI(self):
        #Makes graphical elements
        self.ButtonNew = QPushButton("New question", self)
        self.ButtomDel = QPushButton("Delete question", self)
        self.ButtonBeg = QPushButton("Begin practice", self)
        self.VerticalLine = QVBoxLayout()
        self.Horizontal = QHBoxLayout()

        self.VerticalLine.addLayout(self.Horizontal)
 
        self.Horizontal.addWidget(self.ButtonNew, alignment = Qt.AlignCenter)
        self.Horizontal.addWidget(self.ButtomDel, alignment = Qt.AlignCenter)
        self.VerticalLine.addWidget(self.ButtonBeg, alignment = Qt.AlignCenter)   
 
 
        layoutH = QHBoxLayout()
        #layoutH.addWidget(self.btn_1, alignment = Qt.AlignCenter)
 
        my_Widget = QWidget()
        my_Widget.setLayout(layoutH)
        # self.layout_line.addWidget(my_Widget)
 
        # self.lable_finish.setText("Calculator Mockup")       
        self.setLayout(self.VerticalLine)
 
 
    def connects(self):
        pass
 
    #Window appearance
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
 
def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
 
main()
