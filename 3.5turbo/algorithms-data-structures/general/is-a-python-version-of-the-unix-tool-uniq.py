import sys

def uniq():
    # read input from user
    lines = sys.stdin.readlines()
    
    # remove leading and trailing whitespaces from each line
    lines = [line.strip() for line in lines]
    
    # remove consecutive duplicate lines
    unique_lines = []
    for line in lines:
        if unique_lines == [] or line != unique_lines[-1]:
            unique_lines.append(line)
    
    # print the unique lines
    for line in unique_lines:
        print(line)

if __name__ == "__main__":
    uniq()