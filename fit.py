import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the linear function to fit
def linear_function(x, m, c):
    """
    Linear equation: y = m*x + c
    m: slope
    c: intercept
    """
    return m * x + c

# Specify the path to your CSV file
csv_file_path = 'test_fit.csv'

# Initialize empty lists to store data
current = []
torque = []

# Open the CSV file
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append data to the respective lists
        current.append(float(row[0])) # First column 
        torque.append(float(row[1])) # Second column 

# Perform curve fitting
params, covariance = curve_fit(linear_function, current, torque)

# Extract the fitted parameters
m_fitted, c_fitted = params
print(f"Fitted slope (m): {m_fitted:.4f}")
print(f"Fitted intercept (c): {c_fitted:.4f}")

# Generate fitted y values using the fitted parameters
y_fitted = linear_function(current, m_fitted, c_fitted)

# Plot the data and the fitted curve
plt.scatter(current, torque, color='blue', label='Experimental Data')
plt.plot(x_data, y_fitted, color='red', label='Fitted Line: y = {:.2f}x + {:.2f}'.format(m_fitted, c_fitted))
plt.xlabel('Current (A)')
plt.ylabel('Torque(Nm)')
plt.title('Curve Fitting for Linear Equation')
plt.legend()
plt.grid(True)
# Save the plot to a file
save_path = 'plot.png'  # Save in the current directory
plt.savefig(save_path, dpi=300)
print(f"Plot saved to: {save_path}")
