from flask import Flask
import main
import json


app = Flask(__name__)

home = "Entre no '/clima-tempo'"
home1 = json.dumps(home)


@app.route('/')
def home():
    return home1


@app.route('/clima-tempo')
def clima_tempo():
    data = f"""ID: {main.returno['ID']}
    Cidade/UF: {main.returno['Name']} - {main.returno['Estado']}
    País: {main.returno['Pais']}
    Condição:{main.data['condition']}
    Temperatura: {main.data['temperature']}
    Sensação termica: {main.data['sensation']}
    Data-Hora: {main.data['date']}
    """

    return data


app.run(debug=True)
