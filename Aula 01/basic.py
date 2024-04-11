'''
pré-requisito: é preciso instalar a biblioteca Flask
$ pip3 install flask

Caso seja necessário atualizar o pip:
$ pip3 install --upgrade pip

'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()

'''
how to execute:

1a) open the program in Visual Studio Code and "play" it
1b) run on terminal:
$ python3 01-basic.py
3) for "using" it, on web browser call:
http://127.0.0.1:5000

'''