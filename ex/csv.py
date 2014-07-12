from pandas import read_csv;
import numpy as np;
names = ('year','month','day','hour','min','sec','nsec','lat','lon','amp');
dtype = {'year':np.int16,'month':np.int16,'day':np.int16,'hour':np.int16,'min':np.int16,'sec':np.int16,'nsec':np.int32,'lat':np.float,'lon':np.float,'amp':np.float};
csv = read_csv('c:\\_data\\2013.rn.csv',sep=';',names=names, dtype=dtype);
print csv;
