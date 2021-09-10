from PyQt5 import QtCore, QtWidgets
from MainMenu import MainMenu
from ProgressMenu import ProgressMenu

class UI_MainWindow(QtWidgets.QMainWindow):

    def setupUI(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        
        self.stackedwidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedwidget.setObjectName("stackedwidget")
        
        self.mainMenu = MainMenu()
        self.mainMenu.btn_comenzar.clicked.connect(self.start)

        self.progressMenu = ProgressMenu()

        self.stackedwidget.addWidget(self.mainMenu)
        self.stackedwidget.addWidget(self.progressMenu)

        MainWindow.setCentralWidget(self.stackedwidget)
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

    def start(self):
        self.progressMenu.script(self.mainMenu.wdg_file_drop.tedit_path.text())
        self.stackedwidget.setCurrentWidget(self.progressMenu)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindow(MainWindow)
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
