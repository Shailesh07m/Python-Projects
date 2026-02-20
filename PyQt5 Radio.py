import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Payment Method")

        self.setStyleSheet("background-color: lightgreen;")

        self.label = QLabel("Choose Payment Method:", self)
        self.label.setGeometry(25, 20, 250, 30)

        self.result_label = QLabel("", self)
        self.result_label.setGeometry(25, 220, 300, 30)

        self.initUI()

    def initUI(self):
        # Create Radio Buttons
        self.radio1 = QRadioButton("UPI", self)
        self.radio2 = QRadioButton("Visa", self)
        self.radio3 = QRadioButton("MasterCard", self)
        self.radio4 = QRadioButton("Net Banking", self)
        self.radio5 = QRadioButton("Wallet", self)

        # Set Positions
        self.radio1.setGeometry(25, 60, 150, 30)
        self.radio2.setGeometry(25, 90, 150, 30)
        self.radio3.setGeometry(25, 120, 150, 30)
        self.radio4.setGeometry(25, 150, 150, 30)
        self.radio5.setGeometry(25, 180, 150, 30)

        # Single Button Group (Only one selection allowed)
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio1)
        self.button_group.addButton(self.radio2)
        self.button_group.addButton(self.radio3)
        self.button_group.addButton(self.radio4)
        self.button_group.addButton(self.radio5)

        # Connect toggled signal
        self.radio1.toggled.connect(self.radio_changed)
        self.radio2.toggled.connect(self.radio_changed)
        self.radio3.toggled.connect(self.radio_changed)
        self.radio4.toggled.connect(self.radio_changed)
        self.radio5.toggled.connect(self.radio_changed)

    def radio_changed(self):
        radio = self.sender()
        if radio.isChecked():
            self.result_label.setText(f"Selected Payment Method: {radio.text()}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()