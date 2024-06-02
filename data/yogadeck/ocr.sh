#!/bin/zsh

# Directory containing the image files
INPUT_DIR="./data/scans"
# Directory to save the OCR results
OUTPUT_DIR="./data/texts"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all image files in the input directory
for image in "$INPUT_DIR"/*.HEIC; do
  echo "Processing $image"
  # Get the base name of the image file
  base_name=$(basename "$image")
  # Remove the file extension from the base name
  base_name="${base_name%.*}"
  # Define the output text file name
  output_file="$base_name"
  
  # Run tesseract OCR on the image file
  magick "$image" "$INPUT_DIR/$base_name.png"
  magick "$INPUT_DIR/$base_name.png" -colorspace Gray "$INPUT_DIR/$base_name.png"
  magick "$INPUT_DIR/$base_name.png" -threshold "50%" "$INPUT_DIR/$base_name.png"
  magick "$INPUT_DIR/$base_name.png" -negate "$INPUT_DIR/$base_name.png"

  # tesseract "$image" "$output_file"
  # tesseract "$INPUT_DIR/$base_name.png" "$OUTPUT_DIR/$output_file" -l eng
  ./data/correct.swift "$INPUT_DIR/$base_name.png" > "$OUTPUT_DIR/$output_file.txt"
done