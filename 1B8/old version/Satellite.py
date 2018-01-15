from math import sqrt, pi, exp
import numpy as np

class satellite():
    
    def __init__(self, m, M, x, y, v0x, v0y, r, density, A): #, atmosphereHeightRatio
        # Initial values       
        self.x = x  #x-position of satellite
        self.y = y  #y-position of satellite

        self.vX = v0x #x-velocity of satellite
        self.vY = v0y #y-velocity of satellite
        
        self.A = A #satellite parachute area
        self.p = density #atmospheric density
        self.r = r                  #radius of planet
        self.planetMass = M         #mass of planet it orbits
        self.m = m                  #mass of satellite
        self.G = 6.67408*10**(-11) #4*pi*pi  #6.67408*10**(-11) #gravitational constant
        self.h_a = ((322000)/(self.G*self.planetMass/self.r**2)) #2.15243705 * 10**-6
        # initiate array for position and velocity history, for each N steps
        self.orbitHistory = np.array([[self.x, self.y]])#np.array([self.vX, self.vY, self.x, self.y]) 
        #self.orbitHistory[0] =  #add initial values to [0] 
    # Execute movement of planet over time T in N intervals              
    def __call__(self, dt):    
        #print self.h_a,"=atmosphere \n vs r=",self.r,"ratio=",self.h_a/self.r        #*1.496*10**11    
        #print sqrt(self.x**2+self.y**2), ">",(self.r+self.h_a), ">", self.r 
        y0 = self.y
        topOfTheAtmosphere = (self.r+self.h_a)
        #i = 0                     
        #self.orbitHistory = np.zeros((N, 4))   #define size of satellite's orbit history (N steps)
        #while satellite is still outside the planet's radius (above surface) 
        #print sqrt(self.x**2+self.y**2)*100000,"=starting pos \n",(self.r+self.h_a)*100000,"=hit atmosphere\n ", self.r*100000,"=hit surface"
        while (sqrt(self.x**2+self.y**2) > self.r) and (sqrt(self.x**2+self.y**2)<= y0*1.5):            
            if sqrt(self.x**2+self.y**2) > topOfTheAtmosphere: #if above atmosphere
                #print self.orbitHistory[i]
                self.vX, self.vY = self.newVelocity(self.grav(), dt)  #set next velocity n+1 (with only gravity)   
                self.x, self.y = self.newPosition(self.grav(), dt)    #set next position n+1 (with only gravity)   
            else:   # if the satellite has reached the atmosphere
                #print "atmo speed=",self.vX, self.vY
                #print i, self.x, self.y#len(self.orbitHistory)
                self.vX, self.vY = self.newVelocity(self.a(), dt)  #set next velocity n+1 (with gravity + drag)  
                self.x, self.y = self.newPosition(self.a(), dt)    #set next position n+1 (with gravity + drag) 
            self.orbitHistory = np.vstack([self.orbitHistory,[self.x, self.y]]) #self.vX, self.vY,  self.orbitHistory.append([self.vX, self.vY, self.x, self.y])     #store current x velocity n+1     
            #self.orbitHistory[i][1] = self.vY     #store current y velocity n+1    
            #self.orbitHistory[i][2] = self.x      #store current x position n+1     
            #self.orbitHistory[i][3] = self.y      #store current y position n+1
            #if sqrt(self.x**2+self.y**2) <= self.r :
            #    print self.orbitHistory, len(self.orbitHistory)
            #    print sqrt(self.x**2+self.y**2), self.x, self.y
            #i = i+1
        #print "internal lengths=", len(self.orbitHistory)
            
        #print "done"
        #print sqrt(self.orbitHistory[len(self.orbitHistory)-1][0]**2+self.orbitHistory[len(self.orbitHistory)-1][1]**2), " vs ", self.r
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
        #print -self.x*self.G*self.planetMass/(sqrt(self.x**2+self.y**2)**3)
        return [-self.x*self.G*self.planetMass/(sqrt(self.x**2+self.y**2)**3),  # x direction
                -self.y*self.G*self.planetMass/(sqrt(self.x**2+self.y**2)**3)]  # y direction
    #returns drag force by the atmosphere
    def drag(self):
        return [(self.x/sqrt(self.x**2+self.y**2))*(0.5*self.p*self.A*self.vX**2)/self.m,   # x direction
                (self.x/sqrt(self.x**2+self.y**2))*(0.5*self.p*self.A*self.vY**2)/self.m]   # y direction
    # combining gravity + drag
    def a(self):       
        rr = sqrt(self.x**2+self.y**2)
        p = self.p*exp(-(self.r+(rr-self.r)*1000)/self.r)
        #print "p=",p
        #print "x/r=",(self.x/rr)
        #print self.vX**2, "=v*2"
        #print "grav=",-(self.x*self.G*self.planetMass/rr**3)
        #print "drag=",((0.5*self.p*self.A*self.vY**2)/self.m)*(self.y/rr)      
        return [-(self.x*self.G*self.planetMass/rr**3)+((0.5*p*self.A*self.vX**2)/self.m)*(self.x/rr), 
                -(self.y*self.G*self.planetMass/rr**3)+((0.5*p*self.A*self.vY**2)/self.m)*(self.y/rr)]
        
        
        