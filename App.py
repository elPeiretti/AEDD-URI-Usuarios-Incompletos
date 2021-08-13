from PyQt5 import QtCore, QtGui, QtWidgets
from QtDragAndDropWidget import DragAndDropWidget
from UriScript import UriScript
import multiprocessing


class UI_MainWindow(QtWidgets.QMainWindow):

    def setupUI(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.spt = UriScript()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.wdg_file_drop = DragAndDropWidget(self.centralwidget)
        self.wdg_file_drop.setGeometry(QtCore.QRect(10, 10, 611, 341))
        self.wdg_file_drop.setObjectName("wdg_file_drop")
        self.wdg_file_drop.tedit_path.textChanged.connect( lambda: self.btn_comenzar.setEnabled(True))

        font = QtGui.QFont()
        font.setFamily("Garuda")
        font.setItalic(False)
        font.setKerning(True)

        self.btn_comenzar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_comenzar.setGeometry(QtCore.QRect(490, 390, 131, 31))
        self.btn_comenzar.setObjectName("btn_comenzar")
        self.btn_comenzar.setEnabled(False)
        self.btn_comenzar.clicked.connect(self.script)

        self.btn_ayuda = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ayuda.setGeometry(QtCore.QRect(20, 390, 100, 31))
        self.btn_ayuda.setObjectName("btn_ayuda")
        self.btn_ayuda.clicked.connect(self.showPopUp)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TITULO"))
        self.btn_comenzar.setText(_translate("MainWindow", "Comenzar"))
        self.btn_ayuda.setText(_translate("MainWindow", "Ayuda"))

    def showPopUp(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Ayuda")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setText("1) Descargue el archivo .csv del curso correspondiente en la página www.urionlinejudge.com.br/academic/, el cual se encuentra en el apartado 'Students' del curso seleccionado\n\n"+
                    "2) Arraste el archivo en el programa y verifique que le aparezca la ubicacion del archivo en el diálogo correspondiente.\n\n"+
                    "3) Presione el botón comenzar para procesar todos los usuarios y espere a que el proceso finalice.\n\n"+
                    "4) Una vez finalizado el proceso, se creará un archivo .xls (excel) con los usuarios que no contengan el perfil con el país y/o la universidad completos.")
        x = msg.exec_()

    def script(self):
        self.spt.setPath(self.wdg_file_drop.tedit_path.text())
        proc = multiprocessing.Process(target=self.spt.exec)
        proc.daemon = True
        proc.start()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindow(MainWindow)
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
