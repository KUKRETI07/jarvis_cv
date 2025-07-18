
             # NOTE: COMMENTED PART ARE THE PREVIOUS CODES THAT I USED PREVIOUSLY 


# def process_command(command):
#     command = command.lower()  
#     if "hey jarvis" in command:
#         return "Hello boss, how can I help you?"
#     elif "who are you jarvis " in command:
#         return "I am your personal assistant, Mini Jarvis."
#     elif "what can you do" in command:
#         return "Right now, I can listen and talk. Soon I will see and think too!"
#     elif "exit" in command or "bye" in command:
#         return "Goodbye boss, have a great day."
#     else:
#         return "Sorry boss, I didn’t get that yet."
    

# # utils/nlp.py
# import datetime
# import random

# # Basic memory - temporary (can be upgraded later)
# context_memory = []

# def process_command(command):
#     command = command.lower().strip()
#     context_memory.append(command)

#     # Basic understanding logic
#     if "your name" in command:
#         return "I am Jarvis, your personal AI assistant."

#     elif "time" in command:
#         now = datetime.datetime.now().strftime("%I:%M %p")
#         return f"The current time is {now}."

#     elif "date" in command:
#         today = datetime.date.today().strftime("%B %d, %Y")
#         return f"Today's date is {today}."

#     elif "joke" in command:
#         jokes = [
#             "Why did the computer go to therapy? Because it had a hard drive.",
#             "I told my AI friend a joke about UDP... but I'm not sure if it got it.",
#             "I asked the neural network to predict my future. It said: '404 future not found.'"
#         ]
#         return random.choice(jokes)

#     elif "remember" in command:
#         if "what" in command:
#             if context_memory:
#                 return f"You recently said: '{context_memory[-2]}'"
#             else:
#                 return "I don’t have anything in memory yet."
#         else:
#             return "Noted. I'll remember that for now."

#     elif "exit" in command or "shutdown" in command:
#         return "Shutting down Jarvis. Goodbye boss."

#     else:
#         return "I'm still learning. Can you repeat or rephrase that?"

from openai import OpenAI

client = OpenAI(
    api_key="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",  # Replace this
    base_url="https://openrouter.ai/api/v1"
)

def process_command(command):
    response = client.chat.completions.create(
        model="mistralai/mistral-nemo",  
        messages=[
            {"role": "system", "content": "You are sarcastic AI assistant "},
            {"role": "user", "content": command}
        ]
    )
    return response.choices[0].message.content
