# coding: utf8
# imports fot he needed libs
import wiringpi
import smbus
import RPi.GPIO as GPIO
import math
import time
import os

# functions

def cleanup():
    GPIO.cleanup()
    os.system("clear")
    print("cleanup finished exit...")
    time.sleep(1)
    os.system("clear")
    exit

def setup():
    try:
        print "Starting Setup"
        pin = 4
        print "pin was set to", pin
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        print "GPIO, GPIO Mode and PWM Mode were set succesfully"

        wiringpi.pwmSetClock(192)
        wiringpi.pwmSetRange(2000)
        print "PWM clock and Range were set succesfully"

        bus = smbus.SMBus(1)     # Erzeugen und Öffnen einer I2C-Instanz
        print "Bus pin set successfully"
        
        # delcare i2c settings
        i2cAdr = 0x48           # I2C-Adresse des Wandlers
        potiAdr =   0x00        # Poti
        outAdr =    0x40
        
        print("Setup finished succesfully continue in 10 secs")
        time.sleep(0.5)
        # start main function
        main(pin, i2cAdr, potiAdr, bus)

    except KeyboardInterrupt:
        print("Setup failed, starting cleanup")
        cleanup()

def main(pin, i2cAdr, potiAdr, bus):
    try:
        while True:
            bus.write_byte(i2cAdr, potiAdr) 
            value = bus.read_byte(i2cAdr) / 2.55
            pwm = int(value)
            print ("servo kacke: ", pwm)
            wiringpi.softServoWrite(pin, pwm)
            time.sleep(0.2)
    except KeyboardInterrupt:
        os.system("clear")
        print("\nUnexpcted Interruption from the user")
        time.sleep(2)
        cleanup()

setup()
