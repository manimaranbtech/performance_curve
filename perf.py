import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

 # Load data from CSV file
file_csv = input("Enter file name: ")
data = pd.read_csv(file_csv)
    
# Extract stretch ratio and true stress from CSV
current = data['current'].values
torque = data['torque'].values
speed = data['speed'].values

#Battery line
#y2 = int(input("Enter battery voltage: "))
#x2 = int(input("Enter battery current: "))
#x1 = 0
#y1 = 12
#m = (y2-y1)/(x2-x1)
#A_last = current[-1]+10    #last value from current array
#current_bat_line = np.linspace(0, A_last, 10)
#voltage = (current_bat_line*m) + 12
#plt.plot(current_bat_line, voltage)
#plt.savefig('my_plot.png')
