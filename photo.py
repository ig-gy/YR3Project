# Name: Igor Andriesii
# Student no.: B00145876
# Description: To take a photo with the use of a camera

import cv2

# Initialize the camera (0 is the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("The camera could not be opened!")
    exit()

# Capture a single frame
ret, frame = cap.read()

# Check if the single frame was captured unsuccessfully
if not ret:
    print("Failed to capture an image!")

# Save the captured image as a file
cv2.imwrite('photo.jpg', frame)

# Release the camera and close all OpenCV windows
cap.release()
#cv2.destroyAllWindows() -- temporary line (breaks code)

print("Image was captured successfully!")
