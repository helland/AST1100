from math import pi

def massEstimate(m, v, P):
    m_sun = 1.98892*10**30   #solar mass
    G = 6.67428*10**(-11)    #gravitational constant       
    return (m_sun*m)**(2.0/3)*v*(P*86400)**(1.0/3)/(2*pi*G)**(1.0/3)

jupiterMass = 1.898 *10**27 
starMasses = [1.05, 1.51,1.21, 1.34]
for m in starMasses:
    #m = float(raw_input('Mass of star:  '))
    v = float(raw_input('radial velocity:  '))
    P = float(raw_input('Orbital Period:  '))
    

    print "Lower limit of the planet's mass (at i=90): ",massEstimate(m, v, P)," kg"
    print "Planet mass = ",massEstimate(m, v, P)/jupiterMass," Jupiter masses"
