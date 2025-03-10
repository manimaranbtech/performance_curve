import csv
import matplotlib.pyplot as plt

# Specify the path to your CSV file
csv_file_path = 'performance.csv'

# Initialize empty lists to store data
current = []
torque = []
voltage = []
speed = []
output_power= []
efficiency= []

# Open the CSV file
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append data to the respective lists
        current.append(float(row[0])) # First column (Time)
        torque.append(float(row[1])) # Second column (Temperature)
        voltage.append(float(row[2])) # Third column (Pressure)
        speed.append(float(row[3])) # Fourth column (Humidity)
        output_power.append(float(row[4])) # Fifth column (RH)
        efficiency.append(float(row[5])) # sixth column (RH)


# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot torque on the primary y-axis (left)
ax1.plot(current, voltage, marker='o', color='blue', label='Voltage (V)')
ax1.set_xlabel('current (A)')
ax1.set_ylabel('Voltage (V)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a secondary y-axis for voltage (left)
ax2 = ax1.twinx()
ax2.plot(current, torque, marker='s', color='red', label='torque (Nm)')
ax2.set_ylabel('torque (Nm)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Move the secondary y-axis to the left
ax2.spines['left'].set_position(('outward', 60)) # Move the second y-axis to the left
ax2.spines['left'].set_visible(True) # Make the second y-axis visible
ax2.yaxis.set_label_position('left') # Move the label to the left
ax2.yaxis.set_ticks_position('left') # Move the ticks to the left

# Create a tertiary y-axis for speed (left)
ax3 = ax1.twinx()
ax3.plot(current, speed, marker='^', color='green', label='speed (RPM)')
ax3.set_ylabel('speed (RPM)', color='green')
ax3.tick_params(axis='y', labelcolor='green')

# Move the tertiary y-axis to the left
ax3.spines['left'].set_position(('outward', 120)) # Move the third y-axis further to the left
ax3.spines['left'].set_visible(True) # Make the third y-axis visible
ax3.yaxis.set_label_position('left') # Move the label to the left
ax3.yaxis.set_ticks_position('left') # Move the ticks to the left

# Create a quaternary y-axis for output_power (left)
ax4 = ax1.twinx()
ax4.plot(current, output_power, marker='^', color='black', label='output power (W)')
ax4.set_ylabel('output power (W)', color='black')
ax4.tick_params(axis='y', labelcolor='black')

# Move the quaternary y-axis to the left
ax4.spines['left'].set_position(('outward', 180)) # Move the third y-axis further to the left
ax4.spines['left'].set_visible(True) # Make the third y-axis visible
ax4.yaxis.set_label_position('left') # Move the label to the left
ax4.yaxis.set_ticks_position('left') # Move the ticks to the left

# Create a quinary y-axis for efficiency (left)
ax5 = ax1.twinx()
ax5.plot(current, efficiency, marker='^', color='cyan', label='efficiency (%)')
ax5.set_ylabel('efficiency (%)', color='cyan')
ax5.tick_params(axis='y', labelcolor='cyan')

# Move the quinary y-axis to the left
ax5.spines['left'].set_position(('outward', 240)) # Move the third y-axis further to the left
ax5.spines['left'].set_visible(True) # Make the third y-axis visible
ax5.yaxis.set_label_position('left') # Move the label to the left
ax5.yaxis.set_ticks_position('left') # Move the ticks to the left

# Add legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()
lines5, labels5 = ax5.get_legend_handles_labels()
ax1.legend(lines1 + lines2 + lines3 + lines4 + lines5, labels1 + labels2 + labels3 + labels4 + labels5, loc='upper right')

# Add a title
plt.title('Performanc')

# Show the plot
plt.show()
