import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import *
from ui_QtApp import Ui_QtAppClass

class MainWindow(QtWidgets.QMainWindow):
    def onBtnOpenFile(self):
        filePath = QFileDialog.getOpenFileName(self, self.tr("Open Text File"), "", self.tr("Text Files (*.txt)"))[0]
        self.ui.lblPath.setText(filePath)

        file = QFile(filePath)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):                    
            self.ui.lblPath.setText("Cannot open file!")
            return
        
        sin = QTextStream(file)
        self.ui.plainTextEdit.setPlainText(sin.readAll())
        file.close()

    def onBtnSaveFile(self):
        file = QFile(self.ui.lblPath.text())
        if not file.open(QIODevice.WriteOnly | QIODevice.Truncate):
            self.ui.lblPath.setText("Cannot open file!")
            return    
        sin = QTextStream(file)
        sin << self.ui.plainTextEdit.toPlainText()
        file.close()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_QtAppClass()
        self.ui.setupUi(self)        
        self.ui.btnOpenFile.clicked.connect(self.onBtnOpenFile)
        self.ui.btnSave.clicked.connect(self.onBtnSaveFile)

if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    ret = app.exec_()
    sys.exit(ret)