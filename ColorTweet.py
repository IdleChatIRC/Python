#!/usr/bin/env python
import sys
import os
import random
import urllib
from twython import Twython

CONSUMER_KEY = '_CONSUMER_KEY_'
CONSUMER_SECRET = '_CONSUMER_SECRET_'
ACCESS_KEY = '_ACCESS_KEY_'
ACCESS_SECRET = 'ACCESS_SECRET'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

url = 'https://htmlcolors.com/color-image/'
hex1 = ("A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
num1 = random.randrange(0,15)
hex2 = ("A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
num2 = random.randrange(0,15)
hex3 = ("A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
num3 = random.randrange(0,15)
hex4 = ("A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
num4 = random.randrange(0,15)
hex5 = ("A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
num5 = random.randrange(0,15)
hex6 = ("A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
num6 = random.randrange(0,15)

hash = chr(35)

api.update_status(status='The color of the day is: '+hash+''+hex1[num1]+''+hex2[num2]+''+hex3[num3]+''+hex4[num4]+''+hex5[num5]+''+hex6[num6]+' '+url+''+hex1[num1]+''+hex2[num2]+''+hex3[num3]+''+hex4[num4]+''+hex5[num5]+''+hex6[num6]+'.png')

