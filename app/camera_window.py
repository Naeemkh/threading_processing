import os
import sys

import cv2

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel


from PySide2 import QtGui, QtCore
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Slot



class CamWindow(QWidget):
    def __init__(self,camera_number):
        super().__init__()

        self.camera_number = camera_number
        self.is_saving_frames = False
        self.ith_frame = 1
        self.saving_folder = None
        self.saving_frame_counter = 1

        # set a label place to hold video
        self.video = QLabel()
        vbox = QVBoxLayout()
        vbox.addWidget(self.video)
        self.setLayout(vbox)
        self.initialize_camera()
        self.show()


    def initialize_camera(self, *args):
        self.fps = 30
        self.cap = cv2.VideoCapture(self.camera_number)
        self.cap.set(3,640)
        self.cap.set(4,480)
  

    def next_frame_slot(self):
        ret, frame = self.cap.read()

        # Save images if isCapturing
        
        if self.is_saving_frames and self.saving_folder and (self.saving_frame_counter % self.fps)==0:
            cv2.imwrite(self.saving_folder + '/img_%05d.jpg'%self.ith_frame, frame)
            self.ith_frame += 1
            self.saving_frame_counter = 1
        else:
            self.saving_frame_counter += 1

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # The QImage class provides a hardware-independent image representation
        # that allows direct access to the pixel data, and can be used as a paint device. 
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        
        # QPixmap is designed and optimized for showing images on screen
        pix = QPixmap.fromImage(img)
        self.video.setPixmap(pix)    


    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.next_frame_slot)
        self.timer.start(1000./self.fps)



