def is_palindrome(string):
    # Remove whitespace and convert the string to lowercase
    string = string.replace(" ", "").lower()
    length = len(string)

    # Check if the string is symmetrical
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return False

    return True


if __name__ == "__main__":
    # Get user input
    string = input("Enter a string: ")

    if is_palindrome(string):
        print("The string is a palindrome or symmetrical.")
    else:
        print("The string is not a palindrome or symmetrical.")
