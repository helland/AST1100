from AST1100SolarSystemViewer import AST1100SolarSystemViewer
import numpy as np
from ThreeBodyProblem import planet

seed = 88850
system = AST1100SolarSystemViewer(seed)

# Data about the system.
m = 3.213 * 10**-7   #mass of mars in sun masses
x0 = -1.5               #initial x position of planet
y0 = 0                  #initial y position of planet
v0x = 0                 #initial x velocity of planet
v0y = 0.210828877       #1000 (m/s) *3.154e+7 (1 year in seconds) / 1.496e+11 (1 au)

N = 1000000 #total number of time steps
dt = 400.0/(3.154*10**7)  #time interval (0.0000126823 years / 400 seconds)
T = dt*N    #number of years

times = np.zeros(N) 
posPlanet = np.zeros((N, 2))    #planet values array
posStarm1 = np.zeros((N, 2))    #star 1 values array
posStarm2 = np.zeros((N, 2))    #star 2 values array
starSystem = planet(m,x0,y0,v0x,v0y) #initialize star system

#calculate orbits
starSystem(T,N)
    
#create the array required to create the xml file
for t_i in xrange(N):
    posPlanet[t_i, 0] = starSystem.planetHistory[t_i][2]
    posPlanet[t_i, 1] = starSystem.planetHistory[t_i][3]
    posStarm1[t_i, 0] = starSystem.smallStarHistory[t_i][2]
    posStarm1[t_i, 1] = starSystem.smallStarHistory[t_i][3]
    posStarm2[t_i, 0] = starSystem.bigStarHistory[t_i][2]
    posStarm2[t_i, 1]  = starSystem.bigStarHistory[t_i][3]
    times[t_i] = dt*t_i
      
system.dualStarXml(times, posPlanet, posStarm1, posStarm2) #Will generate the xml file

