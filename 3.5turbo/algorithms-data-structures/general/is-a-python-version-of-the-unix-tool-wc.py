import sys

def word_count(file_content):
    lines = file_content.split("\n")
    word_count = sum(len(line.split()) for line in lines)
    return word_count

def line_count(file_content):
    lines = file_content.split("\n")
    line_count = len(lines)
    return line_count

def character_count(file_content):
    character_count = len(file_content)
    return character_count

# Read the file contents from standard input
file_content = sys.stdin.read()

# Perform word count, line count, and character count
wc_output = {
    "word_count": word_count(file_content),
    "line_count": line_count(file_content),
    "character_count": character_count(file_content)
}

# Print the wc output
print(wc_output)
