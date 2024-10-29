import cv2

def stream_from_esp32():
    url = 'http://192.168.8.234:80/stream'  # Replace with the actual IP address and port of your ESP32-CAM
    print("Connecting to ESP32-CAM stream...")

    # Open the video stream with OpenCV
    cap = cv2.VideoCapture(url)
    
    if not cap.isOpened():
        print("Error: Unable to connect to ESP32-CAM.")
        return

    print("Connected to ESP32-CAM stream. Press 'q' to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        
        cv2.imshow("ESP32-CAM Stream", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    print("Stream ended.")

stream_from_esp32()
