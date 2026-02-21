import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.initUI()


    def initUI(self):
        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)
        hbox=QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        centralwidget.setLayout(hbox)

        self.button1.setObjectName("Button1")
        self.button2.setObjectName("Button2")
        self.button3.setObjectName("Button3")

        self.setStyleSheet("""
        QPushButton {
        font-size:30px;
        font-family: Arial;
        padding: 15px 60px;
        margin: 25px;
        border: 2px solid black;
        border-radius: 18px;
        }
        QPushButton#Button1 {
        background-color: red;
        
        }
        
        QPushButton#Button2 {
        background-color: green;
        }
        
        QPushButton#Button3 {
        background-color: blue;
        }
        
        QPushButton#Button1:hover {
        background-color: peachpuff;
        
        }
        
        QPushButton#Button2:hover {
        background-color: lightgreen;
        }
        
        QPushButton#Button3:hover {
        background-color: lightblue;
        }
        
        
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
