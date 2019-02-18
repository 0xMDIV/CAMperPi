# CAMperPi Lib
# Made by Nils & Tim
# Version 1.0
# Last Changed: 18.02.2019
# Ich lass die mal hier weiß noch nicht ob wir sowas brauchen - Nils

class Errors:
    err0 = str
    err1 = str
    err2 = str
    err3 = str
    err4 = str
    failcounter = int

    def __init__(self, err0, err1, err2, err3, err4, failcounter):
        self.err0 = 'update failed!'
        self.err1 = 'i2c installation failed!'
        self.err2 = 'python smbus installation failed!'
        self.err3 = 'wiring pi installation failed!'
        self.err4 = 'camera setup failed'
        self.failcounter = 0