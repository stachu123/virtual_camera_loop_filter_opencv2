import cv2
import pyvirtualcam
import numpy as np
from FIlters_and_webcam import Webcam

IMG_W = 1280
IMG_H = 720

webcam = Webcam(1280, 720)
cap = webcam.set_up_cam()
# webcam.capture_loop(cap)
# webcam.output_loop("output.avi")
webcam.output_virtual_cam(cap, filter='face_detection')

# fmt = pyvirtualcam.PixelFormat.BGR
# with pyvirtualcam.Camera(1280, 720, 20, fmt=fmt) as camera:
#     while True:
#         ret, im = cap.read()z
#         hsv_frame = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
#         frame = webcam.yellow_filter(im, hsv_frame)
#         camera.send(frame)
#
#         camera.sleep_until_next_frame()