import numpy as np
from Dataset import dataset, files

filename = files(4,5) #check star 4
observations = dataset(filename[0])
observations(4)    

earthMass = 5.972 * 10**24

print "The model gives us \n v = ",observations.modelV_rel, " m/s"
print " P = ",observations.modelP, " seconds"

print "Planet mass = ",observations.planetMass," kg"
print "Planet mass = ",observations.planetMass/earthMass," Earth masses"