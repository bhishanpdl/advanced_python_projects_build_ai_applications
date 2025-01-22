from textblob import TextBlob

intent_data = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "We are open from 9 AM to 5PM, Mon-Fri",
    },
    "return": {
        "keywords": ["refund", "money back", "return"],
        "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent.",
    },
}


def get_response(message):
    message = message.lower()
    for intent, data in intent_data.items():
        if any(word in message for word in data["keywords"]):
            return data["response"]

    sentiment = TextBlob(message).sentiment.polarity

    if sentiment > 0:
        return "That's great to hear!"
    elif sentiment < 0:
        return "I'm so sorry to hear that. How can I help?"
    else:
        return "I see. Can you tell me more about that?"


def chat():
    print("Chatbot: Hi, how can I help you today?")
    while True:
        user_message = input("You: ").strip().lower()
        if user_message in ["exit", "quit", "bye"]:
            break
        print(f"\nChatbot: {get_response(user_message)}")

    print("Chatbot: Thank you for chatting. Have a great day!")


if __name__ == "__main__":
    chat()
