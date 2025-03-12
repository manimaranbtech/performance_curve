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
