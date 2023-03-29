# ChatGPT Python QT Client
ChatGPT Python QT Client via API and OPENAI

<img src="https://raw.githubusercontent.com/nicarley/ChatGPTPythonQTClient/main/chatgptclient.jpg" />

This python QT client uses the ChatGPT/OpenAI API.  You must get an API Key from User Settings at OPENAI's website:
https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key


Libraries Used:
sys, os, openai, 
PyQt5.QtGui: QIcon, QPixmap, QTextOption
PyQt5.QtWidgets: QApplication, QMainWindow, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QScrollArea, QPushButton

Useful Notes:
1.  Make sure you have installed the libraries imported at the top of the list of the Main Chat Window File. Python 3.8, 3.10, and 3.11 are the environments tested in.  Have not tested other environments. 
2.  You must have a text file that containts your API Key only (filepath indicated at the top of the MainChat.py).  The variable that you need to change is called filename
3.  Once you set the API Key in the Text field, you are ready to ask questions.  Results will be written to a text file declared in the top of the file.  Both are read into variables each time the program each time is loaded.  If you change the API key it will write it to the api file declared also when the send button is clicked..
4.  When loading the app, it verifies that the file listed is at the filepath specified.  If it is not, it creates it.  If it is, it simply reads in the API Key.
5.  In the app, it displays the API Key listed from the Text file.  If you change the text field to a new api key, when you send your request, it will save the new API key to the text file.  

