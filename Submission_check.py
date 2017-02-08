# this file is to check submission file

import numpy as np
import pandas as pd
from matplotlib import pyplot
import seaborn

submission = np.loadtxt('submmission.csv',dtype=int,delimiter=',')
submission[submission<0]=0
print submission
print np.min(submission)
np.savetxt('submmission.csv',submission,fmt='%d',delimiter=',')


shop_info = pd.read_csv('input/shop_info.txt')

for i in range(2000):
    print i+1
    file = 'flow_per_shop/'+str(i+1)+'.csv'
    info = pd.read_csv(file)
    ts = info['count'].values
    location = shop_info.iloc[i,1]
    title1 = shop_info.iloc[i,7]
    title2 = shop_info.iloc[i,8]
    title3 = shop_info.iloc[i,9]

    print location
    print title1
    print title2
    print title3

    pyplot.figure(figsize=(10,8))
    pyplot.plot(np.arange(0,495),ts)
    pyplot.plot(np.arange(495,509),submission[i,1:])
    pyplot.axvline(98,color='brown')
    pyplot.axvline(170,color='red')
    pyplot.axvline(227,color='yellow')
    pyplot.axvline(311,color='green')
    pyplot.axvline(448,color='green')
    pyplot.axvline(464,color='brown')
    pyplot.axvspan(129,142, facecolor='0.5', alpha=0.5)
    pyplot.legend(['ts','10.1','1212','spring D','5.1','Moon','10.1','1111'])
    pyplot.show()
