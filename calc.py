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
        self.multiply_button = QPushButton("Multiply")
        self.division_button = QPushButton("Divide")
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
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.division_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result)

        # Set layout
        self.setLayout(layout)

        # Connect button to function
        self.add_button.clicked.connect(self.add_numbers)
        self.sub_button.clicked.connect(self.sub_numbers)
        self.multiply_button.clicked.connect(self.multiply_numbers)
        self.division_button.clicked.connect(self.divide_numbers)
    def add_numbers(self):
        num1 = self.line_edit1.text()
        num2 = self.line_edit2.text()
        if num1.isdigit() and num2.isdigit():
            num1 = float(num1)
            num2 = float(num2)
            result = num1 + num2
            self.result.setText(str(result))
        else:
            self.result.setText("ONLY DIGITS ALLOWED")

    def sub_numbers(self):
        num1 = self.line_edit1.text()
        num2 = self.line_edit2.text()
        if num1.isdigit() and num2.isdigit():
            num1 = float(num1)
            num2 = float(num2)
            result = num1 - num2
            self.result.setText(str(result))
        else:
            self.result.setText("ONLY DIGITS ALLOWED")

    def multiply_numbers(self):
        num1 = self.line_edit1.text()
        num2 = self.line_edit2.text()
        if num1.isdigit() and num2.isdigit():
            num1 = float(num1)
            num2 = float(num2)
            result = num1 * num2
            self.result.setText(str(result))
        else:
            self.result.setText("ONLY DIGITS ALLOWED")

    def divide_numbers(self):
        num1 = self.line_edit1.text()
        num2 = self.line_edit2.text()
        if num1.isdigit() and num2.isdigit():
            num1 = float(num1)
            num2 = float(num2)
            if num2 != 0:
                result = num1 / num2
                self.result.setText(str(result))
            else:
                self.result.setText("ERROR, DIVIDING BY ZERO?")
        else:
            self.result.setText("ONLY DIGITS ALLOWED")




if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
