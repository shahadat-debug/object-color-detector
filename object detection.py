
import cv2
import numpy as np


# Detect the approximate color of an object
def detect_color(bgr_color):
    blue, green, red = map(int, bgr_color)

    if max(blue, green, red) < 60:
        return "Black"

    if min(blue, green, red) > 190:
        return "White"

    if red > 150 and green > 120 and blue < 100:
        return "Yellow"

    if red > 150 and green < 100 and blue < 100:
        return "Red"

    if green > 100 and red < 120 and blue < 120:
        return "Green"

    if blue > 100 and red < 120 and green < 150:
        return "Blue"

    if red > 130 and blue > 100 and green < 120:
        return "Purple"

    if red > 130 and green > 80 and blue < 100:
        return "Orange"

    return "Unknown / Mixed"


# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam could not be opened.")
    raise SystemExit

print("Object and Color Detector started.")
print("Press Q to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read webcam frame.")
        break

    frame = cv2.resize(frame, (640, 480))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect colored regions
    lower_color = np.array([0, 45, 40])
    upper_color = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Remove small noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_CLOSE, kernel
    )

    # Find object-like colored regions
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        if area < 1500:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        # Sample the center of the region
        center_x = x + w // 2
        center_y = y + h // 2

        sample = frame[
            max(0, center_y - 5):center_y + 5,
            max(0, center_x - 5):center_x + 5
        ]

        if sample.size == 0:
            continue

        median_color = np.median(
            sample.reshape(-1, 3), axis=0
        ).astype(int)

        color_name = detect_color(median_color)

        # Draw green rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Display color name
        label = "Color: " + color_name

        cv2.putText(
            frame,
            label,
            (x, max(25, y - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0, 255, 0),
            2
        )

        # Mark the center
        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (0, 0, 255),
            -1
        )

    # Display ONLY the webcam window
    cv2.imshow("Object and Color Detector", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Detector stopped.")
