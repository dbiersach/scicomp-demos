#!/usr/bin/env python3
# plot_field_voltage.py


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


def fit_quintic(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    transformer = PolynomialFeatures(degree=5, include_bias=False)
    transformer.fit(vec_x)
    vec_x2 = transformer.transform(vec_x)
    model = LinearRegression().fit(vec_x2, vec_y)
    e, d, c, b, a = model.coef_
    f = model.intercept_
    score = model.score(vec_x2, vec_y)
    return a, b, c, d, e, f, score


def plot(ax, file_path, file_name):
    data = np.genfromtxt(f"{file_path}", delimiter=",")
    vec_x = data[:, 0] / 256 * 5.0  # Convert to volts
    vec_y = data[:, 1]

    x = np.linspace(0, 5, 500)

    m, b, score = fit_linear(vec_x, vec_y)
    ax.plot(
        x,
        m * x + b,
        color="green",
        linewidth=2,
        linestyle="--",
        label=f"Linear ($R^2$={score:.4f})",
    )

    a, b, c, d, e, f, score = fit_quintic(vec_x, vec_y)
    ax.plot(
        x,
        a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f,
        color="blue",
        linewidth=2,
        label=f"Quintic ($R^2$={score:.4f})",
    )

    # Plot rising voltage strengths
    ax.scatter(vec_x, vec_y, color="red", marker=".", label="Rising Volts")
    # Plot falling voltage strengths
    ax.scatter(
        vec_x[256:], vec_y[256:], color="purple", marker=".", label="Falling Volts"
    )

    ax.set_title(f"Magnetic Field Strength vs. Voltage")
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Field Strength (uT)")
    ax.legend()

    ax.xaxis.set_minor_locator(MultipleLocator(2))

    ax.figure.savefig(f"field_vs_voltage.png")
    ax.figure.savefig(f"field_vs_voltage.pdf", dpi=600, orientation="landscape")


def main():
    file_name = "strength.csv"

    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, file_name)

    fig = plt.figure()
    fig.set_size_inches(11, 8.5)
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax, file_path, file_name)
    fig.canvas.manager.set_window_title("SciComp Demonstrations")
    plt.show()


if __name__ == "__main__":
    main()
