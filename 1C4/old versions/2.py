from math import pi

def massEstimate(m, v, P):
    return m**(2/3)*v*P**(1/3)/(2*pi*6.667*10**-11)

m = float(raw_input('Mass of star:  '))
v = float(raw_input('radial velocity:  '))
P = float(raw_input('Orbital Period:  '))

print "Lower limit of the planet's mass (at i=90): ",massEstimate(m, v, P)

