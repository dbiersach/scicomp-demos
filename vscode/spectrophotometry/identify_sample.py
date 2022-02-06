#!/usr/bin/env python3
# identify_sample.py

import numpy as np
import os


def calc_rel_error(obs, exp):
    err = 0.0
    for i in range(len(obs)):
        err += abs(obs[i] - exp[i]) / exp[i]
    return err


def main():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, "Unknown.csv")
    unknown_levels = np.genfromtxt(file_path, delimiter=",")

    folder_path = os.path.join(folder_path, "samples")
    sample_files = os.listdir(folder_path)

    sample_names = []
    scores = []

    for file in sample_files:
        file_path = os.path.join(folder_path, file)
        sample_levels = np.genfromtxt(file_path, delimiter=",")
        sample_names.append(file[:-4])  # Remove ".csv" from filename
        scores.append(calc_rel_error(unknown_levels, sample_levels))

    match_index = scores.index(min(scores))
    print(f"Best match: {sample_names[match_index]}")


if __name__ == "__main__":
    main()
