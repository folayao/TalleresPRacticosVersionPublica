from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

tipo_medicion= {'sensor' : 'DS18B20','variable':'temperatura','unidades':'centigrados'}

mediciones = [
    {'fecha': '2019-08-07 12:23:00',**tipo_medicion, 'valor': random.randint(17,22)},
    {'fecha': '2019-08-06 12:22:00',**tipo_medicion, 'valor': random.randint(17,22)},
    {'fecha': '2019-08-05 12:21:00',**tipo_medicion, 'valor': random.randint(17,22)},
    {'fecha': '2019-08-04 12:14:00',**tipo_medicion, 'valor': random.randint(17,22)},
    {'fecha': '2019-08-04 12:24:00',**tipo_medicion, 'valor': random.randint(17,22)},
    {'fecha': '2019-08-03 12:22:00',**tipo_medicion, 'valor': random.randint(17,22)},
    {'fecha': '2019-08-03 12:20:00',**tipo_medicion, 'valor': random.randint(17,22)}
]

#tipo de medicion

@app.route("/mediciones")
def get():
    return jsonify(mediciones)

@app.route("/index")
def index():
    return render_template("index.html") #Esto es una prueba para manejar render_templates.

@app.route('/mediciones/')#GET obtener info
def getMedia():
    
    
@app.route('/mediciones/')#GETALL obtener info
def getAllMedia():

@app.route('/mediciones/', methods=[POST])#POST es para crear nuevos archivos.
def postMedia():
    


app.run(port=5000, debug=True) #simepre tiene que ir al final para definir el puerto

