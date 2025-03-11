import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def case1():
        # Define the linear function to fit
    def linear_function(x, m, c):
        """
        Linear equation: y = m*x + c
        m: slope
        c: intercept
        """
        return m * x + c
    
    # Load data from CSV file (assumes two columns: 'Stretch_Ratio' and 'True_Stress')
    data = pd.read_csv('performance.csv')  # Replace with your actual file name
    
    # Extract stretch ratio and true stress from CSV
    current = data['current'].values
    torque = data['torque'].values
    
    # Perform curve fitting
    params, covariance = curve_fit(linear_function, current, torque)
    
    # Extract the fitted parameters
    m_fitted, c_fitted = params
    print(f"Fitted slope (m): {m_fitted:.4f}")
    print(f"Fitted intercept (c): {c_fitted:.4f}")
    
    # Generate fitted y values using the fitted parameters
    y_fitted = linear_function(current, m_fitted, c_fitted)
    
    # Calculate R² value
    residuals = torque - y_fitted
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((torque - np.mean(torque))**2)
    r_squared = ss_res / ss_tot
    print(f"R² value: {r_squared:.4f}")
    
    # Plot the data and the fitted curve
    plt.scatter(current, torque, color='blue', label='Experimental Data')
    plt.plot(current, y_fitted, color='red', label=f'Fitted Line: y = {m_fitted:.2f}x + {c_fitted:.2f}\nR² = {r_squared:.4f}')
    plt.xlabel('Current (A)')
    plt.ylabel('Torque (Nm)')
    plt.title('Curve Fitting for Linear Equation')
    plt.legend()
    plt.grid(True)
    
    # Show the plot
    plt.show()
    
def case2():
        # Define the quadratic function (second-order polynomial)
    def quadratic_function(x, a, b, c):
        """
        Quadratic equation: y = a*x^2 + b*x + c
        a: coefficient of x^2
        b: coefficient of x
        c: constant term
        """
        return a * x**2 + b * x + c
    
    # Load data from CSV file (assumes two columns: 'Stretch_Ratio' and 'True_Stress')
    data = pd.read_csv('performance.csv')  # Replace with your actual file name
    
    # Extract stretch ratio and true stress from CSV
    current = data['current'].values
    speed = data['speed'].values
    
    # Perform curve fitting
    params, covariance = curve_fit(quadratic_function, current, speed)
    
    # Extract the fitted parameters
    a_fitted, b_fitted, c_fitted = params
    print(f"Fitted coefficients:")
    print(f"a (x^2 term): {a_fitted:.4f}")
    print(f"b (x term): {b_fitted:.4f}")
    print(f"c (constant term): {c_fitted:.4f}")
    
    # Generate fitted y values using the fitted parameters
    y_fitted = quadratic_function(current, a_fitted, b_fitted, c_fitted)
    
    # Calculate R² value
    residuals = speed - y_fitted
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((speed - np.mean(speed))**2)
    r_squared = (ss_res / ss_tot)
    print(f"R² value: {r_squared:.4f}")
    
    # Plot the data and the fitted curve
    plt.scatter(current, speed, color='blue', label='Experimental Data')
    plt.plot(current, y_fitted, color='red')
    plt.xlabel('Current (A)')
    plt.ylabel('Speed (Nm)')
    plt.title('Curve Fitting for Linear Equation')
    plt.legend()
    plt.grid(True)
    
    # Show the plot
    plt.show()
    
def case3():
    print("You selected Option 3")

def default_case():
    print("Invalid option selected")

def switch_case(option):
    # Dictionary mapping options to functions
    switch_dict = {
        1: case1,
        2: case2,
        3: case3,
    }
    
    # Get the function from the dictionary, default to default_case if option is not found
    selected_case = switch_dict.get(option, default_case)
    
    # Execute the selected function
    selected_case()

# Main program
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Torque:Linear")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 4:
                print("Exiting the program.")
                break
            switch_case(choice)
        except ValueError:
            print("Please enter a valid number.")