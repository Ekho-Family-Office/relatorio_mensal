import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'ff3'

# Data to plot
sizes = [67, 33]
labels = ['67%', '33%']
amounts = ['R$ 6.426.380', 'R$ 3.132.842']
colors = ['#4a90e2', '#6bb2f5']  # Colors for each segment

# Plotting the pie chart
fig, ax = plt.subplots()
wedges, _ = ax.pie(
    sizes, 
    colors=colors, 
    startangle=90, 
    counterclock=False, 
    wedgeprops={'edgecolor': 'white'}
)

# Adding custom labels with percentages and amounts
for i, (percent, amount) in enumerate(zip(labels, amounts)):
    # Calculating the angle for the text
    angle = (wedges[i].theta2 + wedges[i].theta1) / 2
    x = np.cos(np.radians(angle)) * 0.7  # Adjust multiplier for text position
    y = np.sin(np.radians(angle)) * 0.7
    
    # Adding a text box with a white background, aligned to the left
    ax.text(
        x, y, f"{percent}\n{amount}", ha='left', va='center', 
        fontsize=14, fontfamily='ff3', fontstyle='normal', fontweight='normal', color='black', 
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3')
    )

# Remove the inner circle to create a full pie chart
centre_circle = plt.Circle((0, 0), 0.01, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that the pie is drawn as a circle
ax.axis('equal')

# Display the chart
plt.show()
