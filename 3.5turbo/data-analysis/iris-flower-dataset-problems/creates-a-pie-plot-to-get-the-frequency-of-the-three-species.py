import pandas as pd
import matplotlib.pyplot as plt

def create_pie_plot():
    # Load the Iris dataset
    df = pd.read_csv('iris.csv')

    # Count the frequency of each species
    species_counts = df['species'].value_counts()

    # Create a pie plot
    plt.figure(figsize=(8, 6))
    print("showing pie")
    plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle
    plt.title('Frequency of Species in Iris Dataset')
    plt.show()

if __name__ == '__main__':
    create_pie_plot()
