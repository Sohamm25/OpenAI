import openai
openai.api_key = 'your api key'
def chat(prompt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages= [{'role': 'user', 'content': prompt}]  
    )
    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    while True:
        abc = input("Type prompt:-->")
        if abc.lower() in ['exit', 'break', 'shutdown', 'shut down', 'close']:
            break
        response = chat(abc)
        print("Bot:-->", response)
