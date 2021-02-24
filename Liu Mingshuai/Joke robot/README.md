# Joke robot
It is a robot that can tell jokes, of course you can also choose to read the jokes yourself.
* It is a program I wrote based on the article written by Maishu, 
  but with some personal understanding added, it is a bit different.
* It uses the SQLite database to store the jokes. At the same time, I also wrote a code for the MySQL database. 
  If you want to use this, you need to modify the code.
  
## Requirement
* [python 3.8.2] - The version of Python I am using.
* [sqlite3] - I use the sqlite3 library to store jokes.
* [requests 2.25.1] - I use the requests library to crawl the jokes on the Internet.
* [bs4 0.0.1] - I use the bs4 library to parse the crawled data.
* [PyQt5 5.15.2] - I use the PyQt5 library to create a window for this program.
* [pyttsx3 2.90] - I use pyttsx3 to tell jokes.
* [pymysql 1.0.2] - This is my second method of storing jokes. 
  If you don't want to use MySQL, you don't need to install it.

**Method of installing third-party libraries:**
Enter the following commands in cmd, only one at a time, and then press Enter.(This method only works on Windows.)
* pip install requests
* pip install bs4
* pip install pyqt5 
* pip install pyttsx3
* pip install pymysql
sqlite 3 is built-in in Python and does not need to be installed separately.
  
## How to use:
Navigate to the folder where all the code information is stored in cmd and enter the following command:
`joke_gui.py`