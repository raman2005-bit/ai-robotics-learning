import random
from datetime import datetime

# Time-based greeting helper
def get_greeting(hour):
    if hour < 12:
        return "Good morning ☀️"
    elif hour < 16:
        return "Good afternoon 🌤"
    elif hour < 20:
        return "Good evening 🌆"
    else:
        return "Good night 🌙"

# Replies
unknown_replies = [
    "Mujhe ye samajh nahi aaya 🤔",
    "Kya tum ise alag tarike se poochh sakte ho?",
    "Hmm... is baare me mujhe knowledge nahi hai",
    "Interesting... batao aur!",
    "Samajh gaya, lekin thoda detail me batao."
]

hello_keyword = ["helo", "hey", "hi", "hii", "hello"]
happy_keyword = ["happy", "amazing", "peace", "mast"]
sad_keyword = ["sad", "depressed", "lonely", "dukhi"]
angry_keyword = ["mad", "angry", "furious", "gussa"]

# Start chatbot
print("🤖 Hello! Main tumhara AI Chatbot hoon.")
name = input("Tumhara naam kya hai: ").strip().lower()

# Greet user based on time
hour = datetime.now().hour
print(f"{get_greeting(hour)}, {name}! Nice to meet you.")

last_reply = ""  # to avoid repeating same message

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "exit":
        if 20 <= hour or hour < 3:
            print(f"Good night {name}, bye! 🌙")
        else:
            print(f"Alvida {name}, fir milte hain! 👋")
        break

    # Responses
    if any(word in user_input for word in hello_keyword):
        reply = f"Hello {name}! i am your ai chatbot"
    elif "thik hoon" in user_input:
        reply = "Achha hai! Hamesha aise hi khush raho. 😄"
    elif any(word in user_input for word in happy_keyword):
        reply = f"Wah! Tumhara mood to mast lag raha hai {name} 😄"
    elif any(word in user_input for word in sad_keyword):
        reply = f"Fikr mat karo {name}, main tumhare saath hoon. 🙂"
    elif any(word in user_input for word in angry_keyword):
        reply = f"{name}, lambi saans lo 😌 Hum saath me problem solve karenge."
    elif "kaise ho" in user_input:
        reply = "Main theek hoon! Tum sunao?"
    elif "name" in user_input:
        reply = "Mera naam RoboBuddy hai 🤖."
    else:
        # Avoid same unknown reply twice in a row
        while True:
            reply = random.choice(unknown_replies)
            if reply != last_reply:
                break

    print(f"🤖 Chatbot: {reply}")
    last_reply = reply