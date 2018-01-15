#from Planet import planet
from ThreeBodyProblem import planet
import matplotlib.pyplot as plt
#import unittest
import numpy as np
'''
class test(unittest.TestCase):

    def __init__(self): 
        self.M = 1.989 * 10**30 
        self.m = 5.972 * 10**24
        self.x = 0
        self.y = 1.496*10**11
        self.v0x = 30000
        self.v0y = 0
        self.Planet = planet(self.m, self.M, self.x, self.y, self.v0x, self.v0y)
        
        self.T = 0.1
        self.N = 30000
        self.t = self.T*365*24*60*60.0  #convert time frame to seconds
        self.dt = self.t/self.N 
        
        self.Planet(self.T, self.N)
        
    def test_positions(self):
        self.assertEqual(len(planet.positionHistory[0]), len(planet.positionHistory[1]))

    def test_velocity(self, velocities):
        self.assertEqual(len(velocities[0]), len(velocities[1]))
    def numberOfPositions(self, N, positions):
        self.assertEqual(len(positions[0]), N)
    def NumberOfVelocities(self,N, velocities):
        self.assertEqual(len(velocities[0]), N)
'''        
        
if __name__ == '__main__':

    m = 3.213 * 10**-7   #mass of mars in sun masses
    x0 = -1.5               #initial x position of planet
    y0 = 0                  #initial y position of planet
    vx0 = 0                 #initial x velocity of planet
    vy0 = 0.210828877       #1000 (m/s) *3.154e+7 (1 year in seconds) / 1.496e+11 (1 au)
    PT = planet(m, x0, y0, vx0, vy0)    

    N = 8000000 #total number of time steps
    dt = 50.0/(3.154*10**7)  #time interval (0.0000126823)
    T = dt*N    #number of years
    PT(T, N)
    
    XposPlanet = np.zeros(N)    #planet values array
    YposPlanet = np.zeros(N)      #planet values array
    XposStarm1 = np.zeros(N)     #star 1 values array
    YposStarm1 = np.zeros(N)      #star 1 values array
    XposStarm2 = np.zeros(N)      #star 2 values array
    YposStarm2 = np.zeros(N)      #star 2 values array
    
    #create printable arrays
    for t_i in xrange(N):
        XposPlanet[t_i] = PT.planetHistory[t_i][2]
        YposPlanet[t_i] = PT.planetHistory[t_i][3]
        XposStarm1[t_i] = PT.smallStarHistory[t_i][2]
        YposStarm1[t_i] = PT.smallStarHistory[t_i][3]
        XposStarm2[t_i] = PT.bigStarHistory[t_i][2]
        YposStarm2[t_i]  = PT.bigStarHistory[t_i][3]
       
        
    ax = plt.gca()  
    fig, ax = plt.subplots()
    ax.plot(XposPlanet, YposPlanet,'r--',XposStarm1, YposStarm1, 'b-', XposStarm2,YposStarm2, 'g-')
    plt.xlim(-10,10) 
    plt.ylim(-10, 10) 
    plt.legend(['Planet position', 'Small star location', 'Large star location'])  
    plt.xlabel('x (AU)')
    plt.ylabel('y (AU)')
    plt.show()
    fig.savefig('plot b72.png')
 
    

    #unittest.main()
    #test = np.array([5,5])
    #test1 = [[6,6]]
    
    #test = test()
'''  
    M = 1.71129 #1 * 1.989 * 10**30 
    m = 9.2*10**-6 #0.000003 * 1.989 * 10**30 #5.972 * 10**24
    x = 2.87 # 0
    y = 0 #1.496*10**11
    v0x = 0 #30000 #2*10**-7
    v0y = 4.8#0
    PT = planet(m, M, x, y, v0x, v0y)    

    T = 27.0
    N = 500000
    #t = T*365*24*60*60.0    #convert time frame to seconds
    dt = T/N *1.0               # seconds per given time interval
    print dt  
    #PT(T, N)
    # main test
    #TP = test.planet
    #print test.dt, test.t
    PT(T, N)
    
    #print PT.Xpos, "\n\n y: ", PT.Ypos
    #plt.plot(test.Planet.velocityHistory[0], test.Planet.velocityHistory[1])
    plt.plot(PT.Xpos, PT.Ypos) 
    plt.show()
'''   