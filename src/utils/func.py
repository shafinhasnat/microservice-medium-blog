import string
import random

def generateUID():
    uid = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
    return uid

def generateOTP(key):
    return

def getOTP(key):
    return