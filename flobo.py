import sys
import ollama
import clips
import chromadb

def call_ollama(input_text):
    # Call Ollama API using the local Ollama library
    stream = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': input_text,
        }
    ], stream=True)
    
    # Check the structure of the response
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def usage():
    print("Usage: python flobo.py <model>")
    print("<model>: naked | rag | symbol")
    sys.exit(1)
def main():
    if len(sys.argv) < 2:
        usage()
    if sys.argv[1] not in ["naked", "rag", "symbol"]:
        usage()
    print("Flobo running %s model. Type '/exit' to quit." % sys.argv[1])
    while True:
        # Read input from the user
        input_text = input(">>> ")
        
        # Exit if the user types 'exit'
        if input_text.strip().lower() == '/exit':
            print("Exiting.")
            from IPython.display import clear_output
            break
        
        # Call Ollama with the input text
        call_ollama(input_text)
        print()  # Print a newline for better readability

if __name__ == "__main__":
    main()