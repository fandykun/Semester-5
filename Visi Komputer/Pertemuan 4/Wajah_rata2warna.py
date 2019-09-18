import numpy as np
import cv2
import pickle

# mengekstraksi fitur citra

fitur = np.zeros((3040,4),dtype=np.float)
#kelas = np.zeros((3040,1),dtype=np.int)
for i in range(1,20):
    for j in range(1,21):
        nama_file='D:\VK_Python\Dataset Wajah\F'+str(i)+'.'+str(j)+'.jpg'
        img = cv2.imread(nama_file,1)
        for k in range(0, 3):
            fitur[(i-1)*20+j-1,k]=img[:,:,k].mean()
        #kelas[(i-1)*20+j-1]=i
        #fitur[(i-1)*20+j-1,3]=int(i)
        fitur[(i-1)*20+j-1,3]=int(i)

for i in range(1,114):
    for j in range(1,21):
        nama_file='D:\VK_Python\Dataset Wajah\M'+str(i)+'.'+str(j)+'.jpg'
        img = cv2.imread(nama_file,1)
        for k in range(0, 3):
            fitur[380+(i-1)*20+j-1,k]=img[:,:,k].mean()
        #kelas[380+(i-1)*20+j-1]=19+i
        #fitur[380+(i-1)*20+j-1,3]=int(i)
        fitur[380+(i-1)*20+j-1,3]=int(i+19)
        
for i in range(1,21):
    for j in range(1,21):
        nama_file='D:\VK_Python\Dataset Wajah\MS'+str(i)+'.'+str(j)+'.jpg'
        img = cv2.imread(nama_file,1)
        for k in range(0, 3):
            fitur[2640+(i-1)*20+j-1,k]=img[:,:,k].mean()
        #kelas[2640+(i-1)*20+j-1]=132+i
        #fitur[2640+(i-1)*20+j-1,3]=int(i)
        fitur[2640+(i-1)*20+j-1,3]=int(i+132)

# menyimpan fitur ke dalam file
outputFile = 'FiturWarnaWajah.data'
fw = open(outputFile, 'wb')
pickle.dump(fitur, fw)
fw.close()


#print(fitur)


#ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#cv2.THRESH_BINARY,3,3)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#cv2.THRESH_BINARY,3,3)
#titles = ['Original Image', 'Global Thresholding (v = 127)',
#'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
#images = [img, th1, th2, th3]
#for i in xrange(4):
#    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()