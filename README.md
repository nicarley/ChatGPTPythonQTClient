# ChatGPT Python QT Client
ChatGPT Python QT Client via API and OPENAPI

<img src="https://raw.githubusercontent.com/nicarley/ChatGPTPythonQTClient/main/chatgptclient.jpg" />

This python client uses the ChatGPT/OpenAI API.  You must get an API Key from User Settings at OPENAI's website:
https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key


Libraries Used:
sys, os, openai, 
PyQt5.QtGui: QIcon, QPixmap, QTextOption
PyQt5.QtWidgets: QApplication, QMainWindow, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QScrollArea, QPushButton

Useful Notes:
1.  Make sure you have installed the libraries imported at the top of the list of the Main Chat Window File.  
2.  You must have a text file that containts your API Key only (filepath indicated at the top of the MainChat.py).  The variable that you need to change is called filename
3.  Once you set the API Key in the Text file, simple run python MainChat.py from your enviroment.
4.  When loading the app, it verifies that the file listed is at the filepath specified.  If it is not, it creates it.  If it is, it simply reads in the API Key.
5.  In the app, it displays the API Key listed from the Text file.  If you change the text field to a new api key, when you send your request, it will save the new API key to the text file.  
6.  You can change the properties available in the API Key.  They are set as:          
7.  
8.  # Make the API request
        #Don't change the next 1 line only modify below the response:
        openai.api_key = oapikey
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="User: " + search_text,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text

