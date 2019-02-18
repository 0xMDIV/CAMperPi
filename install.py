# run script to install important stuff so anyone can run it
import os
import time

failcounter = int(0)
err0 = 'update failed!'
err1 = 'i2c installation failed!'
err2 = 'python smbus installation failed!'
err3 = 'wiring pi installation failed!'
err4 = 'camera setup failed'

try:
    print('installing needed stuff...')
    print('upgrade Pi...')
    os.system('sudo apt-get update -y && sudo apt-get upgrade -y')
    os.system('clear')
except:
    print(err0)
    failcounter += 1

try:
    print('pi sucessfull updated, continue...')
    print('installing i2c tools...')
    os.system('sudo apt-get install i2c-tools -y')
    os.system('sudo adduser pi i2c')
    print('tesing if i2c is working')
    os.system('sudo i2cdetect -y 1')
    time.sleep(2)
    os.system('clear')
except:
    print(err1)
    failcounter += 1

try:
    print('finished installing i2c tools continue...')
    print('install smbus...')
    os.system('sudo apt-get install python-smbus -y')
    os.system('clear')
except:
    print(err2)
    failcounter += 1

try:
    print('installing wiringPi ...')
    os.system('sudo apt-get install git git-core -y')
    os.system('sudo pip3 install wiringpi')
    os.system('clear')
    print('wiringPi installation succesfull')
except:
    print(err3)
    failcounter += 1

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
    print(err4)
    failcounter += 1


if failcounter > 2:
    print('to many errors...............Exiting')
    exit()
    