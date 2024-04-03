import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Say the desired text
# engine.say("Python is a great programming language")

# Play the speech
engine.runAndWait()

# Get the current speaking rate
rate = engine.getProperty('rate')
print("Current voice rate:", rate)

# Set a new voice rate (e.g., 125)
engine.setProperty('rate', 125)

# Get the current volume level (between 0 and 1)
volume = engine.getProperty('volume')
print("Current volume level:", volume)

# Set a new volume level (e.g., 1.0)
engine.setProperty('volume', 1.0)

# Change the voice (you can choose from available voices)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Say something with the updated settings
engine.say("Hello World!")
engine.say(f"My current speaking rate is {rate}")

# Save the speech to a file (Linux only)
engine.save_to_file("Hello World", "test.mp3")
engine.runAndWait()
