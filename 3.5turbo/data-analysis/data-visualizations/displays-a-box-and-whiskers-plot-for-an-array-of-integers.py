import matplotlib.pyplot as plt
import numpy as np

def create_boxplot(data):
    fig, ax = plt.subplots()
    ax.boxplot(data)

    ax.set_xlabel('Data')
    ax.set_ylabel('Values')
    ax.set_title('Box and Whiskers Plot')

    plt.show()

if __name__ == '__main__':
    # Example input: array of integers
    data = np.array([1, 1, 1, 1, 1, 6, 7, 8, 9, 10])

    create_boxplot(data)
