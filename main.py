import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)  # Google Web Speech API
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Sorry, I did not catch that. Could you repeat?")
        return None

# Main function
def main():
    speak("Hello, I am AQUA, your personal assistant.")
    while True:
        query = listen()
        if query:
            if 'hello' in query.lower():
                speak("Hello! How can I assist you today?")
            elif 'exit' in query.lower():
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()