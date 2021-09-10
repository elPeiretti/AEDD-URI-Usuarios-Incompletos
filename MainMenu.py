from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
import os
from QtDragAndDropWidget import DragAndDropWidget

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        self.setObjectName("MainMenu")
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        self.wdg_file_drop = DragAndDropWidget(self)
        self.wdg_file_drop.setGeometry(QtCore.QRect(10, 10, 611, 341))
        self.wdg_file_drop.setObjectName("wdg_file_drop")
        self.wdg_file_drop.tedit_path.textChanged.connect( lambda: self.btn_comenzar.setEnabled(True))

        font = QtGui.QFont()
        font.setFamily("Garuda")
        font.setItalic(False)
        font.setKerning(True)

        self.btn_comenzar = QtWidgets.QPushButton(self)
        self.btn_comenzar.setGeometry(QtCore.QRect(490, 390, 131, 31))
        self.btn_comenzar.setObjectName("btn_comenzar")
        self.btn_comenzar.setEnabled(False)

        self.btn_ayuda = QtWidgets.QPushButton(self)
        self.btn_ayuda.setGeometry(QtCore.QRect(20, 390, 100, 31))
        self.btn_ayuda.setObjectName("btn_ayuda")
        self.btn_ayuda.clicked.connect(self.showPopUp)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainMenu", "TITULO"))
        self.btn_comenzar.setText(_translate("MainMenu", "Comenzar"))
        self.btn_ayuda.setText(_translate("MainMenu", "Ayuda"))

    def browsefiles(self):
        file = QFileDialog.getOpenFileName(self,'Buscar archivo',os.getcwd(),'CSV Files (*.csv)')
        self.tedit_path.setText(file[0])
    
    def showPopUp(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Ayuda")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setText("1) Descargue el archivo .csv del curso correspondiente en la página www.urionlinejudge.com.br/academic/, el cual se encuentra en el apartado 'Students' del curso seleccionado\n\n"+
                    "2) Arraste el archivo en el programa y verifique que le aparezca la ubicacion del archivo en el diálogo correspondiente.\n\n"+
                    "3) Presione el botón comenzar para procesar todos los usuarios y espere a que el proceso finalice.\n\n"+
                    "4) Una vez finalizado el proceso, se creará un archivo .xlsx (excel) con los usuarios que no contengan el perfil con el país y/o la universidad completos.")
        x = msg.exec_()

    