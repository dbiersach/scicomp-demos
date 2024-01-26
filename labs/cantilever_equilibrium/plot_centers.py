# plot_centers.py


import matplotlib.pyplot as plt
from blocks import BlockList


def plot_14_pile(ax):
    x_14_pile, y_14_pile = [0.0], [0.0]
    block_list = BlockList()
    for _ in range(1, 8):
        block_list.place_block(7.5, 1.5)
        block_list.place_block(1.5, 10.5)
        x_14_pile.append(block_list.center_x)
        y_14_pile.append(block_list.center_y)
        block_list.move_blocks(3, 3)

    ax.set_title("Center of Mass Per Ensemble (14 block pile)")
    ax.plot(range(8), x_14_pile, label="x-Axis Center of Mass")
    ax.plot(range(8), y_14_pile, label="y-Axis Center of Mass")
    ax.set_xlabel("Number of Ensembles")
    ax.set_ylabel("Location (cm)")
    ax.legend()
    ax.set_xlim(1)


def plot_15_pile(ax):
    x_15_pile, y_15_pile = [0.0], [0.0]
    block_list = BlockList()
    # Add the extra initial block in the first
    # ensemble of a 15-block Jenga pile
    block_list.place_block(10.5, 4.5)
    for _ in range(1, 8):
        block_list.place_block(7.5, 1.5)
        block_list.place_block(1.5, 10.5)
        x_15_pile.append(block_list.center_x)
        y_15_pile.append(block_list.center_y)
        block_list.move_blocks(3, 3)

    ax.set_title("Center of Mass Per Ensemble (15 block pile)")
    ax.plot(range(8), x_15_pile, label="x-Axis Center of Mass")
    ax.plot(range(8), y_15_pile, label="y-Axis Center of Mass")
    ax.set_xlabel("Number of Ensembles")
    ax.set_ylabel("Location (cm)")
    ax.legend()
    ax.set_xlim(1)


def main():
    plt.rcParams["figure.constrained_layout.use"] = True
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.canvas.manager.set_window_title(__file__)
    fig.set_size_inches(12, 6)

    plot_14_pile(ax1)
    plot_15_pile(ax2)

    plt.show()


main()
