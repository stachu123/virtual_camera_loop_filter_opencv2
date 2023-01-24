while True:
  _, frame = cap.read()
  hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  low_yellow = np.array([15, 185, 15])
  high_yellow = np.array([40, 255, 255])
  yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
  yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

  if sum(sum(yellow_mask)) > 15000:
    output_yellow = cv2.addWeighted(yellow, alpha, frame, 1-alpha, 0)
    cv2.imshow("Frame", output_yellow)
  else:
    cv2.imshow("Frame", frame)

  key = cv2.waitKey(1)
  if key == 27:
    break