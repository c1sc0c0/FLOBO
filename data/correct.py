#!/usr/bin/python
import ollama
stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)
