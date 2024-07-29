import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize hand tracking
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# For smoothing mouse movements
SMOOTHING_FACTOR = 0.1  # Adjust for smoother movement
MOVEMENT_SCALE = 10  # Increase to cover more of the screen
prev_x, prev_y = pyautogui.position()  # Initialize with current mouse position
screen_width, screen_height = pyautogui.size()

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def main():
    global prev_x, prev_y
    cap = cv2.VideoCapture(0)
    click_time = 0
    double_click_threshold = 0.5  # Time in seconds to detect double click

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        # Flip to mirror
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]

                index_tip_coords = (index_tip.x * screen_width, index_tip.y * screen_height)
                thumb_tip_coords = (thumb_tip.x * screen_width, thumb_tip.y * screen_height)
                middle_tip_coords = (middle_tip.x * screen_width, middle_tip.y * screen_height)
                ring_tip_coords = (ring_tip.x * screen_width, ring_tip.y * screen_height)

                # Calculate distances for clicks
                distance_thumb_middle = calculate_distance(thumb_tip_coords, middle_tip_coords)
                distance_thumb_ring = calculate_distance(thumb_tip_coords, ring_tip_coords)
                distance_thumb_index = calculate_distance(thumb_tip_coords, index_tip_coords)

                # Move cursor based on thumb and index finger
                if distance_thumb_index < 50:
                    # Smooth mouse movement with increased scale
                    delta_x = (index_tip_coords[0] - prev_x) * MOVEMENT_SCALE
                    delta_y = (index_tip_coords[1] - prev_y) * MOVEMENT_SCALE
                    new_x = int(prev_x + SMOOTHING_FACTOR * delta_x)
                    new_y = int(prev_y + SMOOTHING_FACTOR * delta_y)

                    # Ensure the new position is within screen bounds
                    new_x = max(0, min(screen_width - 1, new_x))
                    new_y = max(0, min(screen_height - 1, new_y))

                    pyautogui.moveTo(new_x, new_y)
                    prev_x, prev_y = new_x, new_y

                # Left click with thumb and middle finger
                if distance_thumb_middle < 50:
                    current_time = time.time()
                    if current_time - click_time < double_click_threshold:
                        pyautogui.click(button='left')
                    click_time = current_time

                # Right click with thumb and ring finger
                if distance_thumb_ring < 50:
                    current_time = time.time()
                    if current_time - click_time < double_click_threshold:
                        pyautogui.click(button='right')
                    click_time = current_time

        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
