import cv2

# create camera
device = cv2.VideoCapture(0)
if device.isOpened() is False:
  print "Camera could not be created"
else:
  # show camera stream
  cv2.namedWindow("camera")
  key = -1
  while (key < 0):
    success, img = device.read()
    cv2.imshow("camera", img)
    key = cv2.waitKey(10)
  cv2.destroyAllWindows()
