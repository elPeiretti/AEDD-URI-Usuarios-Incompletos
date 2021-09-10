import pandas
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium import common
import time
from PyQt5.QtCore import QObject, pyqtSignal

# https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
# pip install openpyxl
# https://github.com/elPeiretti/python

class UriScript(QObject):
    
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.path = ""
        self.driver = None
        self.cant_usuarios = 0
        self.cant_incompletos = 0
        self.no_existentes = 0

    def setPath(self,path):
        self.path = path

    def getDriver(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        driver = webdriver.Firefox(options=opts)
        time.sleep(2)
        self.driver = driver

    def validateProfile(self,id):
        
        self.driver.get("https://www.urionlinejudge.com.br/judge/en/profile/"+id)

        try:
            pais = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/ul/li[2]")
            uni = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/ul/li[3]")
        
        except common.exceptions.NoSuchElementException: # no existe el usuario
            self.no_existentes+=1
            return -1 

        if "AR" in pais.get_attribute('innerHTML') and "UTN" in uni.get_attribute('innerHTML'):
            return 1
            
        self.cant_incompletos+=1
        return 0

    def exec(self):
        self.getDriver()

        # reads .csv file obtained from urionlinejudge.com.br/academic/
        col_list = ["uri","student","email"]
        data = pandas.read_csv(self.path, sep=';', usecols=col_list)
        listado = {
            'Estudiante': [],
            'Email': []
        }
        self.cant_usuarios = len(data)

        for i in range (len(data)):
            id = data.loc[i,"uri"]
            if self.validateProfile(str(id))==0:
                listado.get('Estudiante').append(data.loc[i,"student"])
                listado.get('Email').append(data.loc[i,"email"])
            self.progress.emit(i+1)

        pandas.DataFrame(listado, columns=["Estudiante","Email"]).to_excel("excel.xlsx", index = False, header=True)
        self.driver.quit()
        self.finished.emit()