import numpy as np
import matplotlib.pyplot as plt
import os.path
import matplotlib.ticker
from Dataset import dataset, files
   
 
if __name__ == '__main__':
    
    filename = ['star0_1.05.txt','star1_6.20.txt','star2_1.51.txt','star3_1.21.txt','star4_1.34.txt','star5_false.txt']
    observations = np.empty((len(filename),1), dtype=object)
            
    observations = [dataset(filename[i]) for i in xrange(len(filename))]           
    print len(observations)
    for i in xrange(len(observations)):
        observations[i](1) 
    
           
            #print "\n time= ",len(time),"\n wavel= ", len(wavelength), '\n flux= ',len(flux)    
    print "star 0, 2, 3 and 4 seem to have a planet in orbit around them. Only the planet around 3 and 4 eclipses their star"

 
 