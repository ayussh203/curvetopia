import numpy as np
import matplotlib.pyplot as plt
from read_csv import read_csv
from rasterize_svg import polylines2svg

def regularize_curves(paths_XYs):
    regularized_paths = []
    
    for path in paths_XYs:
        for polyline in path:
            regularized_path = []
            for i in range(len(polyline) - 1):
                point1 = polyline[i]
                point2 = polyline[i + 1]
                
                # Check for straight lines
                if np.allclose(point1[1:], point2[1:], atol=1e-3):
                    regularized_path.append([point1, point2])
                else:
                    # If not a straight line, handle other shapes (circles, ellipses, etc.)
                    # For simplicity, let's just add the points directly for now
                    regularized_path.append([point1])
                    
            regularized_paths.append(regularized_path)
    
    return regularized_paths

def detect_symmetry(paths_XYs):
    # Add your symmetry detection code here
    pass

def complete_curves(paths_XYs):
    # Add your curve completion code here
    pass

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
    regularized_paths = regularize_curves(paths)
    plot(regularized_paths)
    polylines2svg(regularized_paths, '../results/output.svg')
