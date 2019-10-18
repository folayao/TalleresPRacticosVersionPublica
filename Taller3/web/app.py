from flask import Flask, jsonify, request, render_template
import requests
 
app = Flask(__name__, template_folder='templates')
variables_list = ['sensor_en_terreno','img_satelital','img_dron','dato_derivado','valor']

@app.route('/listarSensores', methods = ['GET'])
def listarSensores():
    sensores_list = request.get().json()
    return render_template('listarSensor.html', sensores = sensores_list)

@app.route('/crearSensores', methods = ['GET'])
def crearSensores():
    return render_template('crearSensor.html', variables = variables_list)

@app.route('/guardarSensores', methods = ['POST'])
def guardarSensores():
    sensor = dict(request.values)
    sensor['precio'] = int(sensor['precio'])
    request.post(,json = sensor)

app.run(port=8000, debug=True)