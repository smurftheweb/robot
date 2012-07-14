#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  network_trainer.py
#
#  Copyright 2012 smurftheweb (smurftheweb@gmail.com)
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os
import cv2

class NetworkTrainer():

  def __init__(self):
    pass

  def load_network(self, root_folder):
    """ From a specified network definition, or training set folder,
        load the network parameters. """
    # first check for and load the network definition file
    if os.path.isfile(root_folder):
      self.network_file = root_folder
      self.folder = os.path.dirname(root_folder)
    else:
      self.network_file = os.path.join(root_folder, "network.def")
      self.folder = root_folder
    if not os.path.exists(self.network_file):
      raise Exception("Network file '{0}' does not exist".format(self.network_file))

    fin = open(self.network_file, 'r')
    line = fin.readline()
    self.width, self.height, self.middle_layer, self.output_layer = line.split()

    # work out how many images there are in total
    self.images = dict()
    totalImageCount = 0
    for (folder, subfolders, files) in os.walk(self.folder):
      if folder == self.folder: continue
      ignore, class_name = os.path.split(folder)
      classImages = list()
      for file in files:
        classImages.append(os.path.join(folder, file))
      self.images[class_name] = classImages
    print self.images

    # now we know that, create a dataset of filename / result
    # split into training / test set (70% / 30%)

  def load_image(self, file_name, expected_result):
    pass

def main():
  trainer = NetworkTrainer()
  trainer.load_network("/home/user/Dropbox/Code/Robot/object_training_set")

if __name__ == '__main__':
  main()

