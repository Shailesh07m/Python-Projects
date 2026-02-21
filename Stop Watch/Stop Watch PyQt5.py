import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame
)
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QIcon


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)

        self.init_ui()
        self.connect_signals()


    def init_ui(self):
        self.setWindowTitle("Stopwatch")
        self.setMinimumSize(520, 300)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(30)

        # ---- Card Container ----
        self.card = QFrame()
        self.card.setObjectName("card")
        card_layout = QVBoxLayout()
        card_layout.setSpacing(25)
        card_layout.setContentsMargins(30, 30, 30, 30)

        # ---- Time Label ----
        self.time_label = QLabel("00:00:00.000")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setObjectName("timeLabel")

        # ---- Buttons ----
        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.reset_btn = QPushButton("Reset")

        self.start_btn.setObjectName("startBtn")
        self.stop_btn.setObjectName("stopBtn")
        self.reset_btn.setObjectName("resetBtn")

        self.stop_btn.setEnabled(False)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)
        button_layout.addWidget(self.reset_btn)

        # Assemble card
        card_layout.addWidget(self.time_label)
        card_layout.addLayout(button_layout)
        self.card.setLayout(card_layout)

        main_layout.addWidget(self.card)
        self.setLayout(main_layout)

        self.apply_styles()

    # ---------------- Styling ----------------
    def apply_styles(self):
        self.setStyleSheet("""
        QWidget {
            background-color: #EEF3F9;
            font-family: Segoe UI;
        }

        QFrame#card {
            background-color: #FFFFFF;
            border-radius: 20px;
        }

        QLabel#timeLabel {
            font-size: 48px;
            color: #2D3436;
            font-weight: 700;
            padding: 15px;
        }

        QPushButton {
            border: none;
            border-radius: 12px;
            padding: 10px;
            font-size: 15px;
            min-height: 40px;
            color: White;
            font-weight: 1000;
        }

        /* START - Green */
        QPushButton#startBtn {
            background-color:hsl(110, 100%, 62%);
        }
        QPushButton#startBtn:hover {
            background-color: #ECFBF3;
        }
        QPushButton#startBtn:pressed {
            background-color: #BFEAD5;
        }

        /* STOP - Red */
        QPushButton#stopBtn {
            background-color: hsl(3, 100%, 62%);
            color: White;
        }
        QPushButton#stopBtn:hover {
            background-color: #FDECEC;
        }
        QPushButton#stopBtn:pressed {
            background-color: #F3C2C2;
        }

        /* RESET - Blue */
        QPushButton#resetBtn {
            background-color:hsl(235, 100%, 62%) ;
        }
        QPushButton#resetBtn:hover {
            background-color: #EDF4FD;
        }
        QPushButton#resetBtn:pressed {
            background-color: #C5D9F5;
        }

        QPushButton:disabled {
            background-color: #E0E0E0;
            color: #9E9E9E;
        }
        """)

    def connect_signals(self):
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        if not self.timer.isActive():
            self.timer.start(10)
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)

    def stop(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00.000")
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        return f"{time.hour():02}:{time.minute():02}:{time.second():02}.{time.msec():03}"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StopWatch()
    window.show()
    sys.exit(app.exec_())