## Created by Nicolas Farley 11/08/2023
## Chat GPT Client using OPEN AI's API, Python, and PyQT6.

import sys
import os
import openai
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QTextOption
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QScrollArea, QPushButton


filename = 'c:/temp/helpdesk/resources/chatgptapikey.txt'
gptresults = 'c:/temp/helpdesk/resources/gptresults.txt'

# check if file exists
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        oapikey = f.read().strip()
else:
    # create a new file
    with open(filename, 'w') as f:
        f.write('')
    oapikey = ''

if os.path.isfile(gptresults):
    with open(gptresults, 'r') as f:
        gpttext = f.read().strip()
else:
    # create a new file
    with open(gptresults, 'w') as f:
        f.write('')
    gpttext = ''


class SearchAnswer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the API key box
        api_key_box = QHBoxLayout()
        api_key_label = QLabel("API Key:")
        self.api_key_textbox = QLineEdit()
        self.api_key_textbox.setText(oapikey)
        api_key_box.addWidget(api_key_label)
        api_key_box.addWidget(self.api_key_textbox)

        # Create the search bar
        self.search_bar = QTextEdit()
        search_label = QLabel("Ask: ")

        # Create the answer box
        self.answer_box = QTextEdit()
        self.answer_box.setText(gpttext)
        self.answer_box.setReadOnly(True)
        self.answer_box.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        answer_label = QLabel("Assistant:")
        self.clear_button = QPushButton("Clear Chat Logs")
        self.clear_button.clicked.connect(self.clear_answer_box)
        # Create the import all chat logs button
        self.import_button = QPushButton("Import All Chat Logs")
        self.import_button.clicked.connect(self.import_chat_logs)
        # Create the label
        verify_label = QLabel("Please Verify information is accurate before using!")
        verify_label.setStyleSheet("color: red")

        # Create the vertical layout for the search bar and answer box
        v_layout = QVBoxLayout()

        # Add the label to the vertical layout
        v_layout.addWidget(verify_label)

        # Add the API key box to the vertical layout
        v_layout.addLayout(api_key_box)

        # Create the horizontal layout for the search bar
        h_layout_search = QHBoxLayout()
        h_layout_search.addWidget(search_label)
        h_layout_search.addWidget(self.search_bar)
        v_layout.addLayout(h_layout_search)

        # Create the horizontal layout for the answer box
        h_layout_answer = QHBoxLayout()
        h_layout_answer.addWidget(answer_label)

        # Create the scroll area for the answer box
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.answer_box)
        scroll_area.setWidgetResizable(True)
        h_layout_answer.addWidget(scroll_area)

        # Create the send button
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.make_request)
        # Add the send button to the vertical layout
        v_layout.addWidget(self.send_button)

        # Add the answer box and send button to the vertical layout
        v_layout.addLayout(h_layout_answer)
        # Add the clear button to the vertical layout
        v_layout.addWidget(self.clear_button)
        # Add the import button to the vertical layout
        v_layout.addWidget(self.import_button)
        # Create the central widget and set its layout
        central_widget = QWidget()
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

        # Set the window title and size
        self.setWindowTitle("Virtual Assistant")
        self.resize(800, 600)

        # Create the ChatGPT icon
        icon = QIcon(QPixmap("c:/temp/Helpdesk/resources/openai.png"))
        self.setWindowIcon(icon)

        # Autoscroll the answer box to the bottom
        scroll_bar = self.answer_box.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())

    # Define the clear_answer_box method
    def clear_answer_box(self):
        self.answer_box.clear()
        # with open(gptresults, 'w') as f:
        #    f.seek(0)
        #    f.truncate()

    # Define the import_chat_logs method
    def import_chat_logs(self):
        with open(gptresults, 'r') as f:
            gpttext = f.read().strip()
        self.answer_box.setText(gpttext)

    def make_request(self):
        # Get the text from the API key text box
        oapikey = self.api_key_textbox.text()
        openai.api_key = f'{oapikey}'

        # Write the new API key to the file
        with open(filename, "r") as f:
            content = f.read()
        if content != oapikey:
            with open(filename, 'w') as file:
                file.write(oapikey)

        # Get the text from the search bar
        search_text = self.search_bar.toPlainText()

        message = (search_text)
        messages = [{"role": "user", "content": message}]
        response = openai.ChatCompletion.create(
            # model="gpt-3.5-turbo",
            model="gpt-4-turbo",
            messages=messages
        )

        reply = response["choices"][0]["message"]["content"]
        self.answer_box.append("\n" + "YOU: " + search_text + "\n" + "ANSWER: " + reply + "\n \n")
        with open(f'{gptresults}', 'a') as f:
            f.write("YOU: " + search_text + "\n" + "ANSWER: " + reply + "\n \n")

        # Clear the search bar
        self.search_bar.clear()

        # Autoscroll the answer box to the bottom
        scroll_bar = self.answer_box.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchAnswer()
    window.show()
    sys.exit(app.exec())
