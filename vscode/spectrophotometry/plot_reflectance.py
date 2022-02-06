#!/usr/bin/env python3
# plot_reflectance.py


import matplotlib.pyplot as plt
import numpy as np
import os

wavelengths = np.array(
    [
        "410",  # AS72653(A) - Ultraviolet
        "435",  # AS72653(B) - Violet
        "460",  # AS72653(C) - Blue
        "485",  # AS72653(D) - Cyan
        "510",  # AS72653(E) - Green
        "535",  # AS72651(F) - Green
        "560",  # AS72652(G) - Yellow Green
        "585",  # AS72652(H) - Yellow
        "610",  # AS72651(R) - Orange
        "645",  # AS72652(I) - Red
        "680",  # AS72651(S) - Red
        "705",  # AS72652(J) - Near Infrared (NIR)
        "730",  # AS72651(T) - Near Infrared (NIR)
        "760",  # AS72651(U) - Near Infrared (NIR)
        "810",  # AS72651(V) - Infrared (IR-A)
        "860",  # AS72651(W) - Infrared (IR-A)
        "900",  # AS72652(K) - Infrared (IR-A)
        "940",  # AS72652(L) - Infrared (IR-A)
    ]
)


def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        r = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        g = 0.0
        b = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        r = 0.0
        g = ((wavelength - 440) / (490 - 440)) ** gamma
        b = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        r = 0.0
        g = 1.0
        b = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        r = ((wavelength - 510) / (580 - 510)) ** gamma
        g = 1.0
        b = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        r = 1.0
        g = (-(wavelength - 645) / (645 - 580)) ** gamma
        b = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        r = (1.0 * attenuation) ** gamma
        g = 0.0
        b = 0.0
    else:
        r = 0.0
        g = 0.0
        b = 0.0
    return (r, g, b)


def plot(ax, sample_name):
    # Open sample data file
    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, sample_name + ".csv")
    levels = np.genfromtxt(file_path, delimiter=",")

    # Convert wavelengths to RGB colors
    colors = []
    for wavelength in wavelengths:
        r, g, b = wavelength_to_rgb(wavelength)
        colors.append((r, g, b))

    ax.set_xlabel("Wavelength (mm)")
    ax.set_title(f"Spectrophotometry ({sample_name})")
    ax.set_ylabel("Reflectance Level")

    ax.set_ylim((0, 15000))

    ax.bar(wavelengths, levels, color=colors)

    # Save image of bar chart
    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, sample_name + ".png")
    ax.figure.savefig(file_path)


def main():
    # sample_name = "Acrylic"
    # sample_name = "Aerogel"
    # sample_name = "Aluminum"
    # sample_name = "Brass"
    # sample_name = "Copper"
    # sample_name = "Felt Black"
    # sample_name = "Lego Blue"
    # sample_name = "Lego Red"
    # sample_name = "Lego White"
    # sample_name = "Maple"
    # sample_name = "Mirror"
    # sample_name = "Nylon"
    # sample_name = "Pine"
    sample_name = "Unknown"

    fig = plt.figure()
    fig.set_size_inches(11.5, 8)
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])

    plot(ax, sample_name)

    fig.canvas.manager.set_window_title("Master Teacher PLT")
    plt.show()


if __name__ == "__main__":
    main()
