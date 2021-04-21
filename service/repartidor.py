from PIL import Image, ImageDraw
import os
import glob
import cv2
import numpy as np

# 450, 196, 500, 246/620, 810, 670, 860/1185, 205, 1235, 255/1365, 821, 1415, 871

def cropH(dst, input, height, width, k=1):
    im = Image.open(input)
    imgwidth, imgheight = im.size

    base = os.path.basename(input)
    base = os.path.splitext(base)[0]

    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            try:
                # a.save("IMG-%s.jpg" % k)
                a.save(os.path.join(dst, f'{base}_{k+1}.png'))
            except Exception as erro:
                print('deu ruim')
                print(erro)
            k +=1

def crop(dst, input, areas):
    im = Image.open(input)

    base = os.path.basename(input)
    base = os.path.splitext(base)[0]

    for index, area in enumerate(areas) :
        a = im.crop(area)
        a.save(os.path.join(dst, f'{base}_{index+1}.png'))

def desenharetangulo(dst, input, areas):
    im = Image.open(input)
    img1 = ImageDraw.Draw(im)

    base = os.path.basename(input)
    base = os.path.splitext(base)[0]

    for index, area in enumerate(areas) :
        img1.rectangle(area, fill ="gray", outline ="green")
    im.save(os.path.join(dst, f'{base}_edited.png'))

def acinzentar(dst, input):
    im = cv2.imread(input)

    base = os.path.basename(input)
    base = os.path.splitext(base)[0]

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    equ = cv2.equalizeHist(gray)

    cv2.imwrite(os.path.join(dst, f'{base}_edited_eq_new_2.png'), equ)