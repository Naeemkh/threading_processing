"""
An example of live data streaming
Author: Naeem Khoshnevis

Description:
These tutorials were helpful in crafting this app:

https://stackoverflow.com/questions/41103148/capture-webcam-video-using-pyqt
https://doc.qt.io/qt-5/qimage.html
https://www.codingforentrepreneurs.com/blog/open-cv-python-change-video-resolution-or-scale
 
"""

import os
import sys
import cv2
import multiprocessing

from PySide2.QtWidgets import (QApplication, QWidget, 
                               QPushButton, QCheckBox, QGroupBox,QLabel,
                               QGridLayout, QVBoxLayout)


from PySide2.QtCore import Signal, Slot

import camera_window as cw


class FirstWindow(QWidget):
    """
    Class for the main window
    """
    def __init__(self,camera_number):
        super().__init__()

        self.capture = None
        self.title = "Live Data Streaming" 
        self.video_frame = None
        self.camera_number = camera_number
        self.initialize()  


    def initialize(self):        
        """Intialize the main window"""        
        self.setWindowTitle(self.title)
        self.setGeometry(100,100,100,200)

        grid = QGridLayout()
        grid.addWidget(self.create_camera_group(),0,0)
        grid.addWidget(self.record_frame_group(),1,0)
        grid.addWidget(self.available_resources_group(),2,0)

        self.setLayout(grid)
        self.show()        

    def create_camera_group(self):
  
        self.groupbox1 = QGroupBox("Camera Capturing Controller")
        self.button1 = QPushButton("Start",self)
        self.button1.clicked.connect(self.start_recording)
        self.button2 = QPushButton("Stop",self)
        self.button2.clicked.connect(self.stop_recording)
        self.button3 = QPushButton("Close Camera",self)
        self.button3.clicked.connect(self.close_recording)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)        
        self.groupbox1.setLayout(vbox)

        return self.groupbox1


    def record_frame_group(self):
  
        self.groupbox2 = QGroupBox("Frame Recording Controller")

        self.button4 = QPushButton("Create New Folder",self)
        self.button4.clicked.connect(self.create_new_folder)

        self.start_cap = QPushButton("Start",self)
        self.start_cap.clicked.connect(self.start_saving_frames)

        self.stop_cap = QPushButton("Stop",self)
        self.stop_cap.clicked.connect(self.stop_saving_frames)

        gridbox = QGridLayout()
        self.foldername_l = QLabel("Folder Name: " ,self)
        self.foldername_v = QLabel("",self)
        self.capture_frame_rate_l   = QLabel("Capture Frame Rate: " ,self)
        self.capture_frame_rate_v   = QLabel("" ,self)

        gridbox.addWidget(self.foldername_l,0,0)
        gridbox.addWidget(self.foldername_v,0,1,1,2)
        gridbox.addWidget(self.capture_frame_rate_l,1,0)
        gridbox.addWidget(self.capture_frame_rate_v,1,1,1,1)
        gridbox.addWidget(self.button4,2,0,1,1)
        gridbox.addWidget(self.start_cap,2,1,1,1)
        gridbox.addWidget(self.stop_cap,2,2,1,1)

        self.groupbox2.setLayout(gridbox)

        return self.groupbox2    

    def image_labeling_group(self):

        self.groupbox3 = QGroupBox("Image Labeling Controller")
        self.button5 = QPushButton("Start Labeling Window", self)
        self.button5.clicked.connect(self.start_labeling_images)
        self.button6 = QPushButton("Choose Source Directory", self)
        self.button6.clicked.connect(self.choose_source_directory)
        self.button7 = QPushButton("Choose Target Directory", self)
        self.button7.clicked.connect(self.choose_target_directory)
        self.source_directory_l = QLabel("",self)
        self.target_directory_l = QLabel("",self)

        gridbox3 = QGridLayout()
        gridbox3.addWidget(self.button6,0,0)
        gridbox3.addWidget(self.source_directory_l,0,1,1,2)
        gridbox3.addWidget(self.button7,1,0)
        gridbox3.addWidget(self.target_directory_l,1,1,1,2)
        gridbox3.addWidget(self.button5,2,0)
        self.groupbox3.setLayout(gridbox3)

        return self.groupbox3

    def available_resources_group(self):

        self.groupbox4 = QGroupBox("Computational Power Controller",self)
        
        gridbox = QGridLayout()
        self.available_cpu = QLabel("Number of CPUs: ",self)
        self.available_cpu_v = QLabel(str(multiprocessing.cpu_count()),self)
        
        self.test_cpu = QPushButton("Load CPU(s)",self)
        self.test_cpu.clicked.connect(self.test_cpu_power)

        self.enable_multi_thread = QCheckBox(" Enable Threading", self)
        self.enable_multi_thread.setChecked(False)

        gridbox.addWidget(self.available_cpu,1,0)
        gridbox.addWidget(self.available_cpu_v,1,1)
        gridbox.addWidget(self.test_cpu,0,0,1,2)
        gridbox.addWidget(self.enable_multi_thread,2,0,1,1)
                
        self.groupbox4.setLayout(gridbox)

        return self.groupbox4


    def start_recording(self):
        print("Recording started ... ")
        if not self.video_frame:
            self.video_frame = cw.CamWindow(self.camera_number) 
        self.video_frame.start()
        self.video_frame.show()


    def stop_recording(self):
        print("Recording Stopped.")   
        self.video_frame.timer.stop()            

    def close_recording(self):
        print("Closing video frame window ... ")
        self.video_frame.cap.release()
        self.video_frame.close()


    def create_new_folder(self):
        pass


    def start_saving_frames(self):
        pass
   
    def stop_saving_frames(self):
        pass

    def test_cpu_power(self):
        pass 

    def make_connection_with_folder(self, other):
        pass

    @Slot(str,int)
    def update_new_folder_params(self,fname,frate):
        self.foldername_vtext = fname
        self.capture_frame_rate_for_record = frate
        self.foldername_v.setText(fname)
        self.capture_frame_rate_v.setText(str(frate))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = FirstWindow(0)
    sys.exit(app.exec_())
