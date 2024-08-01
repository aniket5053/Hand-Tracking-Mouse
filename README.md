# Hand Tracking Mouse Control

## Overview

This project uses Mediapipe for hand tracking and PyAutoGUI for mouse control, allowing users to interact with their computer through hand gestures. The program tracks hand movements to control the mouse cursor, perform left and right-click actions, and handle double clicks based on specific finger gestures.

## Features

- **Cursor Control:** Move the mouse cursor by moving your thumb and index finger.
- **Left Click:** Perform a left-click by touching your thumb and middle finger together.
- **Right Click:** Perform a right-click by touching your thumb and ring finger together.
- **Double Click Detection:** Detects double clicks with a quick double tap of the thumb and middle finger.

## Files

- **`main.py`**: The main script that runs the hand tracking and mouse control functionality. It captures video from the webcam, processes hand landmarks using Mediapipe, and controls the mouse cursor and clicks using PyAutoGUI.

## Usage

1. **Run the Program:**

   Execute the script with Python to start the webcam feed and begin tracking hand movements.

2. **Hand Gestures:**

   - **Move Cursor:** Move your thumb and index finger apart to control the mouse cursor.
   - **Left Click:** Touch your thumb and middle finger together.
   - **Right Click:** Touch your thumb and ring finger together.
   - **Double Click:** Quickly touch your thumb and middle finger together twice.

3. **Exit:**

   - Press `ESC` to exit the program.

## TODO

- **Implement Scroll Wheel:** Allow users to move their hand up or down to allow to scroll easily
- **Improve Gesture Detection:** Enhance the accuracy of gesture recognition to avoid false positives.
- **Add Customization Options:** Allow users to adjust sensitivity settings and configure gestures.
- **Implement Feedback Mechanism:** Provide visual or auditory feedback for clicks and movements.


## Notes

- Ensure that the lighting conditions are suitable for hand tracking.
- Adjust the `SMOOTHING_FACTOR` and `MOVEMENT_SCALE` values in the script for smoother cursor movement and better control.

