import cv2
import sqlite3
from datetime import datetime

# ---------- DB ----------
DB_PATH = "database/attendance.db"

def get_user_name(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM users WHERE id=? AND active=1", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else "Unknown"

def mark_attendance(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO attendance (user_id, timestamp) VALUES (?, ?)",
        (user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()


# ---------- Face & Model ----------
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("models/trainer.yml")

cap = cv2.VideoCapture(0)

marked_today = set()

print("[INFO] Starting attendance system... Press Q to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        user_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 70:
            name = get_user_name(user_id)

            if user_id not in marked_today and name != "Unknown":
                mark_attendance(user_id)
                marked_today.add(user_id)

            label = f"{name} ({round(100 - confidence, 1)}%)"
            color = (0, 255, 0)
        else:
            label = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
