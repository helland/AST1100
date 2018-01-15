from AST1100SolarSystemViewer import AST1100SolarSystemViewer
import numpy as np
from Satellite import satellite

seed = 88850
system = AST1100SolarSystemViewer(seed)

planetsRadius = system.radius     # Radiuses of planets, [km].
planetsMass = system.mass         # Mass of the planets, [solar masses].
rho0 = system.rho0                # Atmospheric density at surface 

# initialize values to be used
m = 100                             #mass of satellite
M = 1.989 * 10**30 * planetsMass[0] #mass of planet converted to [kg]
r = planetsRadius[0]*1000    #radius of planet [m]
x0 = 0                  #initial x position of satellite
y0 = 40000000+r         #initial y position of satellite 
vx0 = -2000             #initial x velocity of satellite
vy0 = -800              #initial y velocity of satellite
p = rho0[0]             #atmospheric density 
A = 20                  #size of parachute 
dt = 0.03               #time interval in seconds

#run satellite module
lander = satellite(m, M, x0, y0, vx0, vy0, r, p, A)    
lander(dt)

#get position values from lander object
satPos = np.array([lander.orbitHistory[:,0], lander.orbitHistory[:,1]]) 
satPos = satPos.T               #Transpose instead of initializing it properly (sorry)
times = np.zeros(len(satPos))   #create array of time intervals

for i in xrange(len(satPos)):
    satPos[i][0] = satPos[i][0]*6.68459*10**-12 #convert from meters to AU
    satPos[i][1] = satPos[i][1]*6.68459*10**-12 #convert from meters to AU
    times[i] = (3.17098*10**-8*dt*i) #converted from seconds to years
    
system.landingSat(satPos, times, 0) #generate the xml file

