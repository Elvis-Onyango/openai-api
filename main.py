import openai
import os

my_secret = os.environ['openaikey']
openai.api_key = my_secret

def chat_with_ai(user_input):
    api_key = openai.api_key
    conversation = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': user_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        api_key=api_key
    )

    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    while True:
        user_input = input("you: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        else:
            response = chat_with_ai(user_input)
            print("chat bot:", response)
