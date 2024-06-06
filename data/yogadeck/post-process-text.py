import os
import re

def remove_trailing_period(line):
    """Remove trailing period if the line starts with ( and ends with ) before the final period."""
    pattern = r'^\(.*\)\.$'
    if re.match(pattern, line.strip()):
        return line.strip()[:-1]
    return line.strip()

def process_file(filepath):
    """Process a file to remove the trailing period from specific lines."""
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    cleaned_lines = [remove_trailing_period(line) for line in lines]
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write("\n".join(cleaned_lines) + "\n")
    
    print(f"Processed file: {filepath}")

def process_directory(directory):
    """Process all text files in the specified directory to remove trailing periods."""
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            process_file(filepath)

# Replace '/path/to/your/directory' with the actual directory path containing your .txt files
process_directory('texts/')