from math import pi, exp, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

#global static filenames
def files(min, max):
    filenames = ['star0_1.05.txt','star1_6.20.txt','star2_1.51.txt','star3_1.21.txt','star4_1.34.txt','star5_false.txt']
    return filenames[min : max]

class dataset():
    
    def __init__(self, filename): 
        
        self.time       = []    # List of time data points
        self.wavelength = []    # Observed Wavelength at time data points
        self.flux       = []    # Measured flux at time data points
        self.read(filename)     # Sort data from file into lists   
        self.filename = str(filename).replace(' ', '')[:-4] # strip away '.txt'   
        self.v_rad = []             #radial velocity
        self.v_pec = []             #peculiar velocity
        self.v_rel = []             #relative velocity
        self.fig = plt.figure()     #Shared figure for plots
        self.modelV_rel = 0.0         #relative velocity estimate
        self.modelP = 0.0             #orbital period estimate        
        self.starMass = 0.0
        self.starMassInit(filename) # get mass of star from filename
        self.planetMass = 0.0         #Mass of planet

    #execute given action on data set
    def __call__(self, action):     
        if action == 1: #solve problem 1
            self.velocityCalc()                             #calculate velocity
            self.upperPlot(self.v_rel,'relative velocity')  #relative velocity in upper plot
            self.lowerPlot(self.flux, 'flux')               #flux in lower plot
            self.plotter()                                  #complete plot
        if action == 3: #solve problem 3
            self.reduceData()       #reduce data to a subset of the total
            self.velocityCalc()                             #test
            self.upperPlot(self.v_rel,'relative velocity')  #test
            #self.lowerPlot(self.flux, 'flux')   #plot the light curve 
            self.plotter()          #in the limited interval given
        if action == 4: #solve problem 4
            self.velocityCalc()
            self.model()
            self.mass(self.modelV_rel, self.modelP)

    #reduce data to look at subset 
    def reduceData(self):
        min = int(raw_input('Look at subset of data for '+self.filename+' \n From time interval:  '))
        max = int(raw_input('\n to time interval:  '))
        self.time = self.time[min : max]
        self.flux = self.flux[min : max]
        self.wavelength = self.wavelength[min : max]
        self.filename = str(self.filename).replace('star', 'ReducedDataofStar') #for the sake of distinction in saved figures
        
    # Function that handles data from file 
    def read(self, filename): 
        file = open(filename, 'r') # open file 
       
        for line in file:       # handle rows 
            data = line.split() # split lines 
            
            # append data to lists 
            self.time.append(float(data[0])) 
            self.wavelength.append(float(data[1])) 
            self.flux.append(float(data[2]))    
    
    # calculate radial velocity 
    def velocityCalc(self): 
        lambda_0 = 656.30   # H_alpha
        c = 299792458.0     # light speed       
        for i in self.wavelength:                           #for every wavelength
            self.v_rad.append(((i-lambda_0)/lambda_0)*c)    #use Doppler equation to find radial velocity       
        
        self.v_pec = sum(self.v_rad)/float(len(self.v_rad)) #calculate peculiar velocity 
        self.v_rel = np.array(np.array(self.v_rad) - self.v_pec) #relative velocity    

    # create velocity subplot (separated for neatness sake)
    def upperPlot(self, v, ylabel): 
        ax1 = self.fig.add_subplot(2,1,1)                      
        ax1.set_ylabel(ylabel) 
        y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
        ax1.yaxis.set_major_formatter(y_formatter)
        ax1.plot(self.time, v,'r')
         
    # create light curves subplot (separated for neatness sake)
    def lowerPlot(self, yAxisValues, ylabel): 
        ax2 = self.fig.add_subplot(2,1,2)         
        ax2.set_ylabel(ylabel)    
        ax2.set_xlabel('t (days)')  
        y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
        ax2.yaxis.set_major_formatter(y_formatter)
        ax2.plot(self.time, yAxisValues,'r')         
        
    # actual plot with light curves + velocity curves together
    def plotter(self):
        self.fig.savefig(str(self.filename).replace(str(self.starMass), '')+'plot.png')  #figname              

    # create a model of relative velocity through the least squares approach
    def model(self):   
        t, t0, vr, P = self.modelValues() #automated estimate for intervals    
        delta = [0,0,0] 
        best_delta = 10000000000000000   
     
        # Calculate minimal delta by least square approach
        for i in t0: 
            for j in vr: 
                for k in P:                                     
                    model = j*cos((2*pi/k*(i-t)))               #Calculate model for radial velocity                                    
                    deltaCurrent = sum((self.v_rel - model)**2) #Calculate change 
                    # if current delta is smaller than previous smallest delta
                    if deltaCurrent < best_delta: 
                        best_delta = deltaCurrent #set currentDelta as best estimate
                        delta[0], delta[1], delta[2] = i, j, k 

        self.modelP, self.modelV_rel = delta[2], delta[1] # store best estimate of orbital period & velocity

    #find interval values for the least square approach function. 
    #This sloppy method will only work as long as there is a peak velocity in each half of the data set 
    #If you want it to work in a different data set, just set the limit between two peaks and use the reduceData function to remove extra peaks
    def modelValues(self):
        t1, t2,vr,vr2= self.time[0],self.time[0],self.v_rel[0],self.v_rel[0]    #radial velocity is highest and/or lowest        
        for i in range(len(self.v_rel)):    #for every v_rel value
            if self.v_rel[i] > vr and i<=len(self.time)/2: #if v is higher than previous highest (first half)
                vr = self.v_rel[i]  #store v                   
                t1 = self.time[i]   #store time
            if self.v_rel[i] > vr2 and i>=len(self.time)/2: #if v is higher than previous highest (second half)
                vr2 = self.v_rel[i] #store a second v
                t2 = self.time[i]   #store a second time stamp at the second v peak
        
        P = t2-t1 #period = time steps between the two peaks
        return t1, np.linspace(t1-50, t1+50, 20), np.linspace(vr-10, vr+10, 20), np.linspace(P-50,P+50, 20)
        
    #calculate planet mass from formula (5)
    def mass(self, v, P):
        m_sun = 1.98892*10**30   #solar mass
        G = 6.67428*10**(-11)    #gravitational constant   
        self.planetMass = ((self.starMass * m_sun)**(2.0/3)*v*(P*86400)**(1.0/3))/((2*pi*G)**(1.0/3)) 
    
    #find mass of star from filename
    def starMassInit(self, filename):        
        starMassString = str(filename).replace('star', '')          #remove 'star' string
        for i in xrange(6): #For every star number in range (change range for larger number of data sets)
            starMassString = starMassString.replace(str(i)+'_', '') #remove number from text file
        starMassString = starMassString.replace('.txt', '')         #remove .txt
        try:
            self.starMass = float(starMassString)                   #store remaining numeric value
        except (IndentationError, ValueError):
            pass