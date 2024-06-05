#!/bin/bash

# Directory to process
DIRECTORY="texts/"

# Iterate over the files in the directory
for FILE in "$DIRECTORY"/*-0.txt; do
    # Check if the file exists (in case there are no matches)
    if [[ -e "$FILE" ]]; then
        # Remove -0 from the filename
        NEW_NAME="${FILE%-0.txt}.txt"
        # Rename the file
        mv "$FILE" "$NEW_NAME"
        echo "Renamed '$FILE' to '$NEW_NAME'"
    fi
done