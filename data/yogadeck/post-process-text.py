import os
import re

def remove_fig_mentions(directory):
    """Remove all mentions of (fig. n): from the contents of files in the specified directory."""
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            full_path = os.path.join(directory, filename)
            with open(full_path, 'r') as file:
                content = file.read()

            # Remove all instances of (fig. n):
            modified_content = re.sub(r'\(fig\. \d+\):', '', content)

            with open(full_path, 'w') as file:
                file.write(modified_content)
            print(f"Processed '{filename}'")

# Replace '/path/to/your/directory' with the actual directory path containing your .txt files
remove_fig_mentions('texts/')