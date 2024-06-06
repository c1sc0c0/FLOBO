import sys, os
import ollama
import clips
import chromadb

def concatenate_files(directory):
    """Concatenate contents of all .txt files in the directory."""
    concatenated_text = ""
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                concatenated_text += file.read() + "\n"
    
    return concatenated_text

def create_rag_prompt(question):
    client = chromadb.PersistentClient(path="chromadb")
    collection = client.get_or_create_collection(name="yoga-poses-deck")
    
    results = collection.query(
        query_texts=[question],
        n_results=1,
    )
    context = results["documents"][0][0] # Meh, need to discover filtering more
    
    return f"Given the following context: \n\t{context} \n\nAnswer this question: \n\t{question}"

def create_dump_prompt(question):

    context = concatenate_files("data/yogadeck/texts/")
    return f"Given the following context: \n\t{context} \n\nAnswer this question: \n\t{question}"



def create_symbolic_prompt(question):

    context = "Vajrasana is a pose that people with knee problems should avoid."
    
    return f"Given the following context: \n\t{context} \n\nAnswer this question: \n\t{question}"


def call_ollama(input_text, model):

    if model == "naked":
        stream = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': input_text,
            }
        ], stream=True)
        
    if model == "rag":
        prompt = create_rag_prompt(input_text)
        stream = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': prompt,
            }
        ], stream=True)
    
    if model == "dump":
        prompt = create_dump_prompt(input_text)
        stream = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': prompt,
            }
        ], stream=True)    
    
    if model == "symbol":
        prompt = create_symbolic_prompt(input_text)
        print(prompt)
        stream = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': input_text + " SYMBOL",
            }
        ], stream=True)    
        
    
    
    # Check the structure of the response
    # TODO: print the scoring?
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def usage():
    print("Usage: python flobo.py <model>")
    print("<model>: naked | dump | rag | symbol")
    sys.exit(1)
def main():
    if len(sys.argv) < 2:
        usage()
    if sys.argv[1] not in ["naked", "rag", "symbol", "dump"]:
        usage()
    model = sys.argv[1]
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
        call_ollama(input_text, model)
        print()  # Print a newline for better readability

if __name__ == "__main__":
    main()