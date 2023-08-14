###########################################
#   Plot combined raw data (single plot)  #
###########################################


# Import modules
import time
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Specify columns to read from
column_time_local = "time_local"
column_um = "um"

# Set data folder path and save folder names
file_path = "C:/Users/kimda/Onedrive/Documents/PhaenoFlex/data/2023/magnetic_SD/48/shifted_data_48.csv"

# Read and combine data from CSV file
df = pd.read_csv(file_path, skiprows=1, low_memory=False)

# Extract data
times = pd.to_datetime(df[column_time_local]) #, errors='coerce'
um = df[column_um]

# Create plot
plt.figure(figsize=(9, 5))  # Adjust the width and height as needed
#plt.scatter(times, um, marker='o', s=1)
plt.plot(times, um)

# Format x-axis as dates
plt.gcf().autofmt_xdate()

# Set plot title and labels
title = "shifted_data_plot.UBC_Dendrometer_48"
#title = "shifted_data_scatterplot.UBC_Dendrometer_48"
plt.title(title)
plt.xlabel('Timestamp.time_local')
plt.ylabel('displacement.um')

# Save the plot to a specific folder
output_folder = "C:/Users/kimda/Downloads/plots"

# Specify filename for plot
#output_filename = "shifted_scatterplot_48.png"
output_filename = "shifted_plot_48.png"

# Specify output file paths
#output_path = "C:/Users/kimda/Onedrive/Documents/PhaenoFlex/python/plots/shifted_plots/shifted_scatterplot_48.png"
#output_path2 = "C:/Users/kimda/Downloads/problem_dendrometers/shifted_scatterplot_48.png"
output_path = "C:/Users/kimda/Onedrive/Documents/PhaenoFlex/python/plots/shifted_plots/shifted_plot_48.png"
output_path2 = "C:/Users/kimda/Downloads/problem_dendrometers/shifted_plot_48.png"

#plt.show()

# Save plot
plt.savefig(output_path)
plt.savefig(output_path2)
#plt.close()

# Done!
print(f"Saved plot")
