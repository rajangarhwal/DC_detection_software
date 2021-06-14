# DC_detection_software

This software AIM on microscopic image of blood cell. Software refines the chromosomes of microscopic image of blood cell using Image processing in python. Developed GUI for user interaction with chromosomes Di centric, Mono centric counts and stats. Manual detection also implemented for better accuracy.

## Main Module
 
Graphical user interface (GUI) developed in Main module using Tkinter in python. Manual detection also implemented in the same.

## Ranking Module

All the algorithms or image processing in python is done inside Ranking module. Rank defining of a image according to image's property is also done in Ranking module.

## Software Requirements
1. Python 2.7
2. cv2 ( OpenCV )
3. Tkinter, Tkconstants, tkFileDialog, tkMessageBox, ttk
4. os
5. PIL
6. time
7. shutil
8. sys
9. threading
10. numpy
11. argparse
12. openpyxl
13. skimage
14. scipy
15. progressbar
16. random
17. matplotlib

## Steps to use Software
1. Open Main python file to load GUI
2. Select the folder in which microscopic image of blood cells resides ( Select Folder ).
3. Run the Ranking algorithm on selected images (Run Ranking Algorithm ).
4. Select the rank from which you want to select images ( Show Images Upto ).
5. Check the images rank statistics ( Rank Statistics ).
6. Select one image and detect DC (Red boundary), Mono(Green Boundary) centric chromosomes ( Detect DC ).
7. If want use manual detection (Manual Detection).
8. In manual detection, select Mono centric right click to add an mono centric chromosome and left to delete.
9. In manual detection, select Di centric left click to add an di centric chromosome and right to delete.
10. Stats ( Total files, Total Chromosomes, Di centric Chromosomes, Mono centric Chromosomes) are shown below in the GUI.
11. EXIT ( Exit ).
