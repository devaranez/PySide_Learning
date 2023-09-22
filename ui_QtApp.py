# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtApp.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

class Ui_QtAppClass(object):
    def setupUi(self, QtAppClass):
        if not QtAppClass.objectName():
            QtAppClass.setObjectName(u"QtAppClass")
        QtAppClass.resize(649, 558)
        self.centralWidget = QWidget(QtAppClass)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lblPath = QLabel(self.widget)
        self.lblPath.setObjectName(u"lblPath")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPath.sizePolicy().hasHeightForWidth())
        self.lblPath.setSizePolicy(sizePolicy)
        self.lblPath.setFrameShape(QFrame.WinPanel)
        self.lblPath.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.lblPath)

        self.btnOpenFile = QPushButton(self.widget)
        self.btnOpenFile.setObjectName(u"btnOpenFile")

        self.horizontalLayout.addWidget(self.btnOpenFile)


        self.verticalLayout.addWidget(self.widget)

        self.plainTextEdit = QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setInputMethodHints(Qt.ImhMultiLine)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.widget_2 = QWidget(self.centralWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnSave = QPushButton(self.widget_2)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addWidget(self.widget_2)

        QtAppClass.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(QtAppClass)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 649, 21))
        QtAppClass.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(QtAppClass)
        self.mainToolBar.setObjectName(u"mainToolBar")
        QtAppClass.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(QtAppClass)
        self.statusBar.setObjectName(u"statusBar")
        QtAppClass.setStatusBar(self.statusBar)

        self.retranslateUi(QtAppClass)

        QMetaObject.connectSlotsByName(QtAppClass)
    # setupUi

    def retranslateUi(self, QtAppClass):
        QtAppClass.setWindowTitle(QCoreApplication.translate("QtAppClass", u"QtApp", None))
        self.label_2.setText(QCoreApplication.translate("QtAppClass", u"\u8def\u5f91:", None))
        self.lblPath.setText(QCoreApplication.translate("QtAppClass", u"TextLabel", None))
        self.btnOpenFile.setText(QCoreApplication.translate("QtAppClass", u"\u958b\u555f\u6a94\u6848", None))
        self.btnSave.setText(QCoreApplication.translate("QtAppClass", u"\u5132\u5b58", None))
    # retranslateUi

