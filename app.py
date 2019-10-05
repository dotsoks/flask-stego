# Importing all the libraries
from flask import Flask,render_template,request,redirect,url_for,session
from werkzeug.utils  import secure_filename
import os
from cryptosteganography import CryptoSteganography
import time
import random

# Users
users = {
    'admin' : 'secret123',
    'steve' : 'steve123'
}


#Uploaded files destination
UPLOAD_FOLDER =r'C:\Users\Steve Power\PycharmProjects\flask-stego'
app = Flask(__name__)

# This configuration is for allowing all media types to be upload using flask-upload module
#all_files=UploadSet('media',ALL,default_dest=lambda x: 'media')
#app.config['UPLOADED_ALL_DEST']= r"C:\Users\Steve Power\PycharmProjects\flask-stego"

# Project app secret for session security
app.secret_key = "SECretK1Y"

# Assigning upload directory to app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/test')
def test():
    return "Tested and working properly."
@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/encrypt')
def encrypt():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('encrypt.html')

# Route for encryption
@app.route('/convert',methods=['GET','POST'])
def convert():
    if request.method == 'POST':
        # check if post has file
        file = request.files['file']
        message = request.form['message']
        ps = request.form['password']
        filename = secure_filename(file.filename)
        num=random.randint(1,999)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        crypto_steganography = CryptoSteganography(ps)
        # Naming the stego file
        nm='stego'+str(num)+'.png'
        # Encrypting and hiding a message
        crypto_steganography.hide(os.path.join(app.config['UPLOAD_FOLDER'], filename),nm, message)
        msg='File encrypted successfully.'
        return render_template('index.html',msg=msg)

@app.route('/retrieve')
def retrieve():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('retrieve.html')

@app.route('/decrypt',methods=['GET','POST'])
def decrypt():
    if request.method == 'POST':
        # check if post has file
        file = request.files['file']
        pswd = request.form['password']
        filename = secure_filename(file.filename)
        filename_d='dec_'+filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename_d))
        time.sleep(10)
        # Decrypting file and retrieving message
        decipher = CryptoSteganography(pswd)
        secret = decipher.retrieve(filename_d)
        if secret == None:
            return render_template('incorrect.html')
        else:
            return render_template('message.html',secret=secret)

@app.route('/login',methods=['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password and username in users and users[username] == password:
        session['logged_in'] = True
        return render_template('index.html')
    return render_template('login.html')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('index.html')

@app.route('/logout')
def logout():
    if not session.get('logged_in'):
        return "Not logged in."
    else:
        session['logged_in'] = False
        return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
