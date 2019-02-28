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


def installSmBus():
    try:
        print('finished installing i2c tools continue...')
        print('install smbus...')
        # install the smbus package
        os.system('sudo apt-get install python-smbus -y')
        os.system('clear')
    except:
        print(err2, sys.exc_info()[0])
    

def installWiringPi():
    try:
        print('installing wiringPi ...')
        # install the wiringpi package
        os.system('sudo pip install wiringpi')
        os.system('clear')
        print('wiringPi installation succesfull')
    except:
        print(err3, sys.exc_info()[0])  


def installCamera():
    try:
        print('setup the Camera...')
        print('opening raspi-config where the User needs to go to\n5 -> Camera Enable -> Enable -> back -> Finish')
        os.system('sudo raspi-config')
        print('Adding Camera Drivers')
        # add the camera drivers to the pi and have an option to make the camera auto start
        os.system('sudo modprobe v4l2_common && sudo modprobe bcm2835-v4l2')
        choice = int(input('Do you want to add the Camera into the Autostart? \n\n1. Yes, \n2. No '))

        if choice == int(1):
            os.system('echo "v4l2_common" | sudo tee -a /etc/modules && echo "bcm2835-v4l2" | sudo tee -a /etc/modules')
        elif choice == int(2):
            print('Camera wasnt Added to Autostart')
        else:
            print('nothing was choosen, so it wont be added to auto start')

        # ashow all connected video devices
        os.system('ls /dev/video*')
        print('Camera successfully installed')
        os.system('clear')
    except:
        print(err4, sys.exc_info()[0])


def installMotion():
    try:
        print('Install Motion...')
        # install Motion on the pi
        os.system('sudo apt-get install motion')
    except:
        print(err5, sys.exc_info()[0])



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
    
    


def main():
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
    menuChoice = int(input('\nChoose an Option by typing the number and press Enter'))
    print('\n> ')
    print('Your Choice: ', menuChoice)

    if menuChoice == int(1):
        fullInstallation()
    elif menuChoice == int(2):
        updateOS()
    elif menuChoice == int(3):
        installi2c
    elif menuChoice == int(4):
        installSmBus
    elif menuChoice == int(5):
        installWiringPi
    elif menuChoice == int(6):
        installMotion
    elif menuChoice == int(7):
        installCamera
    elif menuChoice == int(8):
        print('Thanks for using CAMperPi, we hope ur happy with our product')
        print('Exit...')
        time.sleep(5)
        exit()

main()