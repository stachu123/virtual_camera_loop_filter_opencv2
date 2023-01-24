import cv2
import numpy as np
import pyvirtualcam
import sys
haar_file = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(haar_file)



class Webcam:
    def __init__(self, IMG_W, IMG_H):
        self.IMG_W = IMG_W
        self.IMG_H = IMG_H

    def set_up_cam(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.IMG_W)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.IMG_H)
        if not cap.isOpened():
            print("Cannot open Camera")
            exit()
        return cap

    def output_virtual_cam(self, cap, filter=None):
        # function takes webcam set up from set_UP_cam(), and name of the filter
        # and outputs filtered video to virtual webcam created with obs
        fmt = pyvirtualcam.PixelFormat.BGR
        frameTime = 20
        with pyvirtualcam.Camera(1280, 720, 20, fmt=fmt) as camera:
            while True:
                ret, im = cap.read()
                hsv_frame = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
                if filter == "yellow":
                    frame = self.yellow_filter(im, hsv_frame)
                if filter == "blue":
                    frame = self.blue_filter(im, hsv_frame)
                if filter == "face_detection":
                    frame = self.face_detection(im,hsv_frame )

                camera.send(frame)

                camera.sleep_until_next_frame()

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

    def output_loop(self, filename):
        frameTime = 20
        fmt = pyvirtualcam.PixelFormat.BGR
        cap = cv2.VideoCapture(filename)
        frameTime = 30
        with pyvirtualcam.Camera(1280, 720, 20, fmt=fmt) as camera:
            while True:

                ret, frameset = cap.read()

                if cap.get(1) > cap.get(7) - 2:  # video loop
                    cap.set(1, 0)  # if frame count > than total frame number, next frame will be zero
                cv2.imshow("G", frameset)
                key = cv2.waitKey(1)
                if cv2.waitKey(frameTime) & 0xFF == ord('q'):
                    break
                camera.send(frameset)
                #
                #         camera.sleep_until_next_frame()
            cap.release()
            cv2.destroyAllWindows()

    # FILTERS

    def yellow_filter(self, frame, hsv_frame):
        # Function to creat mask for yellow color on video and outputs modified frame
        self.low_yellow = np.array([17, 186, 17])
        self.high_yellow = np.array([40, 255, 255])
        alpha = 0.8
        self.yellow_mask = cv2.inRange(hsv_frame, self.low_yellow, self.high_yellow)
        self.yellow = cv2.bitwise_and(frame, frame, mask=self.yellow_mask)
        if sum(sum(self.yellow_mask)) > 25000:
            return cv2.addWeighted(self.yellow, alpha, frame, 1 - alpha, 0)

        else:
            return frame

    def blue_filter(self, frame, hsv_frame):
        self.low_blue = np.array([95, 105, 120])
        self.high_blue = np.array([135, 255, 255])
        alpha = 0.8
        self.blue_mask = cv2.inRange(hsv_frame, self.low_blue, self.high_blue)
        self.blue = cv2.bitwise_and(frame, frame, mask=self.blue_mask)
        if self.blue_mask.any:
            return cv2.addWeighted(self.blue, alpha, frame, 1 - alpha, 0)

        else:
            return frame

    def capture_loop(self, cap):
        # Function to show and record video from a webcam and save it in project folder as output.mp4
        fps = cap.get(cv2.CAP_PROP_FPS)

        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4)
                           )
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))

        # loop runs if capturing has been initialized.
        while (True):
            # reads frames from a camera
            # ret checks return at each frame
            ret, frame = cap.read()

            # output the frame
            out.write(frame)

            # The original input frame is shown in the window
            cv2.imshow('Original', frame)

            # Wait for 'a' key to stop the program
            if cv2.waitKey(1) & 0xFF == ord('a'):
                break

        # Close the window / Release webcam
        cap.release()
        cv2.destroyAllWindows()

    def face_detection(self, frame, hsv_frame):
        # Function to creat mask for yellow color on video and outputs modified frame


        faces = faceCascade.detectMultiScale(
            hsv_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame