from AST1100SolarSystemViewer import AST1100SolarSystemViewer
import numpy as np
from math import pi

seed = 88850
system = AST1100SolarSystemViewer(seed)

planetsRadius = system.radius     # Radiuses of planets, [km].
planetsMass = system.mass         # Mass of the planets, [solar masses].
planets_initial_x0 = system.x0    # Initial x-position of planets, [AU].
planets_initial_y0 = system.y0    # Initial y-position of planets, [AU].
planets_initial_vx0 = system.vx0  # Initial x-velocity of planets, [AU].
planets_initial_vy0 = system.vy0  # Initial y-velocity of planets, [AU].

# Data about the system.
G    = 4 * pi * pi                  # Gravitational constant in astronomical units.
numberOfPlanets = system.numberOfPlanets # Number of planets in the system.
starRadius = system.starRadius      # Radius of star, [km]
starMass = system.starMass          # Mass of the star, [solar masses].
starTemp = system.temperature       # surface temperature of star [K].


T = 1       #number of years
N = 100000  #total number of time steps
times = np.zeros(N) 
'''# Fill out the times-array yourself here, using uniform time steps dt
pos_computed = np.zeros((2, system.numberOfPlanets, N))
for t_i in xrange(N):                    #for each time step...
    for p_no in xrange(numberOfPlanets): #for each planet...
        time = times[t_i]                #the current time step
        pos_computed[0, p_no, t_i] = x + self.vX*dt )#+ 0.5*a[0]*dt**2#calculate the x position of planet p_no
        pos_computed[1, p_no, t_i] = #calculate the y position of planet p_no

        
system.orbitXml(pos_computed, times) #Will generate the xml file


# Fill out the times-array yourself here, using uniform time steps dt

#for t_i in xrange(N):                    #for each time step...
#    for p_no in xrange(numberOfPlanets): #for each planet...
#        time = times[t_i]                #the current time step
#        pos_computed[0, p_no, t_i] =#calculate the x position of planet p_no
#        pos_computed[1, p_no, t_i] = #calculate the y position of planet p_no
'''
print "star radius: ", starRadius, " km"
print "star mass: ", starMass, " sun masses"
print starTemp, " K"
print numberOfPlanets, " #"
print planetsMass, " sun masses"
print planetsRadius, " km"
print "position:\n"
print planets_initial_x0  
print planets_initial_y0 
print "velocity:\n"
print planets_initial_vx0
print planets_initial_vy0 