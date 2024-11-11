import speech_recognition as sr
from functions import img

recognizer = sr.Recognizer()

IMAGE_PATH = "img.png"

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=.2)
            audio = recognizer.listen(mic)  # Listen to the microphone input

            text = recognizer.recognize_google(audio)  # Use recognize_google to transcribe audio
            text = text.lower()

            print(f"Recognized: {text}")

            # Check if the recognized text is "hello system"
            if "system what i am looking at" in text:
                print("Taking a picture...")
                img(IMAGE_PATH)
                break  # Exit the loop to stop listening

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        continue
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        break