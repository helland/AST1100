from math import sqrt, pi
import numpy as np

class planet():
    
    def __init__(self, m, M, x, y, v0x, v0y): 
        # Initial values       
        self.x = x  #x-position of planet
        self.y = y  #y-position of planet

        self.vX = v0x #x-velocity of planet
        self.vY = v0y #y-velocity of planet

        self.starMass = M   #mass of star planet orbits
        self.m = m          #mass of planet
        self.G = 4*pi*pi    #6.67408*10**(-11) #gravitational constant
        
        # initiate array for position and velocity history, for each N steps
        self.planetHistory = np.zeros((1, 4))
        
    # execute movement of planet over time T in N intervals              
    def __call__(self, T, N):                
        dt = T/N                                #seconds per given time interval
        self.planetHistory = np.zeros((N, 4))   #define size of planet history (N steps)
   
        for i in xrange(N):      
            self.vX, self.vY = self.newVelocity(self.A(), dt)  #set next velocity n+1   
            self.x, self.y = self.newPosition(self.A(), dt)    #set next position n+1
            #self.planetHistory[i][0] = self.vX     #store current x velocity n+1     
            #self.planetHistory[i][1] = self.vY     #store current y velocity n+1    
            self.planetHistory[i][2] = self.x      #store current x position n+1     
            self.planetHistory[i][3] = self.y      #store current y position n+1     
        
    # returns position in the next step    
    def newPosition(self, a, dt):
        x = (self.x + self.vX*dt )#+ 0.5*a[0]*dt**2) # next x_(n+1) = x_n + Vx_(n+1)dt
        y = (self.y + self.vY*dt )#+ 0.5*a[1]*dt**2) # next y_(n+1) = y_n + Vy_(n+1)dt
        return x, y
                
    #returns velocity in the next step           
    def newVelocity(self, a, dt):
        return self.vX + a[0]*dt, self.vY + a[1]*dt #v_(n+1) = v_n +a*dt
    
    #returns acceleration from gravitational force
    def A(self):
        return [-self.x*self.G*self.starMass/(sqrt(self.x**2+self.y**2)**3),    # x direction
                 -self.y*self.G*self.starMass/(sqrt(self.x**2+self.y**2)**3)]   # y direction    