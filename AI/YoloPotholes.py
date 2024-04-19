from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import gps_test
import json
import base64
import requests




cap = cv2.VideoCapture(0)  # For Webcam
# cap.set(3, 1280)
# cap.set(4, 720)
# cap = cv2.VideoCapture("C:/Users/hessa/PycharmProjects/yolov8_Project/Videos/Potholevideo.mp4")  # For Video
model = YOLO("C:/Users/hessa/PycharmProjects/yolov8_Project/Yolo-Weights/Pithole.pt")
classNames = ["pothole"]
prev_frame_time = 0
new_frame_time = 0










while True:
    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)


            def send_to_ground_control(image_path, latitude, longitude, conf):
                # Check if confidence level is higher than 0.7
                if conf > 0.7:
                    # Convert image to base64
                    with open(image_path, "rb") as image_file:
                        image_data = base64.b64encode(image_file.read()).decode('utf-8')

                    # Prepare data in JSON format
                    data = {
                        "image_base64": image_data,
                        "latitude": latitude,
                        "longitude": longitude
                    }
                    json_data = json.dumps(data)

                    # Send JSON data to ground control station via HTTP POST request
                    url = "http://example.com/api/pothole_detection"  # Replace with actual endpoint
                    headers = {"Content-Type": "application/json"}
                    response = requests.post(url, data=json_data, headers=headers)

                    # Check if request was successful
                    if response.status_code == 200:
                        print("Pothole detection data sent successfully")
                    else:
                        print("Error sending pothole detection data:", response.text)


            # Example usage
            conf = 0.8  # Confidence level
            image_path = "path/to/pothole_image.jpg"
            latitude = 123.456  # Replace with actual latitude value
            longitude = 789.012  # Replace with actual longitude value

            send_to_ground_control(image_path, latitude, longitude, conf)



    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break




cap.release()
cv2.destroyAllWindows()
