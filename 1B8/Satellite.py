from math import sqrt, pi, exp
import numpy as np

class satellite():
    
    def __init__(self, m, M, x, y, v0x, v0y, r, density, A): #, atmosphereHeightRatio
        # Initial values       
        self.x = x  #x-position of satellite
        self.y = y  #y-position of satellite

        self.vX = v0x #x-velocity of satellite
        self.vY = v0y #y-velocity of satellite
        
        self.A = A          #satellite parachute area
        self.p = density    #atmospheric density
        self.r = r                  #radius of planet
        self.planetMass = M         #mass of planet it orbits
        self.m = m                  #mass of satellite
        self.G = 6.67408*10**(-11)  #gravitational constant
        self.h_a = ((322000)/(self.G*self.planetMass/self.r**2))  #AtmosphereHight
        # initiate array for position and velocity history, for each N steps
        self.orbitHistory = np.array([[self.x, self.y]])

    # Execute movement of planet over time T in N intervals              
    def __call__(self, dt):    
        y0 = self.y
        topOfTheAtmosphere = (self.r+self.h_a)
    
        while (sqrt(self.x**2+self.y**2) > self.r) and (sqrt(self.x**2+self.y**2)<= y0*1.5):            
            if sqrt(self.x**2+self.y**2) > topOfTheAtmosphere: #if above atmosphere
                self.vX, self.vY = self.newVelocity(self.a(), dt) #grav() #set next velocity n+1 (with only gravity)   
                self.x, self.y = self.newPosition(self.a(), dt)   #grav()  #set next position n+1 (with only gravity)   
            else:   # if the satellite has reached the atmosphere
                self.vX, self.vY = self.newVelocity(self.a(), dt)  #set next velocity n+1 (with gravity + drag)  
                self.x, self.y = self.newPosition(self.a(), dt)    #set next position n+1 (with gravity + drag) 
            self.orbitHistory = np.vstack([self.orbitHistory,[self.x, self.y]])    #store current position 

    # returns position in the next step    
    def newPosition(self, a, dt):
        x = (self.x + self.vX*dt )#+ 0.5*a[0]*dt**2) # next x_(n+1) = x_n + Vx_(n+1)dt
        y = (self.y + self.vY*dt )#+ 0.5*a[1]*dt**2) # next y_(n+1) = y_n + Vy_(n+1)dt
        return x, y
                
    #returns velocity in the next step           
    def newVelocity(self, a, dt):
        return self.vX + a[0]*dt, self.vY + a[1]*dt #v_(n+1) = v_n +a*dt
    
    #returns acceleration from gravitational force
    def grav(self):
        return [-self.x*self.G*self.planetMass/(sqrt(self.x**2+self.y**2)**3),  # x direction
                -self.y*self.G*self.planetMass/(sqrt(self.x**2+self.y**2)**3)]  # y direction
    # combining gravity + drag
    def a(self):       
        rr = sqrt(self.x**2+self.y**2)
        #print -((rr-self.r)/(75200.0/((self.G*self.planetMass)/self.r**2)))
        p = self.p*exp(-((rr-self.r)/(75200.0/((self.G*self.planetMass)/self.r**2)))) #make atmosphere thinner at the top to improve accuracy with high dt
        #print ((0.5*p*self.A*self.vX**2)/self.m)*(self.x/rr)
        return [-(self.x*self.G*self.planetMass/rr**3)+((0.5*p*self.A*self.vX**2)/self.m)*(self.x/rr), 
                -(self.y*self.G*self.planetMass/rr**3)+((0.5*p*self.A*self.vY**2)/self.m)*(self.y/rr)]
        
        
        