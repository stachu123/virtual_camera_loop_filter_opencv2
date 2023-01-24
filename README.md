# virtual_camera_loop_filter_opencv2
Program outputs modified webcam image to virtual camera created with OBS.

Needed:
 - virtual camera created with OBS
 - Opencv
 - numpy 
 - pyvirtualcam 

Reused code: 
 - face detection code from https://www.geeksforgeeks.org/face-detection-using-python-and-opencv-with-webcam/
   implemented to operated within a program, reused code is in face_detecion function

Operation:
Whole program is based on webcam class.

To operate the program webcam.set_up_cam should be initialazied and assigned to variable, wich sets up the webcam from computer and outputs 
error if none have been found.

Main function in the program is webcam.output_virtual_cam which takes initialized variable with cam,
and also takes filter name ("yellow" - detects yellow color of specified values and makes them more visible on screen,
 "blue" - same as yellow, "face detection" - draws rectangles around detected faces on the image)

To operate loop function you need to record the loop with webcam.capture_loop(takes variable with camera), 
recording starts when window pops up with webcam image, to stop recording press "a"

to output the loop to the virtual camera use webcam.output_loop(takes the video file name), the function outputs looped video to virtual camera.
