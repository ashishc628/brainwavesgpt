import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Initialize Streamlit app
st.title('Brainwave Frequency Visualization')

# Create a placeholder for the live bar chart
chart = st.empty()

# Generate random brainwave frequencies (replace this with your actual brainwave data)
def generate_brainwave_frequencies():
    while True:
        # Generate random values for different brainwave frequencies
        beta = np.random.uniform(15, 40)
        alpha = np.random.uniform(9, 14)
        theta = np.random.uniform(5, 8)
        delta = np.random.uniform(1.5, 4)
        
        yield beta, alpha, theta, delta
        time.sleep(0.5)  # Delay between updates

# Create a generator to generate brainwave frequencies
brainwave_generator = generate_brainwave_frequencies()

# Create labels for the bar chart
labels = ['Beta', 'Alpha', 'Theta', 'Delta']

# Create initial values for the bar heights
values = [0] * len(labels)

# Create a colormap for the bar colors
colors = cm.viridis(np.linspace(0, 1, len(labels)))

# Create the bar chart
fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=colors)

# Set y-axis limits
ax.set_ylim(0, 40)  # Adjust the upper limit according to your data

# Set labels and title
ax.set_xlabel('Brainwave Frequencies')
ax.set_ylabel('Frequency')
ax.set_title('Brainwave Frequency Visualization')

# Remove the chart borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Hide the ticks on the x-axis
ax.tick_params(axis='x', which='both', bottom=False)

# Update the live bar chart
def update_chart():
    beta, alpha, theta, delta = next(brainwave_generator)
    
    # Update the bar heights
    for bar, value in zip(bars, [beta, alpha, theta, delta]):
        bar.set_height(value)
    
    # Update the chart in the Streamlit app
    chart.pyplot(fig)

# Run the app
if __name__ == '__main__':
    while True:
        update_chart()
