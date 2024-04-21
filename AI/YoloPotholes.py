import cv2
import cvzone
import math
import time
from picamera2 import Picamera2
from ultralytics import YOLO

# Initialize and configure the Raspberry Pi camera using picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 720)  # Match your resolution settings
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

model = YOLO("/home/Project/yolov8_Project/Yolo-Weights/Pithole (1).pt")
classNames = ["pothole"]

while True:
    img = picam2.capture_array()  # Capture the image from the PiCamera

    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
