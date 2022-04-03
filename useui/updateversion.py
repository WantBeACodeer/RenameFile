# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/17Lab/rename_file/useui/updateversion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_updateVersion(object):
    def setupUi(self, updateVersion):
        updateVersion.setObjectName("updateVersion")
        updateVersion.resize(402, 611)
        self.centralwidget = QtWidgets.QWidget(updateVersion)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 11, -1, 11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.vversion = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.vversion.setFont(font)
        self.vversion.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.vversion.setObjectName("vversion")
        self.gridLayout_2.addWidget(self.vversion, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        updateVersion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(updateVersion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 25))
        self.menubar.setObjectName("menubar")
        updateVersion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(updateVersion)
        self.statusbar.setObjectName("statusbar")
        updateVersion.setStatusBar(self.statusbar)

        self.retranslateUi(updateVersion)
        QtCore.QMetaObject.connectSlotsByName(updateVersion)

    def retranslateUi(self, updateVersion):
        _translate = QtCore.QCoreApplication.translate
        updateVersion.setWindowTitle(_translate("updateVersion", "AboutMe"))
        self.label.setText(_translate("updateVersion", "Update Version"))
        self.vversion.setText(_translate("updateVersion", "TextLabel"))
        self.pushButton.setText(_translate("updateVersion", "Close"))

