import pandas as pd
import matplotlib.pyplot as plt

def plot_ids_from_csv(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Sort the DataFrame by the timestamp column
    df.sort_values(by='timestamp', inplace=True)
    
    # Extract the id column as a list
    ids = df['id'].tolist()
    
    # Create x-coordinates for the plot
    x = range(1, len(ids) + 1)
    
    # Plot the ids on a line
    plt.plot(x, ids)
    
    # Customize the plot
    plt.xlabel('Order of Occurrence')
    plt.ylabel('ID')
    plt.title('IDs on a Line')
    
    # Display the plot
    plt.show()

# Provide the path to your CSV file
csv_file = 'dataTimestamp.csv'

# Call the function to plot the ids from the CSV file
plot_ids_from_csv(csv_file)
