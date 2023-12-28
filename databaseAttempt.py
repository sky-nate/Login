class CodingLanguageBot:
    def __init__(self):
        self.languages = {
            "python": {
                "description": "Python is a high-level, interpreted programming language known for its readability and versatility.",
                "usage": "Python is widely used in web development, data analysis, artificial intelligence, and more.",
                "year": 1991
            },
            "java": {
                "description": "Java is a general-purpose, class-based, object-oriented programming language.",
                "usage": "Java is used in a wide range of applications, from web development to mobile app development.",
                "year": 1995
            },
            "javascript": {
                "description": "JavaScript is a high-level, interpreted programming language primarily used for web development.",
                "usage": "JavaScript is essential for front-end web development and increasingly used on the server side.",
                "year": 1995
            },
            # add c++, c, c#, ruby, r, rust, php, go, html, css, sql, typescript
        }

    def get_language_info(self, language):
        language = language.lower()
        if language in self.languages:
            return self.languages[language]
        else:
            return None

    def start_chat(self):
        print("Hello! I'm the Coding Language Bot. Ask me about programming languages or type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye! Have a great day.")
                break
            language_info = self.get_language_info(user_input)
            if language_info:
                print(f"{user_input.capitalize()}:")
                print(f"Description: {language_info['description']}")
                print(f"Usage: {language_info['usage']}")
                print(f"First appeared: {language_info['year']}")
            else:
                print("I'm sorry, I don't have information about that programming language.")

if __name__ == "__main__":
    bot = CodingLanguageBot()
    bot.start_chat()
