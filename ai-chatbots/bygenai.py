from google import genai

apikey = "YOUR_API_KEY_HERE"
client = genai.Client(api_key=apikey)

def completion(user_message):
    
    chat_completion = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message
    )

    reply = chat_completion.text
    print(f"GenieChat: {reply}")

if __name__ == "__main__":
    print("GenieChat: Hi, I am GenieChat. How may I help you?")
    while True:
        user_question = input("User: ")
        completion(user_question)
