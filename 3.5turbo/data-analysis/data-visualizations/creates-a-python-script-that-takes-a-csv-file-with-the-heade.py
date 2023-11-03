import pandas as pd
import matplotlib.pyplot as plt

def display_histogram(csv_file, headers):
    # Read the csv file into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Select the specified headers from the DataFrame
    selected_columns = df[headers]

    # Create a histogram for each selected column
    selected_columns.hist()

    # Display the histogram
    plt.show()

if __name__ == "__main__":
    # Specify the csv file path
    csv_file = "data.csv"

    # Specify the headers for which the histogram is to be displayed
    headers = ["Monthly Revenue"]

    # Call the function to display the histogram
    display_histogram(csv_file, headers)
