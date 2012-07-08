#-------------------------------------------------------------------------------
# Name:        neural_traiuning_gen
# Purpose:     The goal of this is to create a training set for a neural network
#              based on the webcam wireframe stream.
#
# Author:      smurftheweb
#
# Created:     08/07/2012
# Copyright:   (c) smurftheweb 2012
# Licence:     Unrestricted
#-------------------------------------------------------------------------------
import os
from camera import Camera
import cv2

WINDOW_NAME = "Live Feed"

class TrainerGenerator():
    def __init__(self, output_path):
        # setup camera object
        self.output_path = output_path
        self.camera = Camera()

        # check path exists, or create it if necessary
        self.check_dir(output_path)

    def check_dir(self, directory_path):
      """ Checks if a folder exists, and creates it if it does not"""
      d = os.path.dirname(output_path)
      if not os.path.exists(d): os.makedirs(d)

    def run(self):
      """ This loops continuously, getting the user's feedback on what to do
      for each wireframe / image"""
      # create a window for showing images
      cv2.namedWindow(WINDOW_NAME)

      # enter a wait key loop - escape will exit
      stopLoop = False
      imgCount = 1
      while (stopLoop is False):
        # grab a frame from the camera and show it to the user
        frame, wireframe = self.camera.grab_wireframe()
        cv2.imshow(WINDOW_NAME, frame)

        # wait for user response - what is the "action" to take
        key = cv2.waitKey(0)
        # if response was exit, then shut down
        if key == 27:
          stopLoop = True
          break

        # save wireframe + action into a training file
        # note for this all actions will be folders, containing files of
        # wireframes. This may change in the future!
        # TODO: cache whether we need to do this in a list of actions
        imgFolder = os.path.join(self.output_path, key)
        check_dir(imgFolder)
        imgFile = os.path.join(imgFolder, imgCount + ".dat")
        savetxt(imgFile, wireframe)
        imgCount = imgCount + 1

      # Tidy up and exit (if needed)
      return

def main():
    TrainerGenerator("~/Code/training_set/").run()

if __name__ == '__main__':
    main()
