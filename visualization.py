''' concrete_visualization.py
Performs statistical analysis and visualizations on concrete data.
Ruby Nunez
'''

# Importing data
import os
from data import Data
from analysis import Analysis

# Get the current directory
current_directory = os.getcwd()

# Get file
concrete_filename = os.path.join(current_directory, 'data', 'concrete_data.csv')
concrete_filename = 'data/concrete_data.csv'

# Create Data and Analysis object to use functions from Data and Analysis class
concrete_data = Data(concrete_filename)
concrete_an = Analysis(concrete_data)

# Headers to use
header_list = ['ash', 'slag', 'strength', 'water']

# Summary of data
data_mean = concrete_an.mean(header_list)
data_range = concrete_an.range(header_list)
data_std = concrete_an.std(header_list)
print('MEANS\n', data_mean, '\nRANGES\n', data_range, '\nSTANDARD DEVIATIONS\n', data_std)

# Pair plot for headers
fig, axes = concrete_an.pair_plot(header_list, title="Figure 1. Components and Strength of Concrete")

# Scatter plots
x_samps, y_samps = concrete_an.scatter('strength', 'water', 'Figure 2. Water Amount vs. Strength of Concrete')
x_samps, y_samps = concrete_an.scatter('ash', 'slag', 'Figure 3. Ash and Slag Amount in Concrete')

# Show figures
concrete_an.show()