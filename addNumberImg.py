#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import fnmatch
from PIL import Image, ImageDraw, ImageFont
import sys

#set variables 
imagenes=[]
img_name=[]
number = 1
n = 0
font = ImageFont.truetype("arial.ttf", 60)
#getting path of files
for dirpath, dirnames, filenames in os.walk("Slabs Resized/"):
    for filename in filenames:
        if fnmatch.fnmatch(filename, '*.jpg'):
            imagenes.append(os.path.join(dirpath, filename))
            img_name.append(filename)
#Painting numbers
#if you wish add series number, you can concatenate number vith another variable
#For example: series + number.
for img in imagenes:
    image = Image.open(img)
    draw = ImageDraw.Draw(image)
    draw.text((50, 50), str(number), font=font, fill="red")
    number += 1
    image.save("done/"+ img_name[n])
    n += 1
