import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QLineEdit
)
from PyQt5.QtCore import Qt
from requests.exceptions import HTTPError


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.city_label = QLabel("Enter City Name")
        self.city_input = QLineEdit()
        self.get_weather_btn = QPushButton("Search")

        self.temperature_label = QLabel("")
        self.emoji_label = QLabel("")
        self.description_label = QLabel("")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setFixedSize(500, 600)

        layout = QVBoxLayout()
        layout.setSpacing(20)

        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_btn)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description_label)

        self.setLayout(layout)

        # Alignment
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Object Names for Styling
        self.city_label.setObjectName("title")
        self.city_input.setObjectName("input")
        self.get_weather_btn.setObjectName("button")
        self.temperature_label.setObjectName("temp")
        self.emoji_label.setObjectName("emoji")
        self.description_label.setObjectName("desc")

        # Modern Professional Dark UI
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: white;
                font-family: Segoe UI;
            }

            QLabel#title {
                font-size: 28px;
                font-weight: bold;
            }

            QLineEdit#input {
                font-size: 22px;
                padding: 10px;
                border-radius: 10px;
                background-color: #2c2c3e;
                border: 2px solid #3e3e55;
            }

            QLineEdit#input:focus {
                border: 2px solid #4e9af1;
            }

            QPushButton#button {
                font-size: 22px;
                font-weight: bold;
                padding: 12px;
                border-radius: 12px;
                background-color: #4e9af1;
            }

            QPushButton#button:hover {
                background-color: #6eaaf5;
            }

            QLabel#temp {
                font-size: 60px;
                font-weight: bold;
            }

            QLabel#emoji {
                font-size: 90px;
            }

            QLabel#desc {
                font-size: 28px;
                font-style: italic;
            }
        """)

        # Connections
        self.get_weather_btn.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    def get_weather(self):
        api_key = "ccfccd13bd650b56e28cfbd0cc36dcca"  
        city = self.city_input.text().strip()

        if not city:
            self.display_error("Please enter a city name")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except HTTPError:
            if response.status_code == 404:
                self.display_error("City not found")
            elif response.status_code == 401:
                self.display_error("Invalid API key")
            else:
                self.display_error("HTTP Error occurred")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error")

        except requests.exceptions.Timeout:
            self.display_error("Request Timed Out")

        except requests.exceptions.RequestException:
            self.display_error("Unexpected Error")

    def display_weather(self, data):
        temp_k = data['main']['temp']
        temp_c = temp_k - 273.15

        description = data['weather'][0]['description']
        weather_id = data['weather'][0]['id']

        self.temperature_label.setText(f"{temp_c:.0f}°C")
        self.description_label.setText(description.title())
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def get_weather_emoji(self, weather_id):
        if 200 <= weather_id < 300:
            return "⛈"
        elif 300 <= weather_id < 600:
            return "🌧"
        elif 600 <= weather_id < 700:
            return "❄"
        elif 700 <= weather_id < 800:
            return "🌫"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return "🌍"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
