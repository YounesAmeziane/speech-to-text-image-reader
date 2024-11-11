import pyttsx3
import easyocr
import time
import cv2

#function to read the text


def app(IMAGE_PATH):
    reader = easyocr.Reader(['en'], gpu = True)
    result = reader.readtext(IMAGE_PATH)

    #
    extracted_text = [item[1] for item in result]

    # If you want to join all the text into a single string
    extracted_text_combined = ','.join(extracted_text)
    final = f"The text in the picture reads: {extracted_text_combined}"

    # Print the results
    print(extracted_text)
    print(extracted_text_combined)


    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed percent (can go between 0 and 200)
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Get available voices and set one (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female

    # Convert text to speech
    start_time = time.time()
    engine.say(final)
    engine.runAndWait()
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Time taken to read the text: {elapsed_time:.2f} seconds")






#function to take image

def img(IMAGE_PATH):
    
    # Initialize the webcam
    cam = cv2.VideoCapture(0)

    # Create a window for displaying the video feed
    cv2.namedWindow("python webcam screenshot app")

    while True:
        # Capture a frame
        ret, frame = cam.read()
        if not ret:
            print('Failed to grab frame')
            break

        # Display the frame in the window
        cv2.imshow("python webcam screenshot app", frame)

        # Wait for a key press
        k = cv2.waitKey(1)

        # Escape key to close the app
        if k % 256 == 27:
            print("Escape hit, closing the app")
            break
        # Space key to take a screenshot
        elif k % 256 == 32:
            img_name = "img.png"  # Store the image as img.png
            cv2.imwrite(img_name, frame)  # Save the screenshot
            print(f"Screenshot taken: {img_name}")
            app(IMAGE_PATH)
            break  # Break the loop after taking the screenshot

    # Release the webcam and close any OpenCV windows
    cam.release()
    cv2.destroyAllWindows()