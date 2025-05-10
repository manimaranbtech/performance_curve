import matplotlib.pyplot as plt
import csv

# Initialize empty lists/arrays for each column
x_values = []
y_values = []

# Read the CSV file
with open('file_n325.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip header row if your CSV has one
    headers = next(csvreader, None)
    
    # Store each column in separate arrays
    for row in csvreader:
        x_values.append(float(row[0]))  # First column
        y_values.append(float(row[1]))  # Second column

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'b-', label='Data from CSV')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('CSV Data Plot')
plt.grid(True)
plt.legend()

# Save and show the plot
plt.savefig('csv_plot.png', dpi=300, bbox_inches='tight')
