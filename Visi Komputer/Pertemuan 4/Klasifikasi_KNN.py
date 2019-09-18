import numpy as np
import math
import csv

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def main():
    # Membaca fitur dari file
    inputFile = 'fitur_warna.csv'
    with open(inputFile, 'r') as f:
        reader=csv.reader(f, delimiter=',')
        fitur=list(reader)
        fitur = np.array(fitur).astype(float)
       
    # membagi data fitur ke dalam testing dan training
    baris=fitur.shape[0]
    kolom=fitur.shape[1]
    fitur_training = np.zeros((int(0.75*float(baris)),kolom-1),dtype=np.float)
    kelas_fitur_training = np.zeros((int(0.75*float(baris)),1),dtype=np.int)
    fitur_testing = np.zeros((int(0.25*float(baris)),kolom-1),dtype=np.float)
    kelas_fitur_testing = np.zeros((int(0.25*float(baris)),1),dtype=np.int)
    
    idx_training = 0
    idx_testing = 0
    for i in range(1,153):
        for j in range(1,16):
            fitur_training[idx_training] = fitur[(i-1)*20+j-1,0:kolom-1]
            kelas_fitur_training[idx_training] = fitur[(i-1)*20+j-1,kolom-1]
            idx_training = idx_training + 1
        for j in range(16,21):
            fitur_testing[idx_testing] = fitur[(i-1)*20+j-1,0:kolom-1]
            kelas_fitur_testing[idx_testing] = fitur[(i-1)*20+j-1,kolom-1]
            idx_testing = idx_testing + 1
    # print(idx_training)
    # print(idx_testing)
    # print(fitur_training[15])
    # print(kelas_fitur_training[0:20])
    # print(kelas_fitur_testing[0:20])
    
    # prediksi knn dengan k=1
    kenali_fitur_testing = np.zeros((int(0.25*float(baris)),1),dtype=np.int)
    for i in range(len(kenali_fitur_testing)):
        distances = 1000000
        idx_tetangga_terdekat = 10000
        for x in range(len(fitur_training)):
            dist = euclideanDistance(fitur_testing[i], fitur_training[x], kolom-1)
            if dist < distances:
                distances = dist
                idx_tetangga_terdekat = x
        kenali_fitur_testing[i]=kelas_fitur_training[idx_tetangga_terdekat]
      
    # hitung akurasi
    jumlah_benar = 0
    jumlah_salah = 0
    for i in range(kenali_fitur_testing.size):
        if (kenali_fitur_testing[i] == kelas_fitur_testing[i]):
            jumlah_benar = jumlah_benar + 1
        else:
            jumlah_salah = jumlah_salah + 1
    akurasi = (float(jumlah_benar)/float(len(kenali_fitur_testing)))*100
    #print(kenali_fitur_testing)
    print('Jumlah benar = ',jumlah_benar)
    print('Jumlah salah = ',jumlah_salah)
    print('Akurasi = ',akurasi)

main()


