class ChatBot:
    def __init__(self):
        self.nlp = nlp
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
            "farewell": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
            "default": ["I'm not sure I understand. Can you please rephrase?", "Sorry, I didn't get that."]
        }
        
    def get_response(self, user_input):
        doc = self.nlp(user_input.lower())
        if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
            return self.responses["greeting"]
        elif any(token.lemma_ in ["bye", "goodbye", "see you"] for token in doc):
            return self.responses["farewell"]
        else:
            return self.responses["default"]

    def chat(self):
        print("ChatBot: Hi! How can I help you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("ChatBot: Goodbye! Have a great day!")
                break
            response = self.get_response(user_input)
            print("ChatBot:", response[0])

if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
