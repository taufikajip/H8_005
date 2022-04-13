from flask import Flask
app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello, World! 1000'

from flask import request
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return 'request.method == POST, so do the login()'
 
def show_the_login_form():
    return 'request.method == GET, so show the login form()'
    
#Running on http://127.0.0.1:5000 