import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QCalendarWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout)
from PyQt5.QtCore import QDate, Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QPalette, QColor, QFont
from datetime import date

class AgeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Magical Age Calculator')
        self.setFixedSize(600, 600)  # Increased height for input section
        
        # Set background gradient
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                          stop:0 #7F7FD5, stop:0.5 #86A8E7, stop:1 #91EAE4);
            }
        """)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title label with animation
        self.title_label = QLabel("✨ Magical Age Calculator ✨")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont('Arial', 24, QFont.Bold))
        self.title_label.setStyleSheet("color: white; padding: 10px;")
        layout.addWidget(self.title_label)

        # Input section
        input_layout = QHBoxLayout()
        
        # Name input
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border-radius: 5px;
                background-color: white;
                font-size: 14px;
            }
        """)
        input_layout.addWidget(self.name_input)
        
        layout.addLayout(input_layout)
        
        # Calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMaximumDate(QDate.currentDate())
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: white;
                border-radius: 10px;
            }
            QCalendarWidget QToolButton {
                color: #333;
                border-radius: 5px;
                background-color: #fff;
                font-weight: bold;
                font-size: 14px;
            }
            QCalendarWidget QMenu {
                background-color: white;
                font-weight: bold;
            }
            QCalendarWidget QSpinBox {
                background-color: white;
                font-weight: bold;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.calendar)
        
        # Calculate button
        self.calc_button = QPushButton("Calculate My Age 🎈")
        self.calc_button.setFont(QFont('Arial', 12))
        self.calc_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.calc_button.clicked.connect(self.calculate_age)
        layout.addWidget(self.calc_button)
        
        # Result label
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont('Arial', 14))
        self.result_label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 0.2);
                padding: 20px;
                border-radius: 10px;
            }
        """)
        layout.addWidget(self.result_label)
        
        # Initialize animation
        self.animation = QPropertyAnimation(self.result_label, b"geometry")
        
    def calculate_age(self):
        # Get name from input
        name = self.name_input.text() or "You"
        
        # Get selected date from calendar
        birth_date = self.calendar.selectedDate()
        current_date = QDate.currentDate()
        
        # Convert QDate to Python date
        birth = date(birth_date.year(), birth_date.month(), birth_date.day())
        today = date.today()
        
        # Calculate age
        years = today.year - birth.year
        months = today.month - birth.month
        days = today.day - birth.day
        
        if days < 0:
            months -= 1
            days += 30  # Approximate days in a month
            
        if months < 0:
            years -= 1
            months += 12
            
        # Create result text with bold years and months
        result = f"Hello {name}! You are <b>{years} years</b>, <b>{months} months</b>, and {days} days old! 🎉"
        
        # Animate result display
        self.result_label.setText(result)
        self.animate_result()
        
    def animate_result(self):
        # Create bounce animation
        current_geometry = self.result_label.geometry()
        
        self.animation.setDuration(1000)
        self.animation.setStartValue(QRect(current_geometry.x(), 
                                         current_geometry.y() - 30,
                                         current_geometry.width(), 
                                         current_geometry.height()))
        self.animation.setEndValue(current_geometry)
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = AgeCalculator()
    calculator.show()
    sys.exit(app.exec_())
