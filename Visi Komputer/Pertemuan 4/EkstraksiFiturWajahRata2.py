# program untuk mengekstraksi fitur rata-rata warna 
# pada setiap channel warna Red, Gree, Blue
# Dataset: Face94 (available at cswww.essex.ac.uk)

import numpy as np
import cv2
import os
os.chdir('D:\Perkuliahan\Semester-5\Visi Komputer\Pertemuan 4')
# variabel fitur bertipe array untuk menyimpan data fitur
# dari 3040 data wajah
# kolom 0 sd 2 untuk menyimpan rata2 intensitas di setiap komponen
# warna R, G, B
# kolom ke-3 untuk menyimpan informasi class

fitur = np.zeros((3040,4),dtype=np.float)

for i in range(1,20):
    for j in range(1,21):
        nama_file='Dataset Wajah\F'+str(i)+'.'+str(j)+'.jpg'
        img = cv2.imread(nama_file,1)
        for k in range(0, 3):
            fitur[(i-1)*20+j-1,k]=img[:,:,k].mean()
        fitur[(i-1)*20+j-1,3]=int(i)

for i in range(1,114):
    for j in range(1,21):
        nama_file='Dataset Wajah\M'+str(i)+'.'+str(j)+'.jpg'
        img = cv2.imread(nama_file,1)
        for k in range(0, 3):
            fitur[380+(i-1)*20+j-1,k]=img[:,:,k].mean()
        fitur[380+(i-1)*20+j-1,3]=int(i+19)
        
for i in range(1,21):
    for j in range(1,21):
        nama_file='Dataset Wajah\MS'+str(i)+'.'+str(j)+'.jpg'
        img = cv2.imread(nama_file,1)
        for k in range(0, 3):
            fitur[2640+(i-1)*20+j-1,k]=img[:,:,k].mean()
        fitur[2640+(i-1)*20+j-1,3]=int(i+132)

# menyimpan fitur ke dalam file csv
np.savetxt('fitur_warna.csv', fitur, delimiter=',', fmt='%f')
