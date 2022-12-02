import cv2
import pyautogui as mouse

# Capture video from the webcam
cap = cv2.VideoCapture(0)
prev_x = 0
prev_y = 0

# Set the width and height of the capture
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Run the video capture loop
while True:
    # Read the current frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use OpenCV's eye detection algorithm to detect the position of the eye
    hands = cv2.CascadeClassifier('hand.xml').detectMultiScale(gray)

    # Loop through the detected hands
    for (x, y, w, h) in hands:
        # Draw a rectangle around the hand
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calculate the movement of the hand
        dx = x - prev_x
        dy = y - prev_y

        # Update the previous position of the hand
        prev_x = x
        prev_y = y

        # Convert the movement of the hand into movement commands for the mouse
        mouse.move(dx, dy)

    # Show the frame in a window
    cv2.imshow('Hand Detection', frame)

    # Check for user input
    key = cv2.waitKey(1)

    # If the user pressed the 'q' key, stop the loop
    if key == ord('q'):
        break

# Release the webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()
