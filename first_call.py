import ollama
question = {"role": "user", "content": "who scored more: Rohit 15 or Gill 8?"} 
messages = [question]
response = ollama.chat(model = 'llama3.2', messages = messages)
print(response["message"]["content"])