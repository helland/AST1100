import matplotlib.pyplot as plt
from math import * 
import os.path
import matplotlib.ticker



def plotter(filename, flux, wavelength): 
    name = filename.strip('.txt').strip('spectrum_day') 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(wavelength, flux, c='r' )
    plt.legend(['Day %s' % name])
    plt.title('1A.6 1)')
    plt.xlabel('Wavelength (nm)')
    x_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
    ax.xaxis.set_major_formatter(x_formatter)
    plt.ylabel('flux')
    plt.show() 
    figureName = 'Day'   
    figureName +=str(name)
    figureName +='plot.png'
    fig.savefig(figureName)
  
 
# read data from file 
def read(filename): 
    i = 0 
    file = open(filename, 'r')  
    for data in [x.split() for x in file]: # handle rows 
 
        # separate data into lists
        flux.append(float(data[1])) 
        wavelength.append(float(data[0])) 
        i += 1 
        
    return flux, wavelength #, index
 
# 1D.6 1)
f = 0           #days gone without a new observation data
day = 0         #current day
while f <= 14:  #as long as there's been data the past f days, continue to look for new data files
    flux = [] 
    wavelength = []    
    filename = 'spectrum_day'
    filename +=str(day)
    filename +='.txt'
    
    if os.path.isfile(filename): #if data file exist
        flux, wavelength = read(filename)   #read data file        
        plotter(filename, flux, wavelength) #plot data
        
        f = 0   #reset day count 
    else:    
        f +=1   #count day without data
    day +=1
   



