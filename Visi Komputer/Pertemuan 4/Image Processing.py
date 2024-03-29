import numpy as np
import cv2

img=cv2.imread('Yumna_small.jpg',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

baris=gray.shape[0]
kolom=gray.shape[1]

kernel = np.ones((5,5),dtype=np.float)/25
img_average = np.zeros((baris,kolom),dtype=np.float)
for i in range(2,baris-2):
    for j in range(2,kolom-2):
        respon=0.0
        for k in range(0,5):
            for l in range(0,5):
                respon=respon+kernel[k,l]*float(gray[i+k-2,j+l-2])
        img_average[i,j]=respon

img_average1 = cv2.filter2D(gray,-1,kernel)

kernel2=np.matrix([[0.0, -1.0, 0.0],[-1.0, 4.0,-1.0],[0.0, -1.0, 0.0]])
img_laplacian = cv2.filter2D(gray,-1,kernel2)

img_enhanced = gray+img_laplacian

img_average = np.uint8(img_average)
cv2.imshow('Fotonya Yumna warna',img)
cv2.imshow('Fotonya Yumna warna',img)
cv2.imshow('Fotonya Yumna gray',gray)
cv2.imshow('Rata-rata',img_average)
cv2.imshow('Rata-rata1',img_average1)
cv2.imshow('Laplacian',img_laplacian)
cv2.imshow('Enhanced',img_enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()