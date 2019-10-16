# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
name = 'D:\Perkuliahan\Semester-5\Visi Komputer\Mencoba\images\palm.jpg'
img = cv2.imread(name,0)
blur = cv2.GaussianBlur(img,(31,31),0)

highpass = cv2.subtract(img,blur)

img_temp = cv2.multiply(img,(1.05-1))
highboost = cv2.add(img_temp,highpass)

hist_eq = cv2.equalizeHist(highboost)

smooth = cv2.GaussianBlur(hist_eq,(11,11),0)
adap = cv2.adaptiveThreshold(smooth, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 25) 

plt.imshow(img,cmap=plt.get_cmap('gray'))
plt.title('reference')
# plt.show()
plt.imshow(blur,cmap=plt.get_cmap('gray'))
plt.title('low pass')
# plt.show()
plt.imshow(highpass,cmap=plt.get_cmap('gray'))
plt.title('high pass')
# plt.show()
plt.imshow(highboost,cmap=plt.get_cmap('gray'))
plt.title('highboost')
# plt.show()
plt.imshow(hist_eq,cmap=plt.get_cmap('gray'))
plt.title('histogram equalization')
# plt.show()
plt.imshow(smooth,cmap=plt.get_cmap('gray'))
plt.title('smoothened')
# plt.show()
plt.imshow(adap,cmap=plt.get_cmap('gray'))
plt.title('adaptive threshold')
plt.show()

