from ultralytics import YOLO
import cv2
import cvzone
import math
import time
from gps_test import read_gps_data
import json
import base64
import requests
from picamera2 import Picamera2


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
            def send_to_ground_control(image_path, conf):
                # Check if confidence level is higher than 0.5
                if conf > 0.5:
                    # Convert image to base64
                    with open(image_path, "rb") as image_file:
                        image_data = base64.b64encode(image_file.read()).decode('utf-8')
                    msg= read_gps_data()
                    # Prepare data in JSON format
                    data = {
                        "image": image_data,
                        "latitude": msg.latitude,
                        "longitude": msg.longitude
                    }
                    json_data = json.dumps(data)

                    # Send JSON data to ground control station via HTTP POST request
                    url = "http://127.0.0.1:5000/api/v1/newpothole"  # Replace with actual endpoint
                    headers = {"Content-Type": "application/json"}
                    response = requests.post(url, data=json_data, headers=headers)

                    # Check if request was successful
                    if response.status_code == 200:
                        print("Pothole detection data sent successfully")
                    else:
                        print("Error sending pothole detection data:", response.text)




                send_to_ground_control(image_path, conf)



    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
