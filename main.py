import threading
from modules.voice_recognizer import take_command
from modules.text_to_speech import speak
from modules.web_search import search_web
from modules.file_manager import open_folder
from modules.weather_update import get_weather

def handle_command(command):
    if command:
        if "search" in command:
            # Perform a web search
            search_web(command)
        elif "weather" in command:
            # Fetch weather information
            city = command.replace("weather in", "").strip()
            get_weather(city)
        elif "open" in command and "folder" in command:
            # Open a folder
            folder_name = command.replace("open", "").replace("folder", "").strip()
            open_folder(folder_name)
        elif "exit" in command:
            # Exit the assistant
            speak("Goodbye!")
            print("Goodbye!")
            exit()
        else:
            # Handle unrecognized commands
            speak("Sorry, I don't understand that command.")

def assistant():
    # Greet the user
    speak("Hello! How can I assist you today?")

    while True:
        # Listen for a command
        command = take_command()

        if command:
            # Use multi-threading to handle the command
            thread = threading.Thread(target=handle_command, args=(command,))
            thread.start()

if __name__ == "__main__":
    assistant()
