#!/usr/bin/env python
import sys
import os
import random
import urllib.request
from twython import Twython
import webcolors
from PIL import Image

CONSUMER_KEY = '_CONSUMER_KEY_'
CONSUMER_SECRET = '_CONSUMER_SECRET_'
ACCESS_KEY = '_ACCESS_KEY_'
ACCESS_SECRET = 'ACCESS_SECRET'



def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

def saveandprint():
    r = lambda: random.randint(0,255)
    color = '%02X%02X%02X' % (r(),r(),r())
    requested_color =  tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    img = Image.new('RGB', (500, 500), color = requested_color)
    img.save('%s.png' % color)
    res = api.upload_media(media = open('%s.png' % color, 'rb'))
    actual_name, closest_name = get_colour_name(requested_color)
    name = actual_name if actual_name else closest_name
    api.update_status(status='Color of the day is %s! #%s #cotd' % (name, color), media_ids=[res['media_id']])
    os.remove("%s.png" % color)

saveandprint()
