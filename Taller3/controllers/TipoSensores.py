from flask import Flask, jsonify, request
from db.db import conex 

class tipoSensor():
    global cur
    cur = conex.cursor() 

    def list():
        lista = []

        cur.execute("SELECT * FROM tipo_sensor")
        rows = cur.fetchall()
        colums = [i[0] for i in cur.description]

        for row in rows:
            #create a zip object from two list
            registo = zip(colums, row)
            #Create a  dictionary from zip object
            json = dict(registo)
            lista.append(json)
        return jsonify(lista)
        conex.close

    def create(body):
        #campos
        data = (body ['referencia'], body ['nombre'], body ['variable'], body ['precio'], 
        body ['salida'], body ['imagen'])
        #sentencia SQL
        sql =  "INSERT INTO tipo_sensores (referencia, nombre, variable, precio, salida, imagen) VALUES(%s, %s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        conex.commit()
        return {'estado' : "insertado"}, 200
        