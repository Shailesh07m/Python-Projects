import sys
from PyQt5.QtWidgets import QApplication, QMainWindow ,QCheckBox,QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)

        self.checkBox = QCheckBox("Are you sure?",self)
        self.label=QLabel(self)
        self.label.setGeometry(150,180,350,100)
        self.setStyleSheet("background-color: lightblue;")
        self.initUI()

    def initUI(self):
        self.checkBox.setGeometry(150,110,300,100 )
        self.checkBox.setStyleSheet("QCheckBox { "
                                    "font-size:20px;"
                                    "font-family:Verdana;}")
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            self.label.setText("You Agreed to the Conditions")
            self.label.setStyleSheet("QLabel {color: green; font-size:15px}")
        else:
            self.label.setText("You Did not Agree")
            self.label.setStyleSheet("QLabel {color: red; font-size:15px}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
