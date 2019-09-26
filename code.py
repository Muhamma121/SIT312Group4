from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time
from RPLCD import CharLCD
from signal import pause
magPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(magPin, GPIO.OUT)
lcd = CharLCD(numbering_mode=GPIO.BCM,cols=16,rows=2, pin_rs=25, pin_e=8, pins_data=[10,9,11,7])




KEYPAD = [
    ["1","2","3","A"],
    ["4","5","6","B"],
    ["7","8","9","C"],
    ["*","0","#","D"]
]

code = ""
pin="1234"
ROW_PINS = [4,14,15,17]
COL_PINS = [27,22,23,24]
factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
def doKey(key):
        global code
        global pin
        global magPin
        code += key
        lcd.write_string('*')
        print(code)
        if(len(code) == 4):
            lcd.clear()
            if(code==pin):
                lcd.write_string('Welcome')
                print("Welcome")
                code=""
                GPIO.output(magPin,GPIO.LOW)
            else:
                lcd.write_string("Wrong Code")
                print("Invalid Code")
                code=""
                GPIO.output(magPin,GPIO.HIGH)
            time.sleep(2)
            lcd.clear()

keypad.registerKeyPressHandler(doKey)
pause()
