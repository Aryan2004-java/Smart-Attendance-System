import cv2
import os
import sys


if len(sys.argv) < 2:
    print("Usage: python capture_faces.py <id>")
    sys.exit(1)

user_id = sys.argv[1]

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

dataset_path = "dataset"
os.makedirs(dataset_path, exist_ok=True)

count = 0
max_samples = 50

print("[INFO] Starting face capture...")

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
        cv2.imwrite(os.path.join(dataset_path, file_name), face_img)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
        cv2.putText(frame, f"Image {count}/{max_samples}",
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2)

    cv2.imshow("Capturing Faces", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if count >= max_samples:
        break

cap.release()
cv2.destroyAllWindows()
print("[INFO] Face capture completed.")

