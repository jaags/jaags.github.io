#! /usr/bin/python

from PIL import Image
import os, sys

path = "/home/hrian/Desktop/github/data_science/images/"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((812,2048), Image.ANTIALIAS).convert()
            imResize.save(f + '_resized.jpg', 'JPEG', quality=90)

    
resize()