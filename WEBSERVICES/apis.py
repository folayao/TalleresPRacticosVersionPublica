from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)
CORS(app)

tipo_medicion= {'sensor' : 'PH0-14','variable':'PH','unidades':'Nivel de PH'}

mediciones = [
    {'fecha': '2019-08-07 12:24:00',**tipo_medicion , 'valor': 0.23}
]

#tipo de medicion

@app.route("/mediciones")
def get():
    return jsonify(mediciones)

app.run(port=5000, debug=True) #simepre tiene que ir al final para definir el puerto