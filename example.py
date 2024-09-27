import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create figure and axis with specified size
fig, ax = plt.subplots(figsize = (8, 6))

# Plotting the data
ax.plot(x, y, label = 'Sine Wave')

# Setting titles and labels with specified fonts and sizes
font_title = {'family': 'serif', 'color': 'black', 'size': 20}
font_label = {'family': 'serif', 'color': 'black', 'size': 14}

ax.set_title('Sine Wave Example', fontdict = font_title)
ax.set_xlabel('X Axis (Radians)', fontdict = font_label)
ax.set_ylabel('Y Axis (Amplitude)', fontdict = font_label)

# Setting legend location with first choice 'upper right', fallback 'upper left'
ax.legend(loc = 'upper right')

# Use tight layout for better spacing
plt.tight_layout()

# Save figure to .pdf with high resolution
plt.savefig('./sine_wave_plot.pdf', dpi = 300, bbox_inches = 'tight')

# Show plot
plt.show()
