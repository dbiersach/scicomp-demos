#!/usr/bin/env python3
# plot_decay_rods.py


import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def fit_linear(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    model = LinearRegression().fit(vec_x, vec_y)
    m = model.coef_
    b = model.intercept_
    score = model.score(vec_x, vec_y)
    return m, b, score


def fit_quadratic(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(vec_x)
    vec_x2 = transformer.transform(vec_x)
    model = LinearRegression().fit(vec_x2, vec_y)
    b, a = model.coef_
    c = model.intercept_
    score = model.score(vec_x2, vec_y)
    return a, b, c, score


def plot(ax, file_path, file_name):
    vec_y = np.genfromtxt(f"{file_path}", delimiter=",")
    vec_x = np.arange(1, vec_y.size + 1)

    x = np.linspace(np.min(vec_x), np.max(vec_x), 500)

    m, b, score = fit_linear(vec_x, vec_y)
    ax.plot(
        x, m * x + b, color="green", linestyle="--", label=f"Linear ($R^2$={score:.4f})"
    )

    a, b, c, score = fit_quadratic(vec_x, vec_y)
    ax.plot(
        x, a * x**2 + b * x + c, color="blue", label=f"Quadratic ($R^2$={score:.4f})"
    )

    ax.scatter(vec_x, vec_y, color="red")

    ax.set_title(f"Decay Events Per Rod ({file_name})")
    ax.set_xlabel("Number of Rods")
    ax.set_ylabel("Number of Events")
    ax.legend()

    ax.set_xlim(0, np.max(vec_x) + 1)
    ax.set_ylim(0)

    ax.xaxis.set_major_locator(MultipleLocator(1))

    ax.figure.savefig(f"Decay Events Per Rod.png")
    ax.figure.savefig(f"Decay Events Per Rod.pdf", dpi=600, orientation="landscape")


def main():
    file_name = "counts.csv"

    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, file_name)

    fig = plt.figure()
    fig.set_size_inches(11.5, 8)
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax, file_path, file_name)
    fig.canvas.manager.set_window_title("SciComp Demonstrations")
    plt.show()


if __name__ == "__main__":
    main()
