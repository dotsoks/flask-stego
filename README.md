# Flask-stego - Python based steganography tool

* Supports Python3.6
* Web framework used - Flask
* This application store messages protected with AES-256 encryption inside an image.
* Steganography is the art of concealing information within different types of media objects such as images or audio files, in such a way that no one, apart from the sender and intended recipient, suspects the existence of the message. By default steganography is a type of security through obscurity.

# Prerequisites / Dependencies
* Python3.6
* pip3
* flask
* cryptosteganography
* apt-get install python-mysqldb

# Installation
* Follow these steps to clone and run this application on your local system.
* git clone https://github.com/dotsoks/flask-stego.git
* pip3 install -r requirements.txt
* In app.py file, edit this variable and enter your current project directory. 
```angular2
UPLOAD_FOLDER  = 'Current Project Directory'
```
* Change these database connection parameters
```
db = MySQLdb.connect("HOST", "USERNAME", "PASSWORD", "DATABASE")
```
* Once we have all dependecies installed, simple run app.py
* python3 app.py
* Open your browser with your localhost IP address. Web server should be running on port 5000.
