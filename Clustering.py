# this file is to clustering (may be not work)

import sklearn.cluster
import sklearn.preprocessing
import sklearn.cluster
import pandas as pd
import numpy as np
from matplotlib import pyplot

input = np.empty((0,495))
stander = sklearn.preprocessing.MaxAbsScaler()

for i in range(1,2001):
    file = 'flow_per_shop/'+str(i)+'.csv'
    info = pd.read_csv(file)
    ts = info['count'].values
    ts = stander.fit_transform(ts)
    input = np.vstack((input,ts))

print input

cluster = sklearn.cluster.KMeans(n_clusters=20)
af = cluster.fit(input)
print af.cluster_centers_
labels =  af.labels_
np.savetxt('labels.csv',labels,fmt='%d')

for i in range(20):
    indice = np.where(labels==i)[0]
    pyplot.figure()
    for item in indice[:10]:
        pyplot.plot(input[item,:])
    pyplot.show()