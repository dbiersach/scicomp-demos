# plot_reflectance.ipynb


import matplotlib.pyplot as plt
from lab_utils import DataFile, TriadSensor

# Read sample data file
file_name = "UnknownSample"
dataFile = DataFile(file_name)
spectra = dataFile.read()

sensor = TriadSensor()

# Create plot window with title and size
plt.figure(__file__)
ax = plt.axes()

# Plot measured wavelenghts as a colored bar graph
ax.bar(sensor.wavelengths, spectra, color=sensor.colors)

# Decorate the graph with proper lables
ax.set_xlabel("Wavelength (mm)")
ax.set_title(f"Spectrophotometry ({dataFile.sample_name})")
ax.set_ylabel("Reflectance Level")
ax.set_ylim((0, 3000))

# Set figure size
ax.figure.set_size_inches(11, 8)

# Save image of bar chart
ax.figure.savefig(dataFile.image_path)

plt.show()
