# run script to install important stuff so anyone can run it
import os

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
    os.system('git clone git://git.drogon.net/wiringPi')
    os.system('cd wiringPi')
    os.system('./build')
    os.system('git pull origin')
    os.system('./build')
    os.system('cd')
    os.system('clear')
    print('wiringPi installation succesfull')
except:
    print(err3)
    failcounter += 1

try:
    print('setup the Camera...')
    print('')
    os.system('')

except:
    print(err4)
    failcounter += 1

if failcounter > 2:
    print("to many errors...............Exiting")
    