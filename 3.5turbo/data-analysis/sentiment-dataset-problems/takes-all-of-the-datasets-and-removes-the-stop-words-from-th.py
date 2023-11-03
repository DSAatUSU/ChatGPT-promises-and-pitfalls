import nltk
from nltk.corpus import stopwords
import os

def remove_stopwords(dataset):
    # Download the stopwords corpus if not already present
    nltk.download('stopwords')

    # Get the list of stopwords
    stop_words = set(stopwords.words('english'))

    # Remove stopwords from each word in the dataset
    words = [word for word in dataset if word.lower() not in stop_words]

    return words

def read_dataset(dataset_path):
    # Read the dataset file
    with open(dataset_path, 'r') as file:
        dataset = file.read().split()

    return dataset

def write_words_to_file(words):
    # Create a new file to write the words
    with open('output.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')

if __name__ == '__main__':
    dataset_path = 'dataset.txt'  # Update this with the path to your dataset file
    
    # Check if dataset file exists
    if not os.path.isfile(dataset_path):
        raise ValueError(f'Dataset file does not exist at {dataset_path}')

    # Read the dataset file
    dataset = read_dataset(dataset_path)

    # Remove stopwords from the dataset
    filtered_words = remove_stopwords(dataset)

    # Write the filtered words to a file
    write_words_to_file(filtered_words)