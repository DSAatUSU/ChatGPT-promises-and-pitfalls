import collections

def find_statistically_significant_strings(string_list):
    # Count the occurrence of each string
    string_count = collections.Counter(string_list)
    
    # Calculate the total number of strings
    total_strings = len(string_list)
    
    # Calculate the occurrence probability of each string
    string_prob = {s: count / total_strings for s, count in string_count.items()}
    
    # Calculate the expected probability of each string assuming equal distribution
    expected_prob = 1 / len(string_count)
    
    # Calculate the chi-squared value for each string
    chi_squared = {s: ((prob - expected_prob) ** 2) / expected_prob for s, prob in string_prob.items()}
    
    # Set the significance level (adjust as needed)
    significance_level = 0.05
    
    # Determine the statistically significant strings
    significant_strings = [s for s, chi in chi_squared.items() if chi > significance_level]
    
    return significant_strings

# Example usage
if __name__ == '__main__':
    string_list = ["apple", "banana", "apple", "cherry", "banana", "banana"]
    significant_strings = find_statistically_significant_strings(string_list)
    print("Statistically significant strings:", significant_strings)
