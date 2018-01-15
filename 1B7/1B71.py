from AST1100SolarSystemViewer import AST1100SolarSystemViewer
import numpy as np
from Planet import planet

seed = 88850
system = AST1100SolarSystemViewer(seed)

planetsRadius = system.radius     # Radiuses of planets, [km].
planetsMass = system.mass         # Mass of the planets, [solar masses].
planets_initial_x0 = system.x0    # Initial x-position of planets, [AU].
planets_initial_y0 = system.y0    # Initial y-position of planets, [AU].
planets_initial_vx0 = system.vx0  # Initial x-velocity of planets, [AU].
planets_initial_vy0 = system.vy0  # Initial y-velocity of planets, [AU].

# Data about the system.
numberOfPlanets = system.numberOfPlanets # Number of planets in the system.
starRadius = system.starRadius      # Radius of star, [km]
starMass = system.starMass          # Mass of the star, [solar masses].

planets = np.empty((numberOfPlanets,1), dtype=object) #planet object array
T = 50.0        #number of years
N = 500000      #total number of time steps
dt = T/N        #time interval
times = np.zeros(N) 
pos_computed = np.zeros((2, system.numberOfPlanets, N))

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
        pos_computed[0, p_no, t_i] = planets[p_no].planetHistory[t_i][2]
        pos_computed[1, p_no, t_i] = planets[p_no].planetHistory[t_i][3]
        
system.orbitXml(pos_computed, times) #Will generate the xml file


