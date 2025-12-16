import cv2
import os
import time
from db import add_user

DATASET_DIR = "dataset"
CASCADE_PATH = "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def register_user(name, img_count=50):
    # 1️⃣ Add user to DB
    user_id = add_user(name)

    user_dir = os.path.join(DATASET_DIR)
    os.makedirs(user_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = 0

    print(f"[INFO] Registering user '{name}' with ID {user_id}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            file_name = f"User.{user_id}.{count}.jpg"
            cv2.imwrite(os.path.join(user_dir, file_name), face_img)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Capturing {count}/{img_count}",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)

            time.sleep(0.1)

        cv2.imshow("Register User", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if count >= img_count:
            break

    cap.release()
    cv2.destroyAllWindows()

    print("[INFO] Face registration completed.")
    return user_id

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python register.py <name>")
        exit()

    name = sys.argv[1]
    register_user(name)
