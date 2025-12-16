import cv2
import numpy as np
import os
from PIL import Image

DATASET_PATH = "dataset"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "trainer.yml")

os.makedirs(MODEL_DIR, exist_ok=True)

recognizer = cv2.face.LBPHFaceRecognizer_create()

def get_images_and_labels(path):
    face_samples = []
    ids = []

    image_paths = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.lower().endswith(".jpg")
    ]

    for image_path in image_paths:
        # Convert image to grayscale
        img = Image.open(image_path).convert("L")
        img_np = np.array(img, "uint8")

        # Extract ID from filename: User.<id>.<count>.jpg
        try:
            user_id = int(image_path.split(".")[1])
        except ValueError:
            continue  # skip bad files

        face_samples.append(img_np)
        ids.append(user_id)

    return face_samples, ids


print("[INFO] Training model...")

faces, ids = get_images_and_labels(DATASET_PATH)

if len(faces) == 0:
    print("[ERROR] No training data found.")
    exit()

recognizer.train(faces, np.array(ids))
recognizer.save(MODEL_PATH)

print(f"[SUCCESS] Model trained and saved at {MODEL_PATH}")
