import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Function to load and display contents of .stl file
def display_stl_file(filename):
    # Load the mesh
    stl_mesh = mesh.Mesh.from_file(filename)

    # Get the vertex coordinates and faces of the mesh
    vertices = stl_mesh.vectors.reshape(-1, 3)
    faces = stl_mesh.vectors.reshape(-1, 3)

    # Plotting the mesh
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure)

    # Add the mesh to the plot
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(vertices[faces], facecolors='black', linewidths=1, edgecolors='r', alpha=0.3))

    # Set plot limits to encompass the whole mesh
    axes.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    # Show the plot
    plt.show()

# Main code
if __name__ == '__main__':
    # Input the path to the .stl file
    filename = input("Enter the path to the .stl file: ")

    # Call the display_stl_file function
    display_stl_file(filename)
