import cv2
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
# Example usage:
filename = "out1.txt"



# Function to perform OCR on an image
def perform_ocr(image):
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    return text

# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 for default camera, you may change it to other values depending on your setup

# Open a text file for writing

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    
    # Convert the frame to grayscale (optional, depending on the image quality)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform OCR on the frame
    text = perform_ocr(gray_frame)
    with open(filename, 'w') as file:
        file.write(text)
    # Print the extracted text
    print("Extracted Text:", text)

    # Write the extracted text to the output file
    
    # Display the captured frame
    cv2.imshow('Camera Feed', frame)
    
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the output file
output_file.close()

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()