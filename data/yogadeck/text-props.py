import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data files
nltk.download('punkt')

def summarize_file_properties(filepath):
    """Summarize the properties of a text file."""
    with open(filepath, 'r') as file:
        content = file.read()
        
        # Calculate number of lines
        lines = content.splitlines()
        num_lines = len(lines)
        
        # Tokenize words and sentences
        words = word_tokenize(content)
        sentences = sent_tokenize(content)
        
        # Number of words
        num_words = len(words)
        
        # Number of sentences
        num_sentences = len(sentences)
        
        # Number of tokens (in LLM context, consider word tokens)
        num_tokens = len(words)
        
        # Display summary
        print(f"File: {filepath}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of sentences: {num_sentences}")
        print(f"Number of tokens: {num_tokens}")
        print("\n")
        
        return num_lines, num_words, num_sentences, num_tokens
        
def summarize_directory(directory):
    """Summarize properties of all text files in the specified directory and provide totals."""
    total_lines = 0
    total_words = 0
    total_sentences = 0
    total_tokens = 0
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            num_lines, num_words, num_sentences, num_tokens = summarize_file_properties(filepath)
            total_lines += num_lines
            total_words += num_words
            total_sentences += num_sentences
            total_tokens += num_tokens
    
    # Print total summary
    print("Total Summary for all files:")
    print(f"Total number of lines: {total_lines}")
    print(f"Total number of words: {total_words}")
    print(f"Total number of sentences: {total_sentences}")
    print(f"Total number of tokens: {total_tokens}")

summarize_directory('texts/')