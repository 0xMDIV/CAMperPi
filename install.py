# run script to install important stuff so anyone can run it
import os
import time
import sys

failcounter = int(0)
err0 = 'update failed!'
err1 = 'i2c installation failed!'
err2 = 'python smbus installation failed!'
err3 = 'wiring pi installation failed!'
err4 = 'camera setup failed'
err5 = 'motion installation failed'
err6 = 'full installation failed'
    
def updateOS():
    try:
        print('upgrading Pi OS...')
        # repair broken packages
        os.system('sudo dpkg --configure -a')
        # check for new updates and install when needed
        os.system('sudo apt-get update -y && sudo apt-get upgrade -y')
        os.system('clear')
    except:
        print(err0, sys.exc_info()[0])
        time.sleep(5)


def installi2c():
    try:
        print('installing i2c tools...')
        # download and install the i2c tools, then check if its working
        os.system('sudo apt-get install i2c-tools -y')
        os.system('sudo adduser pi i2c')
        print('tesing if i2c is working')
        os.system('sudo i2cdetect -y 1')
        time.sleep(2)
        os.system('clear')
    except:
        print(err1, sys.exc_info()[0])
        time.sleep(5)


def installSmBus():
    try:
        print('finished installing i2c tools continue...')
        print('install smbus...')
        # install the smbus package
        os.system('sudo apt-get install python-smbus -y')
        os.system('clear')
    except:
        print(err2, sys.exc_info()[0])
        time.sleep(5)
    

def installWiringPi():
    try:
        # install the wiringpi package
        os.system('sudo pip install wiringpi')
        os.system('clear')
        print('wiringPi installation succesfull')
    except:
        print(err3, sys.exc_info()[0]) 
        time.sleep(5) 


def installCamera():
    try:
        print('setup the Camera...')
        print('opening raspi-config where the User needs to go to\n5 -> Camera Enable -> Enable -> back -> Finish')
        os.system('sudo raspi-config')
        print('Adding Camera Drivers')
        # add the camera drivers to auto start
        os.system('sudo modprobe v4l2_common && sudo modprobe bcm2835-v4l2')
        os.system('echo "v4l2_common" | sudo tee -a /etc/modules && echo "bcm2835-v4l2" | sudo tee -a /etc/modules')
        # a show all connected video devices
        os.system('ls /dev/video*')
        print('Camera successfully installed')
        # os.system('clear')
    except:
        print(err4, sys.exc_info()[0])
        time.sleep(5)


def installMotion():
    try:
        print('Install Motion...')
        # install Motion on the pi
        os.system('sudo apt-get install motion')
        os.system('mkdir /home/pi/Desktop/cam')
        os.system('sudo chgrp motion /home/pi/Desktop/cam')
        os.system('chmod g+rwx /home/pi/Desktop/cam')
        # remove standart motion cfgs
        os.system('sudo rm /etc/default/motion')
        os.system('sudo rm /etc/motion/motion.conf')
        # now add our config files
        os.system('sudo mv motion /etc/default/')
        os.system('sudo mv motion.conf /etc/motion/')
        print('Starting Motion')
        os.system('sudo service motion start')
    except:
        print(err5, sys.exc_info()[0])
        time.sleep(5)


def fullInstallation():
    try:
        print('Installation started..\n')
        # full installation
        updateOS()
        installi2c()
        installSmBus()
        installWiringPi()
        installMotion()
        installCamera()
        os.system('cd /home/pi/Desktop mkdir photo')     
    except:
        print(err6, sys.exc_info()[0])
        time.sleep(5)
    
    
def main():
    try:
        print('----------------CAMperPi Installation Menu----------------')
        print('\n')
        print('Welcome to the CAMperPi Main Menu, what would you like to do?')
        print('1. Full Installation')
        print('2. Update the RaspberryPi')
        print('3. Install the I2c Modules')
        print('4. Install the smbus Modules')
        print('5. Install the wiringPi modules')
        print('6. Install Motion')
        print('7. Activate the Camera')
        print('8. Exit')
        menuChoice = int(input('\nChoose an Option by typing the number and press Enter\n> '))
        print('Your Choice: ', menuChoice)

        if menuChoice == int(1):
            fullInstallation()
        elif menuChoice == int(2):
            updateOS()
        elif menuChoice == int(3):
            installi2c()
        elif menuChoice == int(4):
            installSmBus()
        elif menuChoice == int(5):
            installWiringPi()
        elif menuChoice == int(6):
            installMotion()
        elif menuChoice == int(7):
            installCamera()
        elif menuChoice == int(8):
            print('Thanks for using CAMperPi, we hope ur happy with our product')
            print('Exit...')
            time.sleep(5)
            exit()
    except KeyboardInterrupt:
        print('Installation abgebrochen')
    except:
        print(err6, sys.exc_info()[0])
        time.sleep(5)
    
main()