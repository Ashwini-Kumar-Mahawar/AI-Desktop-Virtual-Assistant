import pyttsx3

def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty("rate", 150)  # Speed of speech
    engine.setProperty("volume", 1.0)  # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()  # Wait for the speech to finish
