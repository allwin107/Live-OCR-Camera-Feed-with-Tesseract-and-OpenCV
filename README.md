
# OCR Camera Feed

This project captures frames from your default camera, performs Optical Character Recognition (OCR) on the captured frames using Tesseract, and displays the extracted text. The extracted text is also saved to a text file.

## Prerequisites

1. Python 3.x
2. OpenCV
3. Tesseract-OCR
4. pytesseract

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/ocr-camera-feed.git
    cd ocr-camera-feed
    ```

2. **Install the Required Python Packages**

    ```bash
    pip install opencv-python pytesseract
    ```

3. **Install Tesseract-OCR**

    - Download and install Tesseract-OCR from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
    - Note the installation path of Tesseract (e.g., `C:/Program Files/Tesseract-OCR/tesseract.exe`).

## Usage

1. **Set the Path to Tesseract Executable**

    Update the `tesseract_cmd` path in the script to point to your Tesseract-OCR installation:

    ```python
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    ```

2. **Run the Script**

    ```bash
    python main.py
    ```

    The script will:

    - Initialize the default camera.
    - Capture frames from the camera.
    - Convert the frames to grayscale (optional).
    - Perform OCR on the frames.
    - Display the captured frames.
    - Print the extracted text to the console.
    - Save the extracted text to `out1.txt`.

3. **Exit the Script**

    Press `q` to exit the camera feed and terminate the script.


## Contributing

Feel free to open issues or submit pull requests with improvements and bug fixes. All contributions are welcome!

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
```
