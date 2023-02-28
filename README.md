# ChatGPT Python QT Client
ChatGPT Python QT Client via API and OPENAPI

<img src="https://raw.githubusercontent.com/nicarley/ChatGPTPythonQTClient/main/chatgptclient.jpg" />

This python client uses the ChatGPT/OpenAI API.  You must get an API Key from User Settings at OPENAI's website:
https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key

Useful Notes:
1.  Make sure you have installed the libraries imported at the top of the list of the Main Chat Window File.  
2.  You must have a text file that containts your API Key only (filepath indicated at the top of the MainChat.py).  
3.  Once you set the API Key in the Text file, simple run python MainChat.py from your enviroment.
4.  When loading the app, it verifies that the file listed is at the filepath specified.  If it is not, it creates it.  If it is, it simply reads in the API Key.
5.  In the app, it displays the API Key listed from the Text file.  If you change the text field to a new api key, when you send your request, it will save the new API key to the text file.  


