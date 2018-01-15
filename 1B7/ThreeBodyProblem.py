from math import sqrt, pi
import numpy as np

class planet():
    
    ''' This object works with hard coded stars and gets input for planet initiation
     This makes the code less general and not very pretty, but reduce work load due to 
     overlapping functions from previous problem. If we were to start over, functions related to 
     movement should have been placed outside the object, so that the planet and both stars could be 
     initiated as objects of their own, essentially the same as a planet, but with higher mass.
     We could possibly have placed the planets & stars in a star system object you can add celestial 
     bodies to etc. with a similar call that calculates each and every celestial body's movement with 
     respect to the others in the system instead of this hard coded, dark forest mess. 
     admittedly, such an open ended multi-body system would probably be an NP-complete 
     problem out of my computer's league.  
    '''
    def __init__(self, m, x, y, v0x, v0y): 
        # Initial values                    
        self.x, self.SSx, self.BSx = x, 0, 3 #x-position of objects (x = -1.5 )
        self.y, self.SSy, self.BSy = y, 0, 0 #y-position of objects  (y = 0
        self.vX, self.SSvX, self.BSvX = v0x, 0,0                  # velocity of objects
        self.vY, self.SSvY, self.BSvY = v0y, 6.32415, -1.5810375  # converted from km/s to au/year (vy = 0.210828877)
        self.BSm = 4.0      # mass of the largest star
        self.SSm = 1.0      # mass of the small star
        self.m = m          #mass of the planet
        self.G = 4.0*pi*pi  #6.67408*10**(-11) #gravitational constant        
        # initiate arrays for position and velocity history of the three objects
        self.planetHistory = np.zeros((1, 4))
        self.smallStarHistory = np.zeros((1, 4))
        self.bigStarHistory = np.zeros((1, 4))
        
    # execute movement of planet over time T in N intervals              
    def __call__(self, T, N):  
        dt = T/N    # seconds per given time interval
        self.planetHistory = np.zeros((N, 4))   #array of stored position & velocity values for planet  
        self.smallStarHistory = np.zeros((N, 4))#array of stored position & velocity values for the small star  
        self.bigStarHistory = np.zeros((N, 4))  #array of stored position & velocity values for the big star
    
        for i in xrange(N):                                    
            #set next iteration of planet position and velocity 
            a = self.A(self.x, self.SSx, self.BSx, self.y, self.SSy, self.BSy, self.SSm, self.BSm) #acceleration
            self.vX, self.vY = self.newVelocity(a, dt, self.vX, self.vY)                #set next velocity n+1   
            self.x, self.y = self.newPosition(a, dt, self.x, self.y, self.vX, self.vY)  #set next position n+1
            #self.planetHistory[i][0] = self.vX     #store current x velocity n+1 of the planet    
            #self.planetHistory[i][1] = self.vY     #store current y velocity n+1 of the planet      
            self.planetHistory[i][2] = self.x      #store current x position n+1 of the planet       
            self.planetHistory[i][3] = self.y      #store current y position n+1 of the planet                 
            #set next iteration of small star position and velocity 
            a = self.A(self.SSx, self.x, self.BSx, self.SSy, self.y, self.BSy, self.m, self.BSm) #acceleration
            self.SSvX, self.SSvY = self.newVelocity(a, dt, self.SSvX, self.SSvY)                    #set next velocity n+1   
            self.SSx, self.SSy = self.newPosition(a, dt, self.SSx, self.SSy, self.SSvX, self.SSvY)  #set next position n+1
            #self.smallStarHistory[i][0] = self.SSvX     #store current x velocity n+1 of the small star    
            #self.smallStarHistory[i][1] = self.SSvY     #store current y velocity n+1 of the small star      
            self.smallStarHistory[i][2] = self.SSx      #store current x position n+1 of the small star       
            self.smallStarHistory[i][3] = self.SSy      #store current y position n+1 of the small star                  
            #set next iteration of big star position and velocity 
            a = self.A(self.BSx, self.SSx, self.x, self.BSy, self.SSy, self.y, self.SSm, self.m) #acceleration
            self.BSvX, self.BSvY = self.newVelocity(a, dt, self.BSvX, self.BSvY)                    #set next velocity n+1   
            self.BSx, self.BSy = self.newPosition(a, dt, self.BSx, self.BSy, self.BSvX, self.BSvY)  #set next position n+1
            #self.bigStarHistory[i][0] = self.BSvX     #store current x velocity n+1 of the big star     
            #self.bigStarHistory[i][1] = self.BSvY     #store current y velocity n+1 of the big star      
            self.bigStarHistory[i][2] = self.BSx      #store current x position n+1 of the big star       
            self.bigStarHistory[i][3] = self.BSy      #store current y position n+1 of the big star               
             
    # returns position in the next step    
    def newPosition(self, a, dt, x, y, vX, vY):
        x = (x + vX*dt )#+ 0.5*a[0]*dt**2) # next x_(n+1) = x_n + Vx_(n+1)dt
        y = (y + vY*dt )#+ 0.5*a[1]*dt**2) # next y_(n+1) = y_n + Vy_(n+1)dt
        return x, y
                
    #returns velocity in the next step           
    def newVelocity(self, a, dt, vX, vY):
        return vX + a[0]*dt, vY + a[1]*dt
    
    #returns acceleration from gravitational force
    def A(self, x, x2, x3, y, y2, y3, m2, m3): #where x & y are the current object, while 2 & 3 are the two other objects

        r2 = sqrt((x-x2)**2+(y-y2)**2)# r vector between self & object 2 
        r3 = sqrt((x-x3)**2+(y-y3)**2)# r vector between self & object 3
        #returns acceleration due to gravitational force from both m2 & m3
        return [(-(x-x2)*self.G*m2/r2**3)+(-(x-x3)*self.G*m3/r3**3),    #x direction
                (-(y-y2)*self.G*m2/r2**3)+(-(y-y3)*self.G*m3/r3**3)]    #y direction
    
    