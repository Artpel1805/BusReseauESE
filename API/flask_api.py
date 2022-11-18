from flask import Flask, jsonify, abort, render_template, request
from uart import *

app = Flask(__name__)

temperatures = []
pressures = []

## TEMPERATURE
@app.route('/temp', methods=['GET', 'POST'])
def funct_temperatures():
        global temperatures
        if request.method=='GET':
                return temperatures
        if request.method=='POST':
                temperature = fetch_temperature()
                temperatures.append(temperature)
                return "", 201

@app.route('/temp/<int:x>', methods=['GET', 'DELETE'])
def funct_temperature(x):
        global temperatures
        if request.method=='GET':
                return str(temperatures[x])
        if request.method=='DELETE':
                del temperatures[x]
                return "", 200


## PRESSURE
@app.route('/pres', methods=['GET', 'POST'])
def funct_pressures():
        global pressures
        if request.method=='GET':
                return pressures
        if request.method=='POST':
                pressure=fetch_pressure()
                pressures.append(pressure)
                return "", 201

@app.route('/pres/<int:x>', methods=['GET', 'DELETE'])
def funct_pressure(x: int):
        global pressures
        if request.method=='GET':
                return str(pressures[x])
        if request.method=='DELETE':
                del temperatures[x]
                return "", 200

