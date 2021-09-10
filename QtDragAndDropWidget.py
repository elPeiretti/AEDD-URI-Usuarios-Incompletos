from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
import os

class DragAndDropWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setUpUI()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls() and e.mimeData().urls().__len__() == 1:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        url = e.mimeData().urls()[0].toLocalFile()
        if url.find(".csv") != -1:
            self.tedit_path.setText(url)
        else:
            self.showErrorPopUp()

    def setUpUI(self):
        self.setObjectName("DragAndDropWidget")
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        
        self.btn_buscar = QtWidgets.QPushButton(self)
        self.btn_buscar.setGeometry(QtCore.QRect(255, 150, 131, 31))
        self.btn_buscar.setObjectName("btn_buscar")
        self.btn_buscar.clicked.connect(self.browsefiles)

        self.lbl_arrastrar = QtWidgets.QLabel(self)
        self.lbl_arrastrar.setGeometry(QtCore.QRect(100, 50, 440, 91))
        self.lbl_arrastrar.setObjectName("lbl_arrastrar")

        self.tedit_path = QtWidgets.QLineEdit(self)
        self.tedit_path.setEnabled(False)
        self.tedit_path.setGeometry(QtCore.QRect(20, 200, 591, 31))
        self.tedit_path.setObjectName("tedit_path")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("DragAndDropWidget", "DragAndDropWidget"))
        self.btn_buscar.setText(_translate("DragAndDropWidget", "Buscar"))
        self.lbl_arrastrar.setText(_translate("DragAndDropWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Arrastre el archivo .csv aquí<br/>o</span></p></body></html>"))

    def browsefiles(self):
        file = QFileDialog.getOpenFileName(self,'Buscar archivo',os.getcwd(),'CSV Files (*.csv)')
        self.tedit_path.setText(file[0])

    def showErrorPopUp(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Advertencia")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Solo se pueden procesar archivos del tipo .csv")
        x = msg.exec_()