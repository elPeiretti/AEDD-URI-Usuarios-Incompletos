from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
import multiprocessing
from UriScript import UriScript
from PyQt5.QtCore import QThread

class ProgressMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        self.setObjectName("ProgressMenu")
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        
        self.spt = UriScript()

        self.lbl_procesando = QtWidgets.QLabel(self)
        self.lbl_procesando.setGeometry(QtCore.QRect(100, 190, 440, 20))
        self.lbl_procesando.setObjectName("lbl_procesando")
        self.lbl_procesando.setText("Inicializando...")

        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(QtCore.QRect(100, 220, 440, 30))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ProgressMenu", "Procesando"))

    def reportProgress(self,i):
        self.lbl_procesando.setText("Procesando usuario "+str(i)+" / "+str(self.spt.cant_usuarios))
        self.pbar.setValue(i/self.spt.cant_usuarios *100)

    def script(self,path):
        self.spt.setPath(path)
        self.thread = QThread()
        self.spt.moveToThread(self.thread)

        self.thread.started.connect(self.spt.exec)
        self.spt.finished.connect(self.thread.quit)
        self.spt.finished.connect(self.finalizarPopup)
        self.spt.finished.connect(self.spt.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.spt.progress.connect(self.reportProgress) 
        self.thread.start()

    def finalizarPopup(self):
        #todo
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Fin del proceso")
        msg.setText("El proceso a finalizado exitosamente.")
        x = msg.exec_()