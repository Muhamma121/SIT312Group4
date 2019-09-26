#!/usr/bin/python
import RPi.GPIO as GPIO
from flask import Flask,request, render_template
import datetime
import time

magPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(magPin, GPIO.OUT)

app = Flask(__name__)
@app.route('/')
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'time' : timeString
        }
    return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>", methods=['POST'])
def action(deviceName, action):
    
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    if deviceName == 'magPin':
        actuator = magPin
        
        
    if action == "on":
        GPIO.output (actuator,GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
        
    templateData = {
        'time' : timeString
        }
    return render_template('index.html', **templateData)


if __name__=='__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
