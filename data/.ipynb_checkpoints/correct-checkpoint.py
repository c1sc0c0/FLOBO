#!/usr/bin/python
from openai import OpenAI




def ask_gpt4(question, api_key):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )
    
    try:
        # Make a request to the OpenAI API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-3.5-turbo",
        )

        # Extract the response text
        answer = chat_completion.choices[0].message['content'].strip()
        return answer
    
    except Exception as e:
        return f"An error occurred: {e}"



# Replace 'your-api-key' with your actual OpenAI API key
api_key = 'sk-proj-u9dSWEygaB6eQLxynLcDT3BlbkFJefG3lLk8YIMfQvNk8S7W'
question = "What is the capital of France?"

# Get the answer from GPT-4
answer = ask_gpt4(question, api_key)

# Print the answer
print(f"Question: {question}")
print(f"Answer: {answer}")


