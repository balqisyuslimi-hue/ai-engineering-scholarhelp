import ollama

response = ollama.chat(
    model='phi3:mini',
    messages=[
        # This is the system prompt that gives it a personality!
        {'role': 'system', 'content': 'You are PibboPet, a cute, encouraging virtual study pet. You are not an AI, you are a small digital creature. Keep your responses under 3 sentences. Use cute actions in asterisks like *wags tail* or *tilts head*.'},
        
        {'role': 'user', 'content': 'Hello! Are you ready to be my study pet?'}
    ]
)

print(response['message']['content'])