import pyttsx3

# Initialise friend
friend = pyttsx3.init()

# Input text to speak
speak = input("Say Something: ")

# Convert to speech
friend.say(speak)
friend.runAndWait()

