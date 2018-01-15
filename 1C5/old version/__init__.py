from AST1100SolarSystemViewer import AST1100SolarSystemViewer
import numpy as np
from Planet import planet
from Star import starSystem
from Dataset import dataset

def maxV(v):
    vMax = v[0]         
    for i in range(len(v)):    
        if v[i] > vMax: 
            vMax = v[i]             
    return vMax



seed = 88850
system = AST1100SolarSystemViewer(seed)

planetsRadius = system.radius     # Radiuses of planets, [km].
planetsMass = system.mass         # Mass of the planets, [solar masses].
planets_initial_x0 = system.x0    # Initial x-position of planets, [AU].
planets_initial_y0 = system.y0    # Initial y-position of planets, [AU].
planets_initial_vx0 = system.vx0  # Initial x-velocity of planets, [AU].
planets_initial_vy0 = system.vy0  # Initial y-velocity of planets, [AU].
print planetsMass[0]/0.0009543, "and ",planetsMass[3]/0.0009543, "and ", planetsMass[2]/0.0009543
# Data about the system.
numberOfPlanets = 3 # Number of planets used
starRadius = system.starRadius      # Radius of star, [km]
starMass = system.starMass          # Mass of the star, [solar masses].

# Data about the system.
numberOfPlanets = system.numberOfPlanets # Number of planets in the system.
starRadius = system.starRadius      # Radius of star, [km]
starMass = system.starMass          # Mass of the star, [solar masses].

planets = np.empty((numberOfPlanets,1), dtype=object) #planet object array
T = 50.0        #number of years
N = 500000      #total number of time steps
dt = T/N        #time interval
times = np.zeros(N) 
pos_computed = np.zeros((2, 3, N))

#initiate planets
planets = [planet(planetsMass[i], starMass, planets_initial_x0[i], 
                  planets_initial_y0[i], planets_initial_vx0[i], 
                  planets_initial_vy0[i]) for i in range(numberOfPlanets)]

# fill out time array
for t_i in xrange(N):
    times[t_i] = dt*t_i

#calculate planet orbits
for i in xrange(numberOfPlanets): 
    planets[i](T,N)

#create the array required to create the xml file
for p_no in xrange(numberOfPlanets):
    for t_i in xrange(N):
        if p_no == 0: # only store values from planet 0, 3 & 5
            pos_computed[0, 0, t_i] = planets[p_no].planetHistory[t_i][2]
            pos_computed[1, 0, t_i] = planets[p_no].planetHistory[t_i][3]
        if p_no == 3:
            pos_computed[0, 1, t_i] = planets[p_no].planetHistory[t_i][2]
            pos_computed[1, 1, t_i] = planets[p_no].planetHistory[t_i][3]

        if p_no == 6:
            pos_computed[0, 2, t_i] = planets[p_no].planetHistory[t_i][2]
            pos_computed[1, 2, t_i] = planets[p_no].planetHistory[t_i][3]



planetMasses = [planetsMass[0],planetsMass[3],planetsMass[5]]
star = starSystem(starMass)
star(pos_computed, planetMasses,3, T, N)



velocityData = []


for i in xrange(len(star.starHistory)):   
    velocityData.append(star.starHistory[i][1]*4743.72) #convert to [m/s]

#process data with an already calculated time, radial velocity, given peculiar velocity and star mass
processData = dataset(velocityData, times, -4213.37, starMass)
processData(0)

