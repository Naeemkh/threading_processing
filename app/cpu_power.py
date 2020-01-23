import time
import multiprocessing
import numpy as np
import concurrent.futures

from PySide2.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel, QTextEdit
from PySide2.QtCore import Qt

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QThread, Signal


class TestCPU(QWidget):

    def __init__(self,do_threading):
        super().__init__()
        self.do_threading = do_threading
        self.initialize()

    def initialize(self):
        
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("Multiprocessing Computation")
        
        vbox = QVBoxLayout()
        
        self.hs = QSlider()
        self.hs.setOrientation(Qt.Horizontal)
        self.hs.setTickInterval(1)
        self.hs.setProperty("value", 1)
        self.hs.setMinimum(1)
        self.n_cpu = multiprocessing.cpu_count()
        self.hs.setMaximum(self.n_cpu)
        self.hs.setTracking(True)
        self.hs.setTickPosition(QSlider.TicksBelow)
        self.hs.setTickInterval(1)
        self.hs.valueChanged.connect(lambda: self.label.setText("Max taken cores: " + str(self.hs.value())))
        
        vbox.addWidget(self.hs)
                
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Max taken cores: 1 ") 

        vbox.addWidget(self.label)

        self.pushButton = QtWidgets.QPushButton("Test")
        self.pushButton.clicked.connect(self.test_cpu)
        
        vbox.addWidget(self.pushButton)
     
        self.textEdit = QTextEdit()
        vbox.addWidget(self.textEdit)

        self.setLayout(vbox)
        self.show()    

    
    def test_cpu(self):
        
        if self.do_threading: 
            self.num_cpu = self.hs.value()
            self.mythread = MyThread(self.num_cpu)
            self.mythread.result_signal.connect(self.update_results)
            self.mythread.start()
        else:
            # create twice number of job based on total cpu cores
            num_cpu = self.hs.value()
            matrix = [600 for _ in range(4*multiprocessing.cpu_count())]
    
            start = time.time()
    
            with concurrent.futures.ProcessPoolExecutor(max_workers=num_cpu) as executer:
                executer.map(mat_multiply, matrix)
    
            end = time.time()
            this_processing = f'Time taken using {num_cpu} CPU core(s): {round(end - start,3)} seconds.'
    
            old_text = self.textEdit.toPlainText()
            updated_text = old_text + "\n" + this_processing
            self.textEdit.setText(updated_text)


    
    def update_results(self,val):
        old_text = self.textEdit.toPlainText()
        updated_text = old_text + "\n" + val
        self.textEdit.setText(updated_text)




def mat_multiply(matrix_size):
    print('Multiplication started ...')
    n = 1000
    while n>0:
        n -= 1
        yy = np.random.rand(matrix_size,matrix_size)
        np.multiply(yy,yy)    
    print('Multiplication ended.')     
 

class MyThread(QThread):
    result_signal = Signal(str)
    def __init__(self,num_cpu):
       super().__init__()
       self.num_cpu = num_cpu

    def run(self):
        matrix = [600 for _ in range(2*multiprocessing.cpu_count())]
        start = time.time()

        with concurrent.futures.ProcessPoolExecutor(max_workers=self.num_cpu) as executer:
            executer.map(mat_multiply, matrix)

        end = time.time()
        this_processing = f'Time taken using {self.num_cpu} CPU core(s): {round(end - start,3)} seconds.'
        self.result_signal.emit(this_processing)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    do_threading = False
    ui = TestCPU(do_threading)
    sys.exit(app.exec_())
