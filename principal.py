from flask import Flask
import main
import json


app = Flask(__name__)

data = json.dumps(main.returno)
home = "Entre no '/clima-tempo'"
home1 = json.dumps(home)


@app.route('/')
def home():
    return home1


@app.route('/clima-tempo')
def clima_tempo():
    return data


app.run()
