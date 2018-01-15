import matplotlib.pyplot as plt
from math import exp
import numpy as np
import os.path
import matplotlib.ticker

def model(flux, wavelength, selftime): 
    model, fmax = 0, 1.0 

    #Rough, by-eye estimates, followed by fine tuning through small changes
    n = 25  #number of values
    fmin = np.linspace(0.86, 0.775, n) 
    sigma = np.linspace(0.005, 0.1, n) 
    lambdacenter = np.linspace(656.343, 656.347, n) 

    delta = [0,0,0] 
    best_delta = 10000000000 
    observed = (sum(flux))/(len(flux)) #F_obs
 
    # Calculate minimal delta by finding the ideal combination of fmin,sgima and lambdacenter
    for i in fmin: 
        for j in sigma: 
            for k in lambdacenter: 
                for l in wavelength[500:800]: #only check certain interval to save selftime
 
                    # Calculate model 
                    testModel = fmax + (i - fmax)*(exp(-(l - k)**2.0/(2.0*(j**2.0)))) 
 
                    # Calculate change                    
                    deltaCurrent = (observed - testModel)**2 
                    
                    # if current delta is smaller than previous smallest delta
                    if deltaCurrent < best_delta: 
                        best_delta = deltaCurrent #set currentDelta as best estimate
                        delta[0] = i 
                        delta[1] = j 
                        delta[2] = k 
    c, f0 = 299792.458, 656.3
    print 'fmin = ',delta[0],', sigma = ',delta[1],' lambdacenter = ',delta[2],'\n'
    print 'relative velocity = ',((delta[2]-f0)/f0)*c,'km/s '
    
    # Create model array
    model = np.zeros(len(selftime)) 
    for i in selftime: 
        model[i] = fmax + (delta[0] - fmax)*(exp(-((wavelength[i] - delta[2])**2.0)/(2.0*(delta[1]**2.0)))) 
    
    return model

def plotter(flux, wavelength, model): 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(wavelength, flux,'r', wavelength, model, 'b') 
    plt.legend(['measured value', 'model'])
    plt.title('1A.6 3)')
    plt.xlabel('Wavelength (nm)')
    x_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
    ax.xaxis.set_major_formatter(x_formatter)
    plt.ylabel('flux')
    plt.show() 
    fig.savefig('Model plot.png')
    
# handle data from file 
def read(filename): 
    i = 0 #index
    file = open(filename, 'r')  
    for data in [x.split() for x in file]: 
        flux.append(float(data[1])) 
        wavelength.append(float(data[0])) 
        index.append(int(i)) 
        i += 1 

    return flux, wavelength, index
 
# 1D.6 3)
flux = [] 
wavelength = []   
index = [] 
filename = 'spectrum_day0.txt'

if os.path.isfile(filename):
    flux, wavelength, index = read(filename)#read file         
    model = model(flux, wavelength, index)  #create model
    plotter(flux, wavelength, model)        #create plot
    






