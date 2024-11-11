# Speech-to-Text Image Reader 📸🗣️

## Overview
This project is a **Python-based speech recognition and image text reader** that utilizes various libraries to create an interactive voice-controlled application. The program listens for a specific voice command, takes a picture using your webcam, extracts text from the captured image using Optical Character Recognition (OCR), and reads the text aloud using a Text-to-Speech (TTS) engine.

Developed by: **Younes Ameziane**  
Date: **November 2024**

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

---

## Features
- **Voice Command Activation**: Listens for the command **"system what I am looking at"** to trigger a screenshot.
- **Webcam Integration**: Captures an image from the webcam.
- **OCR (Optical Character Recognition)**: Extracts text from the captured image using `easyocr`.
- **Text-to-Speech (TTS)**: Converts the extracted text to speech using `pyttsx3`.
- **Error Handling**: Handles various exceptions for a smooth user experience.

---

## Requirements
Before running this project, ensure you have the following packages installed:

- Python 3.8+
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [EasyOCR](https://pypi.org/project/easyocr/)
- [Pyttsx3](https://pypi.org/project/pyttsx3/)

You can install all dependencies using the following command:
```bash
pip install speechrecognition opencv-python easyocr pyttsx3
```
## Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/speech-to-text-image-reader.git
cd speech-to-text-image-reader
```
## Usage
To run the application, execute the following command in your terminal:
```bash
python main.py
```
## How to Use

1. **Start the program**: It will continuously listen for your voice.
2. **Say the command**: "system what I am looking at" to capture an image.
3. **Wait for OCR processing**: The program will extract text from the captured image.
4. **Listen**: The extracted text will be read out loud using a TTS engine.
5. **Exit**: To exit the listening loop, simply say "exit".

## File structure
```
speech-to-text-image-reader/
├── main.py              # Entry point for the application
├── functions.py         # Contains functions for capturing images and processing text
└── README.md            # Project documentation
```

## How it works
1. ### main.py
- Imports the ```img```
 function from functions.py.
- Listens for voice commands using ```speech_recognition```
.
- If the command "system what I am looking at" is recognized, it triggers the webcam to capture an image.
- Includes exception handling for:

    - Unrecognized speech
    - Errors with the speech recognition service
    - Microphone connection issues

2. ### functions.py
- ```img(IMAGE_PATH)```:
    - Captures an image from the webcam.
    - Waits for the spacebar to be pressed to take a screenshot.
    - Calls the ```app(IMAGE_PATH)``` function to process the captured image.

- ```app(IMAGE_PATH)```:

    - Uses ```easyocr``` to extract text from the given image.
    - Uses ```pyttsx3``` to convert the extracted text to speech.
    - Displays the extracted text in the console.

## Future Improvements
- Add support for multiple languages in OCR.
- Implement a GUI for a more user-friendly experience.
- Save captured images and extracted text for later use.
- Add functionality to read text from a file input.
- Optimize performance for lower-end systems.

## Contributing
Contributions are welcome! If you would like to enhance this project, please follow these steps:

1. Fork the repository.
2. Create a new feature branch: ```git checkout -b feature-name```.
3. Commit your changes: ```git commit -m 'Add new feature'```.
4. Push to the branch: ```git push origin feature-name```.
5. Open a pull request.







