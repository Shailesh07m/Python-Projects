import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Click Game")
        self.setGeometry(200, 200, 600, 400)


        self.score = 0


        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(50, 50, 100, 50)


        self.label = QLabel("Score: 0", self)
        self.label.setGeometry(10, 10, 100, 30)


        self.setStyleSheet(
            "QPushButton {background-color: red; font-size:15px; color:white; border-radius: 25px;}"
        )


        self.button.clicked.connect(self.move_button)

    def move_button(self):
        # Increase score
        self.score += 1
        self.label.setText(f"Score: {self.score}")


        window_width = self.width()
        window_height = self.height()


        button_width = self.button.width()
        button_height = self.button.height()


        new_x = random.randint(0, window_width - button_width)
        new_y = random.randint(0, window_height - button_height)


        self.button.move(new_x, new_y)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
