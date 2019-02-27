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
        os.system('sudo dpkg --configure -a')
        # check for new updates and install when needed
        os.system('sudo apt-get update -y && sudo apt-get upgrade -y')
        os.system('clear')
    except:
        print(err0, sys.exc_info()[0])


def installi2c():
    try:
        print('installing i2c tools...')
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
        os.system('sudo apt-get install python-smbus -y')
        os.system('clear')
    except:
        print(err2, sys.exc_info()[0])
    

def installWiringPi():
    try:
        print('installing wiringPi ...')
        os.system('sudo apt-get install git git-core -y')
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
        os.system('sudo modprobe v4l2_common && sudo modprobe bcm2835-v4l2')
        choice = input('Do you want to add the Camera into the Autostart? y = Yes, n = No ')

        if choice == 'y':
            os.system('echo "v4l2_common" | sudo tee -a /etc/modules && echo "bcm2835-v4l2" | sudo tee -a /etc/modules')
        else:
            print('Camera wasnt Added to Autostart')

        os.system('ls /dev/video*')
        print('Camera successfully installed')
        os.system('clear')
    except:
        print(err4, sys.exc_info()[0])


def installMotion():
    try:
        print('Install Motion...')
        os.system('sudo apt-get install motion')
    except:
        print(err5, sys.exc_info()[0])



def fullInstallation():
    try:
        print('Installation started..\n')
        updateOS()
        installi2c()
        installSmBus()
        installWiringPi()
        installMotion()
        installCamera()
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