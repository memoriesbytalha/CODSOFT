import re


def check_greetings(user_ques):
    if re.search(r"hi|hello|hey|salam",user_ques,re.IGNORECASE):
        return "Hello Sir, How may I help you?"


def check_weather_inquiry(user_ques):
    if re.search(r"weather",user_ques,re.IGNORECASE):
        return "Weather is clear Sir!"
    else:
        return None


def bot_response(user_ques):
    user_ques = user_ques.lower()

    greeting_response = check_greetings(user_ques)
    if greeting_response:
        return greeting_response

    weather_response = check_weather_inquiry(user_ques)
    if weather_response:
        return weather_response
    if user_ques == "exit":
        return "Goodbye!"

    return "I'm sorry, I don't understand that?"


while True:
    user_ques = input("You: ")
    chat_response = bot_response(user_ques)
    print(f"Chatbot: {chat_response}")
    if chat_response == "Goodbye!":
        break
