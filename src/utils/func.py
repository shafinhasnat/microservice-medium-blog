import string
import random
from src import redis

def generateUID():
    uid = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
    return uid

def generateOTP(key):
    otp = random.randint(100000, 999999)
    redis.set(key, otp)
    redis.expire(key, 10*60)
    return otp

def getOTP(key):
    otp = redis.get(key)
    if otp:
        return otp.decode("utf-8")
    return -1