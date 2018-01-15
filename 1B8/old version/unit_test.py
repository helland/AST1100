#from Planet import planet
from math import pi, sqrt, exp
from Satellite import satellite
import matplotlib.pyplot as plt
#import unittest
import numpy as np

if __name__ == '__main__':
  
    m = 100 #5.029081*10**-29 #100 kg in sun mass   #mass of satellite
    M = 1.989 * 10**30 * 9.20744797 * 10**-6#9.20744797 * 10**-6 #1.989 * 10**30 * 9.20744797 * 10**-6    #mass of planet (1.989 * 10^30 * 9.20744797 * 10^-06) 18313614012330000000000000
    r = 9634758.4#6.44043818 * 10**-5    #radius of planet  9634758.4 m
    x0 = 0             #initial x position of planet
    y0 = 40000000+r#0.000267383485+r                  #initial y position of planet 40000000 m
    vx0 = -2000#37#-0.2      #au per year         #initial x velocity of planet
    vy0 = -800#10 #-0.2       #1000 (m/s) *3.154e+7 (1 year in seconds) / 1.496e+11 (1 au)
    p = 1.30554911  #(1.496*10**11)**3/(1.989 * 10**30) #atmospheric density (sun masses per cubic au)
    atmosphereHight = ((322000)/(6.667*10**-11*M/r**2))
    A = 20 #*(6.68459*10**-12)**2 #size of parachute in square au
    #print p 
    #print A
    #print 0.5*p*A*vx0**2/m
    #calculate height of atmosphere compared to radius, done in proper units due to conversion errors
    #atmos = 322000/((6.67408*10**(-11)*9.20744797*10**-6*1.989*10**30)/9634758.4**2) #C /(G * M *sun_mass / r^2)
    #ratio = atmos/9634758.4 
    #print p*exp(-(r+24455*1000)/r)
    #print exp(0)
    #print exp(-10)
    lander = satellite(m, M, x0, y0, vx0, vy0, r, p, A)    
    #N = 1000000 #total number of time steps
    dt = 0.03 #3.16887646 * 10**-8 # 10 second in years #400.0/(3.154*10**7)  #time interval (0.0000126823) 
    #T = dt*N    #number of years
    #print (2.15243705 * 10**-6), "divided by ", dt*(4*pi*pi*M/r**2), "equals", (2.15243705 * 10**-6)/(dt*(4*pi*pi*M/r**2)), "vs r=",r, "a/r=",(2.15243705 * 10**-6)/(dt*(4*pi*pi*M/r**2)) / r
    #print T/(3.154*10**7) #print years
    lander(dt)
    
    XposPlanet = lander.orbitHistory[:,0]
    YposPlanet = lander.orbitHistory[:,1]
    print "landing velocity=", sqrt(lander.vX**2+lander.vY**2), "m/s" #*(1.496*10**11/(3.154*10**7))
    print "interations:",len(XposPlanet)
    #create printable arrays
    #for t_i in xrange(N):
    #    XposPlanet[t_i] = lander.orbitHistory[t_i][2]
    #    YposPlanet[t_i] = lander.orbitHistory[t_i][3]
    
    #print-a-planet
    planetPlot = plt.Circle((0, 0), r, color='r')
    atmosRing = plt.Circle((0, 0), atmosphereHight+r, color='g', fill=False)
        

    ax = plt.gca()
    ax.cla() # clear things for fresh plot 
    ax.set_xlim((-6.44043818 * 10**-4, 6.44043818 * 10**-4))
    ax.set_ylim((-6.44043818 * 10**-4, 6.44043818 * 10**-4)) #plt.axis([-60000000, 60000000, -60000000, 60000000])
      
    fig, ax = plt.subplots()
    ax.add_artist(planetPlot)
    ax.add_artist(atmosRing)
    ax.plot(XposPlanet, YposPlanet,'b-')
    plt.xlim(-y0/2, y0) 
    plt.ylim(-y0/2, y0) 
    #print PT.Xpos, "\n\n y: ", PT.Ypos
    #plt.plot(test.Planet.velocityHistory[0], test.Planet.velocityHistory[1])
    #plt.legend(['satellite position'])  
    #plt.xlabel('x')
    #plt.ylabel('y')
    #ax.show()
    plt.show()
    fig.savefig('plot.png')
    
    
    '''
    #unittest.main()
    #test = np.array([5,5])
    #test1 = [[6,6]]
    
    #test = test()
  
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