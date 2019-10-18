from flask import Flask, jsonify, request
from flask_cors import CORS
from TalleresPracticosVersionPublica.Taller3.controllers.TipoSensores import tipoSensor

app = Flask (__name__)
CORS(app)

@app.route('/tipoSensores', methods = ['GET'])
def getAll():
    return (tipoSensor.list)
        
@app.route('/tipoSensores', methods = ['POST'])
def postOne():
    body  = request.json()
    return  (tipoSensor.create(body))

app.run(port=5000,debug=True)
    