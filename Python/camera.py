import cv2

class Camera():
  """ This is a simple camera, encapsulating all the camera code."""
  
  def __init__(self, cameraId=0, width=0, height=0, flip_image=True):
    # store params
    self.cameraId = cameraId
    self.flip_image = flip_image
    
    # attempt to create a camera
    self.camera_device = cv2.VideoCapture(cameraId)
    if self.camera_device is None or self.camera_device.isOpened is False:
      raise Exception("Could not create camera device")
      
    # set camera parameters
    if width > 0:
      self.camera_device.SetCaptureProperty(cv2.CV_CAP_PROP_FRAME_WIDTH, width)
    if height > 0:
      self.camera_device.SetCaptureProperty(cv2.CV_CAP_PROP_FRAME_HEIGHT, height)
    
    # grab a test frame, and use it to pull some params  
    success, test_frame = self.camera_device.read()
    if success is False:
      raise Exception("An error occurred while trying to grab the test image")
      
    self.width, self.height, self.channels = test_frame.shape
      
  def grab_frame(self):
    if self.camera_device is None:
      raise Exception("No camera device has been created")
    success, img = self.camera_device.read()
    if not success: 
      raise Exception("Could not grab image")
    
    if self.flip_image: 
      return cv2.flip(img, 0)
    else:
      return img
      
  def grab_wireframe(self, threshold=30):
    
    # grab frame, convert to greyscale, and canny for the edges
    frame = self.grab_frame()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold, threshold*3)
    
    return (frame, edges)
      
  def grab_colour_wireframe(self, threshold=30):
    # grab frame
    frame = self.grab_frame()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold, threshold*3)
    
    color_edges = frame.copy()
    color_edges /= 2
    color_edges[edges == 0] = (0, 0, 0)
    
    return (frame, edges, color_edges)

if __name__ == "__main__":
  cam = Camera()
  print "Camera: {0}x{1}".format(cam.width, cam.height)
  # show camera stream
  cv2.namedWindow("camera")
  cv2.namedWindow("edges")
  cv2.namedWindow("colour edges")
  key = -1
  while (key < 0):
    img, edges, coledge = cam.grab_colour_wireframe()
    cv2.imshow("camera", img)
    cv2.imshow("edges", edges)
    cv2.imshow("colour edges", coledge)
    key = cv2.waitKey(10)
  cv2.destroyAllWindows()
