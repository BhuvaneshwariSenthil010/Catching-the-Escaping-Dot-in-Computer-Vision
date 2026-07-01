import cv2
import numpy as np
import random
import time

score = 0
dot_x = random.randint(50, 550)
dot_y = random.randint(50, 450)
radius = 20
start_time = time.time()

def mouse_click(event, x, y, flags, param):
    global dot_x, dot_y, score

    if event == cv2.EVENT_LBUTTONDOWN:
        distance = ((x - dot_x)**2 + (y - dot_y)**2)**0.5

        if distance <= radius:
            score += 1
            dot_x = random.randint(50, 550)
            dot_y = random.randint(50, 450)

cv2.namedWindow("Catch The Dot")
cv2.setMouseCallback("Catch The Dot", mouse_click)

while True:

    img = np.zeros((500, 600, 3), dtype=np.uint8)

    # Move dot every 2 seconds
    if time.time() - start_time > 1:
        dot_x = random.randint(50, 550)
        dot_y = random.randint(50, 450)
        start_time = time.time()

    cv2.circle(img, (dot_x, dot_y), radius, (0, 255, 255), -1)

    cv2.putText(img,
                f"Score: {score}",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2)

    cv2.putText(img,
                "Click the dot!",
                (200, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2)

    cv2.imshow("Catch The Dot", img)

    key = cv2.waitKey(30)

    if key == ord('q'):
        break

cv2.destroyAllWindows()

