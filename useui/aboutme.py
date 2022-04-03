# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/17Lab/rename_file/useui/aboutme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Aboutme(object):
    def setupUi(self, Aboutme):
        Aboutme.setObjectName("Aboutme")
        Aboutme.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(Aboutme)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(20, 20, 20, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        Aboutme.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Aboutme)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName("menubar")
        Aboutme.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Aboutme)
        self.statusbar.setObjectName("statusbar")
        Aboutme.setStatusBar(self.statusbar)

        self.retranslateUi(Aboutme)
        QtCore.QMetaObject.connectSlotsByName(Aboutme)

    def retranslateUi(self, Aboutme):
        _translate = QtCore.QCoreApplication.translate
        Aboutme.setWindowTitle(_translate("Aboutme", "MainWindow"))
        self.label.setText(_translate("Aboutme", "About Me"))
        self.label_2.setText(_translate("Aboutme", "TextLabel"))
        self.pushButton.setText(_translate("Aboutme", "Close"))

