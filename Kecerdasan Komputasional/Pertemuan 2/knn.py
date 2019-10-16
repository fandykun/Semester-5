import csv
import random
import math
import operator
FILENAME = 'pima-indians-diabetes.csv'
SPLIT = 2/3

# load dataset
def loadDataset(filename):
    with open(filename, 'r') as csvfile:
        data = csv.reader(csvfile)
        dataset = []
        for row in data:
            dataset.append(row)
            print(row)
        for i in range(len(dataset)):
            for j in range(len(dataset[i]) - 1):
                dataset[i][j] = float(dataset[i][j])
        return dataset
    
def normalizeDataset(dataset):
    min_values = []
    max_values = []
    # Mencari min dan max dari setiap kolom
    for i in range(len(dataset[0])):
        colValues = [row[i] for row in dataset]
        # remove classnya
        colValues.pop()
        min_value = min(colValues)
        max_value = max(colValues)
        min_values.append(min_value)
        max_values.append(max_value)
    # re-scale agar isi dataset berada di range 0 - 1
    for row in dataset:
        for i in range(len(row) - 1):
            row[i] = (row[i] - min_values[i]) / (max_values[i] - min_values[i])

# split dataset ke train dan test
def trainTestSplit(dataset, training_set, test_set, split):
    for i in range(len(dataset)):
        if random.random() < split:
            training_set.append(dataset[i])
        else:
            test_set.append(dataset[i])

def euclideanDistance(x1, x2, length):
    distance = 0
    for i in range(length):
        distance += pow(x1[i] - x2[i], 2)
    return math.sqrt(distance)

def getNeighbors(training_set, test_instance, k):
	distances = []
	length = len(test_instance)-1
	for x in range(len(training_set)):
		dist = euclideanDistance(test_instance, training_set[x], length)
		distances.append((training_set[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(test_set, predictions):
	correct = 0
	for x in range(len(test_set)):
		if test_set[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(test_set))) * 100.0

dataset = loadDataset(FILENAME)
normalizeDataset(dataset)
training_set = []
test_set = []
trainTestSplit(dataset, training_set, test_set, SPLIT)
print('Training set: ', repr(len(training_set)))
print('Test set: ', repr(len(test_set)))
predictions = []
k = 5
for i in range(len(test_set)):
    neighbors = getNeighbors(training_set, test_set[i], k)
    result = getResponse(neighbors)
    predictions.append(result)
accuracy = getAccuracy(test_set, predictions)
print('Accuracy: ' + repr(accuracy) + '%')