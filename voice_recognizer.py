import speech_recognition as sr

def take_command():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)  # Capture the audio

        try:
            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()  # Return the command in lowercase
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None