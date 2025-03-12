import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

 # Load data from CSV file
    data = pd.read_csv('performance.csv')
    
    # Extract stretch ratio and true stress from CSV
    current = data['current'].values
    torque = data['torque'].values
    speed = data['speed'].values
