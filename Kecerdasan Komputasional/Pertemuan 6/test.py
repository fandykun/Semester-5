#importing libraries / modules
import csv
import math
import operator
import numpy as np
from sklearn.model_selection import StratifiedKFold

#1 handle data
def loadDataSet(fn, attrSet=[], classSet=[], ltrSet=[], lteSet=[]):
    with open(fn,'rt') as csvf:
#        to skip the header
        has_header = csv.Sniffer().has_header(csvf.read(1024))
        csvf.seek(0)
        lines = csv.reader(csvf)
        if has_header:
            next(lines)
        dataset = list(lines)
        
#        skip col 1
#        converting input data into float
#        correcting '?' into mode of their atr
#        splitting data into atr and class
        for x in range(len(dataset)):
            for y in range(1,11):
                if(isinstance(dataset[x][y],str)):
                    if(dataset[x][y].isnumeric()==False):
                        dataset[x][y] = float(1)
                    else:
                        dataset[x][y] = float(dataset[x][y])
            classSet.append(dataset[x][10])
            attrSet.append(dataset[x][1:10])                 
            ltrSet.append(dataset[x][1:11])
            lteSet.append(dataset[x][1:11])
#        print("kelas= ",classSet[-1],"\natr= ",attrSet[-1],"\n"
#              ,"len trSet=",(ltrSet[-1]),"\nlen teSet=",(lteSet[0]))
        
#2 similarity
def euclideanDistance(ins1, ins2, length):
    dist = 0
    for x in range(length):
        dist += pow((ins1[x] - ins2[x]), 2)
    return math.sqrt(dist)

def manhattanDistance(ins1, ins2, length):
    dist = 0
    for x in range(length):
        dist += abs(ins1[x] - ins2[x])
    return dist

def cosineSimilarity(ins1, ins2, length):
    dot = 0
    leng1 = 0
    leng2 = 0
    for x in range(length):
        dot += ins1[x] * ins2[x]
        leng1 += pow(ins1[x],2)
        leng2 += pow(ins2[x],2)
    return dot / (math.sqrt(leng1) * math.sqrt(leng2))

#3 k-neighbors
def getNeighbors(trSet, teIns, k, flag):
    distances = []
    length = len(teIns)-1
    for x in range(len(trSet)):
        if(flag==1):
            dist = euclideanDistance(teIns,trSet[x],length)
        elif(flag==2):
            dist = manhattanDistance(teIns,trSet[x],length)
        else:
            dist = cosineSimilarity(teIns,trSet[x],length)
        distances.append((trSet[x], dist))

#    benahi urutan sort
    if(flag==1 or flag==2):
        distances.sort(key=operator.itemgetter(1))
    else:
        distances.sort(key=operator.itemgetter(1), reverse=True)
    neighbors = []
    for c in range(k):
        neighbors.append(distances[c][0])
    return neighbors

#4 class response
def getResponse(nbrs):
    classVotes = {}
    for c in range(len(nbrs)):
        resp = nbrs[c][-1]
        if resp in classVotes:
            classVotes[resp] += 1
        else:
            classVotes[resp] = 1
    sortedVotes = sorted(classVotes.items(), key=lambda kv: kv[1], reverse=True)
    return sortedVotes[0][0]

#5 accuracy (ratio total correct preds out of all preds made)
def getAccuracy(teSet, pred):
    correct = 0
    for x in range(len(teSet)):
        if teSet[x][-1] == pred[x]:
            correct += 1
    return (correct/float(len(teSet)))*100.0

#6 main
def main():
#    persiapan data
    attrSet = []
    classSet = []
    trSet = []
    teSet = []
    ltrSet = []
    lteSet = []
    
#    membuat prediksi
    pred = []
    print('Masukkan nilai K untuk KNN (min 1, maks 10):')
    k = int(input())
    if(k<1 or k>10):
        print('Pilihan K tidak sesuai\n')
        return
    print('\nPilihlah standard pengukuran untuk KNN:')
    print('1\tEuclidean Distance\n2\tManhattan Distance\n3\tCosine Similarity')
    branch = int(input())
    if(branch<1 or branch>3):
        print('Pilihan tidak valid\n')
        return    
    
#    pembagian atribut dan label kelas
    loadDataSet('breast-cancer-wisconsin.data', attrSet, classSet, ltrSet, lteSet)
    
#    list to numpy
    attrSet = np.array(attrSet)
    classSet = np.array(classSet)
    ltrSet = np.array(ltrSet)
    lteSet = np.array(lteSet)
    
#    K-Folding disini
    print('\n')
    accuracy = 0
    skf = StratifiedKFold(n_splits=10)
    counter = 0
    for trSet, teSet in skf.split(attrSet, classSet):
        counter += 1
        train = ltrSet[trSet]
        test = lteSet[teSet]
        for c in range(len(test)):
            nbs = getNeighbors(train, test[c], k, branch)
            result = getResponse(nbs)
            pred.append(result)
#            print('==> prediksi='+repr(result)+'\t| aktual='+repr(test[c][-1]))
        print('Akurasi ke-'+repr(counter)+':\t\t'+repr(getAccuracy(test, pred))+'%')
        accuracy += getAccuracy(test, pred)
    print('Akurasi rata-rata:\t'+repr(accuracy/counter)+'%')

main()