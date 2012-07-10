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
    
    def load_image_defs(self, root_folder):
        # first work out how many images there are in total
        # now we know that, create a dataset of filename / result
        # split into training / test set (70% / 30%)
        pass
        
    def setup_network(self):
        # Find a test image, and load it
        # Work out size of network needed
        pass
    
    def load_image(self, file_name, expected_result):
        pass
    

def main():
	
	return 0

if __name__ == '__main__':
	main()

