import math
import random
import operator
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

FILENAME = 'breast-cancer-wisconsin.data'

def load_dataset(filename):
    with open(filename, 'r') as file:
        dataset = []
        raw_data = file.read()
        data = raw_data.split()
        for line in data:
            row = line.split(',')
            # Menghapus fitur ID
            row = row[1:]
            # Agar missing value tidak masuk dataset
            if '?' not in row:
                for i in range(len(row)):
                    row[i] = int(row[i]) # Konversi data ke int
                dataset.append(row)
        return dataset

def kfold_cross_validation(dataset, k):
    kf = KFold(n_splits=k, shuffle=False)
    for train_index, test_index in kf.split(dataset):
        pass

    train_index = np.array(train_index).tolist()
    test_index = np.array(test_index).tolist()
    training_set = []
    test_set = []
    for index in train_index:
        training_set.append(dataset[index])
    for index in test_index:
        test_set.append(dataset[index])
    return training_set, test_set

def get_distance(instance1, instance2, length, method):
    distance = 0
    if method == 'euclidean':
        for i in range(length):
            distance += pow((instance1[i] - instance2[i]), 2)
        return math.sqrt(distance)
    elif method == 'manhattan':
        for i in range(length):
            distance += abs(instance1[i] - instance2[i])
        return distance
    elif method == 'cosine-similarity':
        xx, xy, yy = 0, 0, 0
        for i in range(length):
            xy += instance1[i] * instance2[i]
            xx += instance1[i] * instance1[i]
            yy += instance2[i] * instance2[i]
        distance = xy / math.sqrt(xx * yy)
        return distance

def KNN(training_set, test_instance, k, method):
    distances = []
    # Panjang dikurangi 1 agar class-nya tidak masuk hitungan
    length = len(test_instance) - 1
    for i in range(len(training_set)):
        dist = get_distance(test_instance, training_set[i], length, method)
        distances.append((training_set[i], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    votes = {}
    for i in range(len(neighbors)):
        response = neighbors[i][-1]
        if response in votes:
            votes[response] += 1
        else:
            votes[response] = 1
    sort_votes = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
    return sort_votes[0][0] 

def get_accuracy(test_set, predictions):
	correct = 0
	for x in range(len(test_set)):
		if test_set[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(test_set))) * 100.0

if __name__ == "__main__":
    dataset = load_dataset(FILENAME)
    training_set, test_set = kfold_cross_validation(dataset, 10)
    print('Training set: ', repr(len(training_set)))
    print('Test set: ', repr(len(test_set)))
    
    k_range = range(1, 31)
    k_score = []
    # Metode: 'euclidean', 'manhattan', 'cosine-similarity'
    metode = 'cosine-similarity'
    for k in k_range:
        predictions = []
        for i in range(len(test_set)):
            result = KNN(training_set, test_set[i], k, metode)
            # print('# Prediksi: ' + repr(result) + ', seharusnya: ' + repr(test_set[i][-1]))
            predictions.append(result)
        accuracy = get_accuracy(test_set, predictions)
        print('K: ' + repr(k) + ', Accuracy: ' + repr(accuracy) + '%')
        k_score.append(accuracy)
    plt.plot(k_range, k_score)
    plt.xlabel('Banyaknya K Tetangga')
    plt.ylabel('Prediksi metode: ' + metode)
    plt.show()
