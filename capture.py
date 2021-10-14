import cv2
from apscheduler.schedulers.blocking import BlockingScheduler
from config import interval


def capture():
    print("Capturing")
    cap = cv2.VideoCapture('rtsp://admin:admin123@192.168.1.150:88/videoMain')

    if cap.isOpened():
        ret,frame = cap.read()
        cap.release()
        if ret and frame is not None:
            cv2.imwrite('images\latest.jpg', frame)


scheduler = BlockingScheduler()
scheduler.add_job(capture, 'interval', minutes=interval)
scheduler.start()