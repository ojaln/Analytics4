import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from matplotlib import rc
rc('text', usetex=False)
import import_ipynb
import sklearn
from sklearn.pipeline import Pipeline
import pyESN
import pickle
from pyESN import ESN 
#%matplotlib inline

data = open("tesla.txt").read().split()
data = np.array(data).astype('float64')

esn = ESN(n_inputs = 1,
      n_outputs = 1, 
      n_reservoir = 43,
      sparsity = 0.1,
      random_state = 35,
      spectral_radius = 0.1,
      noise = 0.0007)

def customfunct(img):
    img = open("tesla.txt").read().split()
    img = np.array(img).astype('float64')
    trainlen = 1000
    future = 1
    futureTotal = 200
    pred_tot = np.zeros(futureTotal)

    for i in range(0,futureTotal,future):
        pred_training = esn.fit(np.ones(trainlen),data[i:trainlen+i])
        prediction = esn.predict(np.ones(future))
        pred_tot[i:i+future] = prediction[:,0]

    plt.figure(figsize = (16,8))
    plt.plot(range(trainlen,trainlen+futureTotal), data[trainlen:trainlen+futureTotal],'b', label = "Data", alpha = 0.3)
    plt.plot(range(trainlen,trainlen+futureTotal), pred_tot,'k', alpha = 0.8, label = 'Free Running ESN')

    lo,hi = plt.ylim()
    plt.plot([trainlen,trainlen],[lo + np.spacing(1),hi - np.spacing(1)],'k:', linewidth = 4)

    plt.title(r'Ground Truth and Echo State Network Output', fontsize = 30)
    plt.xlabel(r'Time (Days)', fontsize = 18, labelpad = 10)
    plt.ylabel(r'Stock Price', fontsize = 18, labelpad = 10)
    plt.legend(fontsize = 'xx-large', loc =' best')
    sns.despine()

    plt.savefig('final.png')
