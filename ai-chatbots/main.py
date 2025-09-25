from openai import OpenAI



client = OpenAI(api_key= "YOUR_API_KEY_HERE")  

messages = []

def completion(user_message):
    global messages
    messages.append({"role": "user", "content": user_message})

    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=messages
    )

    reply = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"BuddyBot: {reply}")


if __name__ == "__main__":
    print("BuddyBot: Hi, I am BuddyBot. How may I help you?")
    while True:
        user_question = input("User: ")
        completion(user_question)
