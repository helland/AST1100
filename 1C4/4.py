import numpy as np
from Dataset import dataset, files

filename = files(0,5) #check first star in interval. change min to see a different star or make a for loop
observations = dataset(filename[4])
#observations.reduceData() #if you want to look at a subset of the data
observations(4)    
earthMass = 5.972 * 10**24
jupiterMass = 1.898 *10**27 

print "The model gives us \n v = ",observations.modelV_rel, " m/s"
print " P = ",observations.modelP, " days"
print "Planet mass = ",observations.planetMass," kg"
print "Planet mass = ",observations.planetMass/jupiterMass," Jupiter masses"


