# coding: utf8
# importieren der benütigten Bibliotheken
import wiringpi
import smbus
import RPi.GPIO as GPIO
import time
import os
import sys
import datetime

# functions

# Zurücksetzen der GPIO Pins
def cleanup():
    GPIO.cleanup()
    os.system('clear')
    print('cleanup finished exit...')
    time.sleep(1)
    os.system('clear')
    exit

# setup von wiringPi 
def setup():
    try:
        print('Starting Setup')
        # set pin
        pin = int(18)
        print('pin was set to', pin)
        # set wiringpi to Mode GPIO
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        print('GPIO, GPIO Mode and PWM Mode were set succesfully')
        # set pwmClock and pwmRange
        wiringpi.pwmSetClock(512)
        wiringpi.pwmSetRange(2000)
        print('PWM clock and Range were set succesfully')
        # create and open of an I2C-Instanz
        bus = smbus.SMBus(1)
        print('Bus pin set successfully')
        
        # if we would use a cfg file it would be delcared here which var would have which value
        # read cfg 
        # push cfg settings in to the vars
        
        # delcare i2c settings
        i2cAdr = 0x48           # I2C-Adresse des Wandlers
        poti =   0x00        # Poti
        
        print('Setup finished succesfully continue...')
        time.sleep(0.5)
        # return the cfg vars
        return pin, i2cAdr, poti, bus
        #servoMotorAuto(pin, i2cAdr, poti, bus)
    except KeyboardInterrupt:
        print('\nUnexpcted Interruption from the user')
        print('Setup failed, starting cleanup')
        cleanup()
    except IOError as e:
        print('I/O error({0}): {1}'.format(e.errno, e.strerror))
    except:
        print('Unexpected error:', sys.exc_info()[0])


# Zuständig für das Drehen der Servos
def servoMotorAuto(pin, i2cAdr, potiAdr, bus):
    try:
        while True:
            bus.write_byte(i2cAdr, potiAdr) 
            value = bus.read_byte(i2cAdr) / 2.55
            pwm = int(value)
            print ('servo drehwinkel: ', pwm)
            wiringpi.pwmWrite(pin, pwm)
            time.sleep(0.2)
    except KeyboardInterrupt:
        os.system('clear')
        print('\nUnexpcted Interruption from the user')
        time.sleep(2)
        cleanup()
    except IOError as e:
        print('I/O error({0}): {1}'.format(e.errno, e.strerror))
    except:
        print('Unexpected error:', sys.exc_info()[0])

# Erweiterte Funktion um den Servo über das Web steuern zu können
def servoMotorManual(pin, pwm):
    try:     
        print ('servo drehwinkel: ', pwm,' °')
        wiringpi.pwmWrite(pin, pwm)
        time.sleep(0.2)
    except KeyboardInterrupt:
        os.system('clear')
        print('\nUnexpcted Interruption from the user')
        time.sleep(2)
        cleanup()
    except IOError as e:
        print('I/O error({0}): {1}'.format(e.errno, e.strerror))
    except:
        print('Unexpected error:', sys.exc_info()[0])
        
# main zum aufrufen der wichtigsten Funktionen
def main():
    # start the stetup
    setup()
    # setup the vars for the wiring pi and following functions
    pin, i2cAdr, potiAdr, bus = setup()
    # execute automatic servo control over the tunring device
    servoMotorAuto(pin, i2cAdr, potiAdr, bus)
    # execute manual servo control or to turn it for the pictures by and pwm value between 1 and 255
    # servoMotorManual(pin, 30)

main()