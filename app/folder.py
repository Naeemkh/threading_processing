import os

from PySide2.QtWidgets import QDialog, QLabel, QVBoxLayout, QGridLayout,QLineEdit,QPushButton, QGroupBox, QMessageBox
from PySide2.QtCore import Signal


class CreateFolder(QDialog):
    
    foldersignal = Signal(str,int)

    def __init__(self, parent = None):
        super().__init__(parent = None)
        self.title = "Create new folder"
        self.setGeometry(100,100,400,100)
        self.folder_name = "NewFolder"
        self.frame_rate = 2
         
        self.content()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        self.setLayout(vbox)
        self.show()    
    
    def content(self):

        self.groupbox = QGroupBox("Capturing image configuration: ")
        
        mygrid = QGridLayout()
        
        self.label1 = QLabel("Folder Name:",self) 
        self.textedit1 = QLineEdit()
        self.textedit1.setMaximumHeight(20)
        
        self.label2 = QLabel("Number of Frame Per Second:",self) 
        self.textedit2 = QLineEdit()
        self.textedit2.setMaximumHeight(20)

        
        self.savebutton = QPushButton("Save",self)
        self.savebutton.clicked.connect(self.save_values)

        self.cancelbutton = QPushButton("Cancel",self)
        self.cancelbutton.clicked.connect(self.cancel)
                       
        mygrid.addWidget(self.label1,0,0)
        mygrid.addWidget(self.textedit1,0,1)
      
        mygrid.addWidget(self.label2,1,0)
        mygrid.addWidget(self.textedit2,1,1)

        mygrid.addWidget(self.savebutton,2,0)
        mygrid.addWidget(self.cancelbutton,2,1)

        
        self.groupbox.setLayout(mygrid)
  
    
    def save_values(self):

        if not self.textedit1.text() or not self.textedit2.text():
            msgBox = QMessageBox()
            msgBox.setText("Please insert valid Folder Name and CFR")
            msgBox.exec_()
        
        else:
            self.folder_name = self.textedit1.text()
            self.frame_rate = self.textedit2.text() 
            
            if not os.path.isdir(self.folder_name):
                os.mkdir(self.folder_name) 
    
            self.foldersignal.emit(self.folder_name,int(self.frame_rate))
            self.close()    

    def cancel(self):
        self.close()    