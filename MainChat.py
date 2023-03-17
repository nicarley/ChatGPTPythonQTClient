## Created by Nicolas Farley 03/15/2023
## Chat GPT Client using OPEN AI's API, Python, and PyQT5.

import sys
import os
import openai
from PyQt5.QtGui import QIcon, QPixmap, QTextOption
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QScrollArea, QPushButton

#  Change these files to whatever you choose.  filename is for API key, and results save a log of the questions, and answers.
filename = './chatgptapikey.txt'
gptresults = './gptresults.txt'

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
        search_label = QLabel("Ask:")

        # Create the answer box
        self.answer_box = QTextEdit()
        self.answer_box.setText(gpttext)
        self.answer_box.setReadOnly(True)
        self.answer_box.setWordWrapMode(QTextOption.WordWrap)
        #  answer_label = QLabel("Assistant Answer:")

        # Create the vertical layout for the search bar and answer box
        v_layout = QVBoxLayout()

        # Add the API key box to the vertical layout
        v_layout.addLayout(api_key_box)

        # Create the horizontal layout for the search bar
        h_layout_search = QHBoxLayout()
        h_layout_search.addWidget(search_label)
        h_layout_search.addWidget(self.search_bar)
        v_layout.addLayout(h_layout_search)

        # Create the horizontal layout for the answer box
        h_layout_answer = QHBoxLayout()
        # h_layout_answer.addWidget(answer_label)

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

        # Create the central widget and set its layout
        central_widget = QWidget()
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

        # Set the window title and size
        self.setWindowTitle("Chat GPT Client")
        self.resize(640, 480)

        # Create the ChatGPT icon
        icon = QIcon(QPixmap("c:/temp/Helpdesk/resources/openai.png"))
        self.setWindowIcon(icon)

        # Connect the search bar returnPressed signal to the send button clicked signal only if you change the search_box to be a QLineEdit Must also  change toplaintext
        # self.search_bar.returnPressed.connect(self.send_button.click)
        # self.search_bar.textChanged.connect(self.send_button.click)

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

        messages = []
        message = (search_text)
        messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = response["choices"][0]["message"]["content"]


        self.answer_box.append("You: " + search_text + "\n" + "Response: " + reply + "\n \n") 
        with open(f'{gptresults}', 'a') as f:
            f.write("You: " + search_text + "\n" + "Response: " + reply + "\n \n")

        # Clear the search bar
        self.search_bar.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchAnswer()
    window.show()
    sys.exit(app.exec_())
