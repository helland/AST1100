
import numpy as np
from Dataset import dataset, files
    
if __name__ == '__main__':
    
    filename = files(0, 6)                                                      #['star0_1.05.txt','star1_6.20.txt','star2_1.51.txt','star3_1.21.txt','star4_1.34.txt','star5_false.txt']
    observations = np.empty((len(filename),1), dtype=object)            
    observations = [dataset(filename[i]) for i in xrange(len(filename))]           
    for i in xrange(len(observations)):
        observations[i](1) 
    
    print len(observations[0].time)      

