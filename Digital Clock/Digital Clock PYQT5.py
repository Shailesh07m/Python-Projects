import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer ,QTime ,Qt
from PyQt5.QtGui import QFont,QFontDatabase


class DigitClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timeLAbel= QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        # Set window title
        self.setWindowTitle("Digital Clock")

        # Set initial window position (x, y) and size (width, height)
        self.setGeometry(600, 400, 500, 150)

        # Make window background fully transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Remove default window frame and keep clock always on top
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # Create vertical layout for organizing widgets
        vbox = QVBoxLayout()

        # Add spacing around edges (left, top, right, bottom)
        vbox.setContentsMargins(20, 20, 20, 20)

        # Add time label to layout
        vbox.addWidget(self.timeLAbel)

        # Apply layout to main widget
        self.setLayout(vbox)

        # Center align the text inside label
        self.timeLAbel.setAlignment(Qt.AlignCenter)

        # Apply glass UI styling using Qt stylesheet
        self.timeLAbel.setStyleSheet("""
            QLabel {

                /* Semi-transparent black background for glass effect */
                background-color: rgba(0, 0, 0, 120);

                /* Soft ice blue color for calm modern vibe */
                color: #A8EFFF;

                /* Large readable font size */
                font-size: 80px;

                /* Make digits bold */
                font-weight: bold;

                /* Smooth rounded corners */
                border-radius: 20px;

                /* Inner spacing so text doesn't touch edges */
                padding: 20px;
            }
        """)

        # Load custom digital font file
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")

        # Get font family name from loaded font
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        # Create font object (size 80 for balance)
        my_font = QFont(font_family, 80)

        # Apply font to label
        self.timeLAbel.setFont(my_font)

        # Connect timer signal to update function
        self.timer.timeout.connect(self.Update_Time)

        # Update every 1000 milliseconds (1 second)
        self.timer.start(1000)

        # Immediately update time once at startup
        self.Update_Time()
    def Update_Time(self):
        currentTime = QTime.currentTime().toString("hh:mm:ss AP")
        self.timeLAbel.setText(currentTime)


if __name__=="__main__":
    app = QApplication(sys.argv)
    clock = DigitClock()
    clock.show()
    sys.exit(app.exec_())