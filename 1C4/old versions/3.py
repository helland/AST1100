import numpy as np
from Dataset import dataset, files

filename = files(4,5) # #false star added to the end as a quick fix to running error ['star3_1.21.txt','star4_1.34.txt','star5_false.txt']
observations = np.empty((len(filename),1), dtype=object)
    
observations = [dataset(filename[i]) for i in xrange(len(filename))]           

for i in xrange(len(observations)):
    observations[i](3) #recommended interval: star 3 - 4075 to 4175, star 4 - 2500 - 2600
    #print observations[i].flux
    