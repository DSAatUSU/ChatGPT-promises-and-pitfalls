import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import glob, os


def display_stl_file(STL_PATH):
    # Using an existing stl file:
    if STL_PATH[-4:] == ".stl":
        your_mesh = mesh.Mesh.from_file(STL_PATH)
    else:
        raise Exception("File is not an STL")

    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
    # Auto scale to the mesh size
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.show()


if __name__ == "__main__":
    print("Current Working Directory: ", os.getcwd())
    STL_PATH = str(input("Enter the path to the STL: "))
    STL_PATH = glob.glob(STL_PATH)[0]
    print("Found STL: ", STL_PATH)
    display_stl_file(STL_PATH)
    print("Done!")
