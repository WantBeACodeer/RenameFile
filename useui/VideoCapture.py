# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/17Lab/rename_file/useui/VideoCapture.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VideoCaptureWindow(object):
    def setupUi(self, VideoCaptureWindow):
        VideoCaptureWindow.setObjectName("VideoCaptureWindow")
        VideoCaptureWindow.resize(783, 581)
        self.centralwidget = QtWidgets.QWidget(VideoCaptureWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OriginalFilePath = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OriginalFilePath.setFont(font)
        self.OriginalFilePath.setObjectName("OriginalFilePath")
        self.gridLayout_2.addWidget(self.OriginalFilePath, 0, 0, 1, 1)
        self.selectFile = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectFile.setFont(font)
        self.selectFile.setObjectName("selectFile")
        self.gridLayout_2.addWidget(self.selectFile, 0, 1, 1, 1)
        self.SavePath = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SavePath.setFont(font)
        self.SavePath.setObjectName("SavePath")
        self.gridLayout_2.addWidget(self.SavePath, 1, 0, 1, 1)
        self.SaveFileDir = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SaveFileDir.setFont(font)
        self.SaveFileDir.setObjectName("SaveFileDir")
        self.gridLayout_2.addWidget(self.SaveFileDir, 1, 1, 1, 1)
        self.frame = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setAlignment(QtCore.Qt.AlignCenter)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)
        self.StartCapture = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StartCapture.setFont(font)
        self.StartCapture.setObjectName("StartCapture")
        self.gridLayout_2.addWidget(self.StartCapture, 2, 1, 1, 1)
        self.change = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.change.setFont(font)
        self.change.setObjectName("change")
        self.gridLayout_2.addWidget(self.change, 4, 1, 1, 1)
        self.listcount = QtWidgets.QListWidget(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listcount.setFont(font)
        self.listcount.setObjectName("listcount")
        self.gridLayout_2.addWidget(self.listcount, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        VideoCaptureWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VideoCaptureWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 25))
        self.menubar.setObjectName("menubar")
        VideoCaptureWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VideoCaptureWindow)
        self.statusbar.setObjectName("statusbar")
        VideoCaptureWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VideoCaptureWindow)
        QtCore.QMetaObject.connectSlotsByName(VideoCaptureWindow)

    def retranslateUi(self, VideoCaptureWindow):
        _translate = QtCore.QCoreApplication.translate
        VideoCaptureWindow.setWindowTitle(_translate("VideoCaptureWindow", "VideoCapture"))
        self.OriginalFilePath.setText(_translate("VideoCaptureWindow", "FilePath"))
        self.selectFile.setText(_translate("VideoCaptureWindow", "Select File"))
        self.SavePath.setText(_translate("VideoCaptureWindow", "SaveFileDir"))
        self.SaveFileDir.setText(_translate("VideoCaptureWindow", "   Select File Dir   "))
        self.frame.setPlaceholderText(_translate("VideoCaptureWindow", "(How many frames to take a screenshot,only number)"))
        self.StartCapture.setText(_translate("VideoCaptureWindow", "   Start Capture   "))
        self.change.setText(_translate("VideoCaptureWindow", "Rename"))
