from matplotlib import * 
from math import * 
from numpy import *

# Make class 
class process: 
 
    def __init__(self, filename): 
 
        self.file = filename 
        self.flux = [] 
        self.lambd = [] 
        self.index = [] 
 
        self.read().plot_spec() 
 
    # Function that handles data from file 
    def read(self): 
        i = 0 
        file = open(self.file, 'r') # open file and give attributes 
        for data in [x.split() for x in file]: # start loop handling rows 
 
            # append data to lists 
            self.flux.append(float(data[1])) 
            self.lambd.append(float(data[0])) 
            self.index.append(int(i)) 
            i += 1 
 
        # convert to arrays 
        self.flux = array(self.flux) 
        self.lambd = array(self.lambd) 
        self.index = array(self.index) 
 
        return self 
 
    # 1D.6 1)
    def plot_spec(self): 
        figure() 
        name = self.file 
        name = name.strip('.txt').strip('spectrum_day') 
        plot(self.lambd, self.flux, 'r-', title='Problem 6', legend='Day %s' % (name), xlabel='Wavelength / nm', ylabel='Spectra / flux') 
 
        
        process('spectrum_day0.txt') 
        process('spectrum_day2.txt') 
        process('spectrum_day4.txt') 
        process('spectrum_day6.txt') 
        process('spectrum_day8.txt') 
        process('spectrum_day10.txt') 
        process('spectrum_day11.txt') 
        process('spectrum_day13.txt') 
        process('spectrum_day15.txt') 
        process('spectrum_day17.txt')