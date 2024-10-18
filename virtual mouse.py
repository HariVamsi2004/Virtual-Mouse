import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

while True:
    # Read frame from webcam
    success, frame = cap.read()
    if not success:
        break

    # Flip frame horizontally for a natural interaction
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:  # Index finger tip
                    cv2.circle(frame, (x, y), 15, (255, 255, 255), cv2.FILLED)
                    index_x = int(screen_width / frame_width * x)
                    index_y = int(screen_height / frame_height * y)
                    pyautogui.moveTo(index_x, index_y)

                if id == 4:  # Thumb tip
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), cv2.FILLED)
                    thumb_x = int(screen_width / frame_width * x)
                    thumb_y = int(screen_height / frame_height * y)
                    if abs(index_y - thumb_y) < 80:
                        pyautogui.click()

                if id == 20:  # Pinky tip
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), cv2.FILLED)
                    pinky_x = int(screen_width / frame_width * x)
                    pinky_y = int(screen_height / frame_height * y)
                    if abs(index_y - pinky_y) < 80:
                        pyautogui.rightClick()

    # Display the frame with landmarks
    cv2.imshow('Virtual Mouse', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    """_summary_
    """# Release the capture and close the windowHow can Technology careers be more inclusive of underrepresented people?

