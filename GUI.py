from ALEX import Ui_ALEX
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

     
class Gui_Start(QMainWindow):
            
    def __init__(self):
        super().__init__()
        self.ui = Ui_ALEX()
        self.ui.setupUi(self)
        
        self.ui.Exit.clicked.connect(self.close)
        
        self.ui.movies1= QtGui.QMovie("Ntuks.gif")
        self.ui.Voice.setMovie(self.ui.movies1)
        self.ui.movies1.start()
        
        self.ui.movies2= QtGui.QMovie("initial.gif")
        self.ui.Initial.setMovie(self.ui.movies2)
        self.ui.movies2.start()
        
        self.ui.movies3= QtGui.QMovie("Earth_Template.gif")
        self.ui.Earth.setMovie(self.ui.movies3)
        self.ui.movies3.start()
        
        self.ui.movies4= QtGui.QMovie("Hero_Template.gif")
        self.ui.Dis.setMovie(self.ui.movies4)
        self.ui.movies4.start()  
        
        self.ui.movies5= QtGui.QMovie("jhd.gif")
        self.ui.Ball0101.setMovie(self.ui.movies5)
        self.ui.movies5.start()
        
        self.ui.movies6= QtGui.QMovie("kjl.gif")
        self.ui.label.setMovie(self.ui.movies6)
        self.ui.movies6.start()
        
        self.ui.movies7= QtGui.QMovie("giphy.gif")
        self.ui.Circle.setMovie(self.ui.movies7)
        self.ui.movies7.start()
                      
  
Gui_App= QApplication(sys.argv)
Gui_G = Gui_Start()
Gui_G.show()      
exit(Gui_App.exec())    

