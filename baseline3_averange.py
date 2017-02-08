# baseline 3 using just last 2 week avrange

import numpy as np
import pandas as pd
import sklearn.preprocessing
from matplotlib import pyplot

# load train set and test set
cluster = 0

cluster_file = np.loadtxt('classification/cluster_' + str(cluster) + '.csv', dtype=int)
trainset_file = np.loadtxt('classification/cluster_'+str(cluster)+'_trainset.csv',dtype=int)
testset_file = np.loadtxt('classification/cluster_'+str(cluster)+'_testset.csv',dtype=int)
trainset_x = np.empty((0,140), dtype = int)
trainset_y = np.empty((0,14), dtype = int)
testset_x = np.empty((0,140), dtype = int)
testset_y = np.empty((0,14), dtype = int)

for i in trainset_file:
    data = pd.read_csv('flow_per_shop/'+str(i)+'.csv')
    data = data['count'].values
    len_data = len(data)
    trainset_y = np.vstack((trainset_y,data[len_data-14:]))
    trainset_x = np.vstack((trainset_x,data[len_data-154:len_data-14]))

print trainset_y.shape
print trainset_x.shape

for i in testset_file:
    data = pd.read_csv('flow_per_shop/'+str(i)+'.csv')
    data = data['count'].values
    len_data = len(data)
    testset_y = np.vstack((testset_y,data[len_data-14:]))
    testset_x = np.vstack((testset_x,data[len_data-154:len_data-14]))

print testset_y.shape
print testset_x.shape

testset_x = testset_x[:,-14:]
testset_x = np.mean(testset_x,axis=1)
print testset_x.shape
prediction = np.empty((0,14))
for i in range(len(testset_x)):
    prediction = np.vstack((prediction,np.array([testset_x[i]]*14)))
prediction = np.round(prediction)
print prediction

np.savetxt('test_set/baseline_3_clus_'+str(cluster)+'_label.csv',testset_y,fmt='%d')
np.savetxt('test_set/baseline_3_clus_'+str(cluster)+'_predict.csv',prediction,fmt='%d')

# scoring
sum = 0.
for i in range(testset_y.shape[0]):
    for j in range(testset_y.shape[1]):
        sum += np.absolute((prediction[i,j]-testset_y[i,j])/(prediction[i,j]+testset_y[i,j]+0.000000001))
nt = float((testset_y.shape[0]*testset_y.shape[1]))
score = sum/nt
print score

# predicting to submission
submission = np.empty((0,14))

for i in cluster_file:
    data = pd.read_csv('flow_per_shop/' + str(i) + '.csv')
    data = data['count'].values
    data = np.mean(data[-7:])
    submission = np.vstack((submission,np.array([data]*14)))
submission = np.round(submission)
print submission.shape
np.savetxt('submission/baseline_3_clus_' + str(cluster) + '_predict.csv', submission, fmt='%d')

# visualizing check
counter = 0
for i in cluster_file:
    print counter
    data = pd.read_csv('flow_per_shop/' + str(i) + '.csv')
    data = data['count'].values
    pyplot.figure()
    pyplot.plot(np.arange(0,495),data)
    pyplot.plot(np.arange(495,509),submission[counter])
    pyplot.show()
    counter+=1