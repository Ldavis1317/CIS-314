import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,QVBoxLayout,QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__() # Intialize widget class
        self.setWindowTitle("My first GUI") # Set title of gui window
        self.resize(250, 100) # size of window

        layout = QVBoxLayout() # Creates a vertical layout
        self.setLayout(layout) # Assign the layout to the window

        self.input = QLineEdit() # Creates input field
        self.input.setPlaceholderText("Enter your text here...")
        layout.addWidget(self.input) # add the input to the layout

        submit_button = QPushButton("Submit") # Create submit button
        submit_button.clicked.connect(self.submit_text) # Connect the button to submit text
        layout.addWidget(submit_button)

        # Creates label to display text
        self.display_label = QLabel("") # Intialize the label with an empty string
        layout.addWidget(self.display_label)# Update the label to display submitted text

    def submit_text(self):
        text = self.input.text() # Retrieve submitted text
        self.display_label.setText(f"Submitted Text: {text}") # Update the label

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())