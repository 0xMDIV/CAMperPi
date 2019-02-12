# run script to install important stuff so anyone can run it
import os

try:
    print('installing needed stuff...')
    print('upgrade Pi...')
    os.system('sudo apt-get update -y && sudo apt-get upgrade -y')
    os.system('clear')
except:
    print('update failed!')

try:
    print('pi sucessfull updated, continue...')
    print('installing i2c tools...')
    os.system('sudo apt-get install i2c-tools -y')
    os.system('sudo adduser pi i2c')
    print('tesing if i2c is working')
    os.system('sudo i2cdetect -y 1')
    os.system('clear')
except:
    print('installing i2c tools failed!')

try:
    print('finished installing i2c tools continue...')
    print('install smbus...')
    os.system('sudo apt-get install python-smbus -y')
    os.system('clear')
except:
    print('something went wrong')

try:
    print('installing wiringPi ...')
    os.system('sudo apt-get install git git-core -y')
    os.system('git clone git://git.drogon.net/wiringPi')
    os.system('cd wiringPi')
    os.system('./build')
    os.system('git pull origin')
    os.system('./build')
    os.system('cd')
    os.system('clear')
except:
    print('wiring pi installation failed')

try:
    print('wiringPi sucessfull installed, continue...')
except:
    print('something went wrong')





