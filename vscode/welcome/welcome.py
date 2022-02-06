#!/usr/bin/env python3
# welcome.py

# Introduction to Scientific Computing
# Courseware developed by Dave Biersach (dbiersach@bnl.gov)

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-2, 2, 500)
    f_top = np.sqrt(1 - (np.abs(x) - 1) ** 2)
    f_bot = np.arccos(1 - np.abs(x)) - np.pi

    ax = plt.gca()
    ax.plot(x, f_top, color="red")
    ax.plot(x, f_bot, color="red")

    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 1.5)

    ax.set_title("Welcome to Scientific Computing!")
    ax.set_aspect("equal")

    plt.show()


if __name__ == "__main__":
    main()
