import sys
import os
import openai
from PyQt5.QtGui import QIcon, QPixmap, QTextOption
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QScrollArea, QPushButton

filename = 'path/to/file/chatgptapikey.txt'

# check if file exists
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        oapikey = f.read().strip()
else:
    # create a new file
    with open(filename, 'w') as f:
        f.write('')
    oapikey = ''

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
        self.search_bar = QLineEdit()
        search_label = QLabel("Ask:")

        # Create the answer box
        self.answer_box = QTextEdit()
        self.answer_box.setReadOnly(True)
        self.answer_box.setWordWrapMode(QTextOption.WordWrap)
        answer_label = QLabel("Assistant Answer:")

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

        # Create the central widget and set its layout
        central_widget = QWidget()
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

        # Set the window title and size
        self.setWindowTitle("Chat GPT Client")
        self.resize(640, 480)

        # Create the ChatGPT icon
        icon = QIcon(QPixmap("path/to/logofile.png"))
        self.setWindowIcon(icon)

        # Connect the search bar returnPressed signal to the send button clicked signal
        self.search_bar.returnPressed.connect(self.send_button.click)

    def make_request(self):
        # Get the text from the API key text box
        oapikey = self.api_key_textbox.text()

        # Write the new API key to the file
        with open(filename, 'w') as f:
            f.write(oapikey)

        # Get the text from the search bar
        search_text = self.search_bar.text()

        # Get the text from the API key text box
        oapikey = self.api_key_textbox.text()

        # Make the API request
        # Can changes the parameters below to change your chat responses
        openai.api_key = oapikey
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="User: " + search_text,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text

        # Check if the request was successful
        if "```" in response:
            self.answer_box.setHtml("<pre>" + response + "</pre>")
        else:
            # Clear the search bar
            self.search_bar.clear()

            # Set the response text in the answer box
            cursor = self.answer_box.textCursor()
            self.answer_box.setText(response)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchAnswer()
    window.show()
    sys.exit(app.exec_())
