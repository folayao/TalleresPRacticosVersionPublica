
from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
from datetime import datetime
import random
import statistics as stats

app = Flask(__name__)
CORS(app)

tipo_medicion= {'sensor' : 'HC-SR04','variable':'distancia','unidades':'centimetros'}

mediciones = [
    {'fecha': '2019-08-07 12:23:00',**tipo_medicion, 'valor': random.randint(0,100)},
    {'fecha': '2019-08-06 12:100:00',**tipo_medicion, 'valor': random.randint(0,100)},
    {'fecha': '2019-08-05 12:21:00',**tipo_medicion, 'valor': random.randint(0,100)},
    {'fecha': '2019-08-04 12:14:00',**tipo_medicion, 'valor': random.randint(0,100)},
    {'fecha': '2019-08-04 12:24:00',**tipo_medicion, 'valor': random.randint(0,100)},
    {'fecha': '2019-08-03 12:100:00',**tipo_medicion, 'valor': random.randint(0,100)},
    {'fecha': '2019-08-03 12:20:00',**tipo_medicion, 'valor': random.randint(0,100)}
]

#tipo de medicion

@app.route("/index")
def index():
    return render_template("index.html") #Esto es una prueba para manejar render_templates.

@app.route('/mediciones/media')#GET obtener info media
def getMedia():
    counter = 0 
    suma = 0
    for m in mediciones:
        suma = suma + m['valor']
        counter = counter +1
    media = suma/counter
    return jsonify(media)


@app.route('/mediciones/mediana')#GET obtener info mediana
def getMediana():
    
    mediana= []
    for m in mediciones:
        mediana.append(m['valor'])

    return jsonify(stats.median(mediana))
    
@app.route('/mediciones/getAll')#GETALL obtener info
def getAllMedia():
    return jsonify(mediciones)

#@app.route('/mediciones/', methods=[POST])#POST es para crear nuevos archivos.             
#def postMedia():
    


app.run(port=5000, debug=True) #simepre tiene que ir al final para definir el puerto

