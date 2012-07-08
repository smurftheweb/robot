#-------------------------------------------------------------------------------
# Name:        Camera test
# Purpose:     Just makes sure the camera class works
#
# Author:      smurftheweb
#
# Created:     08/07/2012
# Copyright:   (c) smurftheweb 2012
# Licence:     Unrestricted
#-------------------------------------------------------------------------------

def main():
  cam = Camera()
  if cam is None:
    print "Could not create camera class"
    return

  print "Camera: {0}x{1}".format(cam.width, cam.height)
  # show camera stream, wireframe and colour wireframe
  cv2.namedWindow("camera")
  cv2.namedWindow("wireframe")
  cv2.namedWindow("colour wireframe")
  key = -1
  while (key < 0):
    img, edges, coledge = cam.grab_colour_wireframe()
    cv2.imshow("camera", img)
    cv2.imshow("wireframe", edges)
    cv2.imshow("colour wireframe", coledge)
    key = cv2.waitKey(10)
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
