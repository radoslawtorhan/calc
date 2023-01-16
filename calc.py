from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(300, 150)

        # Create widgets
        self.label1 = QLabel("Number 1:")
        self.line_edit1 = QLineEdit()
        self.label2 = QLabel("Number 2:")
        self.line_edit2 = QLineEdit()
        self.add_button = QPushButton("Add")
        self.sub_button = QPushButton("Sub")
        self.result_label = QLabel("Result:")
        self.result = QLabel("0")

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.line_edit1)
        layout.addWidget(self.label2)
        layout.addWidget(self.line_edit2)
        layout.addWidget(self.add_button)
        layout.addWidget(self.sub_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result)

        # Set layout
        self.setLayout(layout)

        # Connect button to function
        self.add_button.clicked.connect(self.add_numbers)
        self.sub_button.clicked.connect(self.sub_numbers)

    def add_numbers(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        result = num1 + num2
        self.result.setText(str(result))

    def sub_numbers(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        result = num1 - num2
        self.result.setText(str(result))

if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
