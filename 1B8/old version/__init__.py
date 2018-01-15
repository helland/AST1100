from AST1100SolarSystemViewer import AST1100SolarSystemViewer
import numpy as np
from Satellite import satellite

seed = 88850
system = AST1100SolarSystemViewer(seed)

planetsRadius = system.radius     # Radiuses of planets, [km].
planetsMass = system.mass         # Mass of the planets, [solar masses].
rho0 = system.rho0                # Atmospheric density at surface 
print planetsRadius

# initialize values to be used
m = 100                             #mass of satellite
M = 1.989 * 10**30 * planetsMass[0] #mass of planet
r = planetsRadius[0]*1000    #radius of planet [m]
x0 = 0                  #initial x position of satellite
y0 = 40000000+r         #initial y position of satellite 
vx0 = -2000             #initial x velocity of satellite
vy0 = -800              #initial y velocity of satellite
p = rho0[0]             #atmospheric density 
A = 20                 #size of parachute 
dt = 0.03 #time interval in seconds
print "step 0"
#run satellite module
print "r=",r,"p=",p,"M=",M
lander = satellite(m, M, x0, y0, vx0, vy0, r, p, A)    
lander(dt)
print "step 1"    
#Xpositions = lander.orbitHistory[:,0]   #get x positions from satellite history array
#Ypositions = lander.orbitHistory[:,1]   #get y positions from satellite history array
#Xpositions = Xpositions*6.68459*10**-12 #convert to AU
#Ypositions = Ypositions*6.68459*10**-12 #convert to AU

#get position values from lander object
satPos = np.array([lander.orbitHistory[:,0], lander.orbitHistory[:,1]]) #*6.68459*10**-12
satPos = satPos.T
for i in xrange(len(satPos)):
    satPos[i][0] = satPos[i][0]*6.68459*10**-12
    satPos[i][1] = satPos[i][1]*6.68459*10**-12
    
print "step 2"
#create & fill time array
times = np.zeros(len(satPos))
for t_i in xrange(len(satPos)):
    times[t_i] = (3.17098*10**-8*dt*t_i) #converted from seconds to years
print len(satPos), len(satPos[0]), len(times)       
system.landingSat(satPos, times, 0) #generate the xml file
