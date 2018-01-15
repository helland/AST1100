from math import sqrt, pi
import numpy as np


class starSystem():
    
    def __init__(self, m): 
        # Initial values                     
        self.x = 0 #x-position of star 
        self.y = 0 #y-position of star  
        self.vX = 0         # velocity of objects
        self.vY =0          # converted from km/s to au/year (vy = 0.210828877)
        self.m = m          #mass of the star
        self.G = 4.0*pi*pi  #gravitational constant        
        self.starHistory = np.zeros((1, 4))
      
    # execute movement of planet over time T in N intervals              
    def __call__(self, planetPositions, planetMass,numberOfPlanets, T, N):  
        dt = T/N    # seconds per given time interval
        self.starHistory = np.zeros((N, 4))   #array of stored position & velocity values for  the star
  
        for i in xrange(N):                                                 
            a_x,a_y = 0,0
            for j in xrange(numberOfPlanets):   #for every planet in the star's vicinity 
                a_x += self.aX(planetPositions[0][j][i], planetPositions[1][j][i], planetMass[j])  #add acceleration in x direction from planet j
                a_y += self.aY(planetPositions[0][j][i], planetPositions[1][j][i], planetMass[j]) #add acceleration in y direction from planet j
                
            self.vX, self.vY = self.newVelocity(a_x, a_y, dt, self.vX, self.vY)                #set next velocity n+1   
            self.x, self.y = self.newPosition( dt, self.x, self.y, self.vX, self.vY)  #set next position n+1  a_x, a_y,
            #self.starHistory[i][0] = self.vX     #store current x velocity n+1 of the planet    
            self.starHistory[i][1] = self.vY     #store current y velocity n+1 of the planet      
            #self.starHistory[i][2] = self.x      #store current x position n+1 of the planet       
            #self.starHistory[i][3] = self.y      #store current y position n+1 of the planet                 
                       
    # returns position in the next step    
    def newPosition(self,dt, x, y, vX, vY):  #a_x, a_y, 
        x = (x + vX*dt ) #  x_(n+1) = x_n + Vx_(n+1)dt
        y = (y + vY*dt ) #  y_(n+1) = y_n + Vy_(n+1)dt
        return x, y
                
    #returns velocity in the next step           
    def newVelocity(self, a_x, a_y, dt, vX, vY):       
        return vX + a_x*dt, vY + a_y*dt
    
    #returns acceleration from gravitational force
    def aX(self, x, y, m): 
        r = sqrt((x-self.x)**2+(y-self.y)**2)     
        return (-(x-self.x)*self.G*m/r**3)
    def aY(self, x, y, m): 
        r = sqrt((x-self.x)**2+(y-self.y)**2)     
        return (-(y-self.y)*self.G*m/r**3) 
