# identify_sample.py

import os

import numpy as np
from lab_utils import DataFile


def sum_rel_errors(observed, expected):
    rel_err = 0.0
    for n in range(len(observed)):
        # Relative error = Absolute Error / Known Value
        rel_err += abs(observed[n] - expected[n]) / expected[n]
    return rel_err


dataFile = DataFile("UnknownSample")
spectra = dataFile.read()

# Read in spectra of all known samples
samples_path = os.path.join(dataFile.folder_path, "samples")
samples_files = os.listdir(samples_path)

# Create empty lists to hold comparison value for each known sample
sample_names = []
sample_scores = []

# Find relative error between each known sample's wavelengths and the unknown sample
for file in samples_files:
    file_path = os.path.join(samples_path, file)
    sample_levels = np.genfromtxt(file_path, delimiter=",")
    sample_names.append(file[:-4])  # Remove ".csv" from filename
    sample_scores.append(sum_rel_errors(spectra, sample_levels))

# Print sample names by increasing score (lower is better)
print(f"{'Sample':<15}{'Score':>7}")
print(f"{'------':<15}{'-----':>7}")
sorted_scores = np.argsort(sample_scores)
for i in range(len(sorted_scores)):
    k = sorted_scores[i]
    print(f"{sample_names[k]:<15}{sample_scores[k]:>7.4f}")

# Display the known sample having the least difference to the unknown sample
match_index = sample_scores.index(min(sample_scores))
print(f"\nBest match: {sample_names[match_index]}")
