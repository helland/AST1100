from math import sqrt, pi
import numpy as np

class planet():
    
    def __init__(self, m, M, x, y, v0x, v0y): 
        # Initial values
        #self.au = 1.496*10**11 #AU to meter converter variable
        #self.year = 365*24*60*60 #year in seconds, for conversion
        
        self.x = x #*self.au #x-position of planet
        self.y = y #*self.au #y-position of planet

        self.vX = v0x #*self.au/self.year #x-velocity of planet
        self.vY = v0y #*self.au/self.year #y-velocity of planet

        self.starMass = M   #mass of star planet orbits
        self.m = m          #mass of planet
        self.G = 4*pi*pi    #6.67408*10**(-11) #gravitational constant
        
        # initiate arrays for position and velocity history
        #self.PosVelHistory = np.zeros((1, 4))
        self.Xpos = np.zeros(1)
        self.Ypos = np.zeros(1)
        self.Xvel = np.zeros(1)
        self.Yvel = np.zeros(1)
        #self.positionHistory = np.array([self.x, self.y])
        #self.velocityHistory = np.array([self.vX, self.vY])
        
    # execute movement of planet over time T in N intervals              
    def __call__(self, T, N):
                
        #t = T*self.year    #convert time frame to seconds
        dt = T/N                 # seconds per given time interval
        #self.PosVelHistory = np.zeros((N,4))
        self.Xpos = np.zeros(N) #set number of stored x position values
        self.Ypos = np.zeros(N) #set number of stored y position values
        self.Xvel = np.zeros(N)  # set number of x velocity values
        self.Yvel = np.zeros(N)  # set number of y velocity values
        #times = np.zeros(N)      # array of time intervals     
        i  = 0#, ct, times[0] 0      # current time interval, start time value
        for i in xrange(N):      
            self.vX, self.vY = self.newVelocity(self.A(), dt)  #set next velocity n+1   
            self.x, self.y = self.newPosition(self.A(), dt)    #set next position n+1
            self.Xvel[i] = self.vX     #store current x velocity n+1     
            self.Yvel[i] = self.vY     #store current y velocity n+1    
            self.Xpos[i] = self.x      #store current x position n+1     
            self.Ypos[i] = self.y      #store current y position n+1     
            #ct += dt                     #time = current time + dt
            #if ct != 0 and ct!=N:
            #    times[ct] = times[ct-1]+dt
        
        #store desired array
        
        
    # returns position in the next step    
    def newPosition(self, a, dt):
        x = (self.x + self.vX*dt )#+ 0.5*a[0]*dt**2) # next x_(n+1) = x_n + Vx_(n+1)dt
        y = (self.y + self.vY*dt )#+ 0.5*a[1]*dt**2) # next y_(n+1) = y_n + Vy_(n+1)dt
        return x, y
                
    #returns velocity in the next step           
    def newVelocity(self, a, dt):
        return self.vX + a[0]*dt, self.vY + a[1]*dt
    
    #returns acceleration from gravitational force
    def A(self):
        return [-self.x*self.G*self.starMass/(sqrt(self.x**2+self.y**2)**3), -self.y*self.G*self.starMass/(sqrt(self.x**2+self.y**2)**3)]
    #