import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

class dataset():
    
    def __init__(self, v, t, v_pec, starMass):         
        self.time  = t              # List of time data points    
        self.v_rad = v              #radial velocity
        self.v_pec = v_pec          #peculiar velocity
        self.v_rel = []             #relative velocity
        self.v_max = 0     
        self.starMass = starMass

    #execute given action on data set
    def __call__(self, action):     
        if action == 0:     #plot radial velocity                           
            self.plotter(self.v_rad)                   
        if action == 1:     #plot relative velocity                       
            self.velocityCalc()  
            self.plotter(self.v_rad)                   
        if action == 2:     #plot relative velocity with noise
            self.velocityCalc()  
            self.maxV()
            self.noisify()                           
            self.plotter(self.v_rel)                  
 
    # calculate radial velocity 
    def velocityCalc(self):             
        self.v_pec = sum(self.v_rad)/float(len(self.v_rad)) #calculate peculiar velocity 
        self.v_rel = np.array(np.array(self.v_rad) - self.v_pec) #relative velocity   
        
    # actual plot with light curves + velocity curves together
    def plotter(self, v):
        fig = plt.figure()     #Shared figure for plots
        ax1 = fig.add_subplot(1,1,1)                      
        ax1.set_ylabel('V (m/s)') 
        y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
        ax1.yaxis.set_major_formatter(y_formatter)  
        ax1.set_xlabel('t (year)')  
        ax1.plot(self.time[0::100], v[0::100],'r') #only plot every 100 data point, due to excessive data
        fig.savefig('peculiar_plot.png')          

    #find and store maximum value for v_rel
    def maxV(self):
        self.v_max = self.v_rel[0]          
        for i in range(len(self.v_rel)):   
            if self.v_rel[i] > self.v_max: 
                self.v_max = self.v_rel[i] 
                  
    # add random value between -v_max/5 & v_max/5 to v_rel
    def noisify(self): 
        noise = np.random.normal(-self.v_max/5,self.v_max/5,len(self.v_rel))    
        for i in xrange(len(self.v_rel)):          
            self.v_rel[i] = self.v_rel[i]+noise[i]

        

    #find and store maximum value for v_rel
    def minV(self):
        self.v_min = self.v_rel[0]          
        for i in range(len(self.v_rel)):   
            if self.v_rel[i] < self.v_min: 
                self.v_min = self.v_rel[i] 
                self.t_min = i 
                
    #find the drift velocity of the star
    def correctDrift(self):
        drift = (self.v_max+self.v_min) #/(self.t_min-self.t_max) #find drift between max and min and divide by points between them
        for i in range(len(self.v_rel)): 
            self.v_rel[i] = self.v_rel[i]+(drift*i)  #add drift correction to v_rel
        print drift
                  