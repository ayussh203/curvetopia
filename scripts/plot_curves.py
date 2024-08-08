import numpy as np
import matplotlib.pyplot as plt
from read_csv import read_csv

def plot(paths_XYs):
    colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))

    for i, XYs in enumerate(paths_XYs):
        c = colours[i % len(colours)]
        for XY in XYs:
            for segment in XY:
                if len(segment) == 2:
                    ax.plot([segment[0][0], segment[1][0]], [segment[0][1], segment[1][1]], c=c, linewidth=2)
                else:
                    ax.plot(segment[0][0], segment[0][1], c=c, linewidth=2)

    ax.set_aspect('equal')
    plt.show()

if __name__ == "__main__":
    paths = read_csv('../data/examples/isolated.csv')
    plot(paths)
