import cv2
import numpy as np
import requests

def stream_video():
    url = 'http://192.168.8.234/stream'  # Replace with your ESP32 IP
    stream = requests.get(url, stream=True, timeout=10)  # 10-second timeout

    if stream.status_code != 200:
        print("Failed to connect to ESP32 stream.")
        return

    bytes_data = bytes()
    for chunk in stream.iter_content(chunk_size=1024):
        bytes_data += chunk
        a = bytes_data.find(b'\xff\xd8')  # Start of JPEG
        b = bytes_data.find(b'\xff\xd9')  # End of JPEG

        if a != -1 and b != -1:
            jpg = bytes_data[a:b+2]
            bytes_data = bytes_data[b+2:]

            try:
                img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                if img is not None:
                    cv2.imshow("ESP32 Stream", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    print("Empty frame received, skipping...")
            except cv2.error as e:
                print(f"OpenCV error: {e}")
                continue

    cv2.destroyAllWindows()

stream_video()
