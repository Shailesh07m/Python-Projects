import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow,QLabel,QLineEdit,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Line Widget")
        self.setGeometry(700, 300, 500, 500)
        self.lineEdit = QLineEdit(self)
        self.button = QPushButton("Submit",self)
        self.label=QLabel(self)



        self.initUI()

    def initUI(self):
        self.lineEdit.setPlaceholderText("     Enter your name")
        self.lineEdit.setGeometry(150,50,250,50)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "font-size:22px;"
                                    "border-radius:10px;"
                                    "border:1px solid;"
                                    "font-family:Georgia;}")
        self.button.setGeometry(180,120,150,50)
        self.button.setStyleSheet("QPushButton {\n"
                                  "border-radius:25px;"
                                  "background-color:#2bfb77;"
                                  "margin-left:25px;}")
        self.button.clicked.connect(self.submit)
    def submit(self):
        text = self.lineEdit.text()
        self.label.setText(f"Hello {text}!")
        self.label.setStyleSheet("QLabel {\n"
                                 "color:green;"
                                 "font-size:40px;"
                                 "font-family:Georgia;}")
        self.label.setGeometry(150,200,200,100)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
