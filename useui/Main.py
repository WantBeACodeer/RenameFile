# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/17Lab/rename_file/useui/Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.type2 = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.type2.setFont(font)
        self.type2.setObjectName("type2")
        self.gridLayout_2.addWidget(self.type2, 3, 0, 1, 1)
        self.filename_willchange = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filename_willchange.setFont(font)
        self.filename_willchange.setAlignment(QtCore.Qt.AlignCenter)
        self.filename_willchange.setObjectName("filename_willchange")
        self.gridLayout_2.addWidget(self.filename_willchange, 1, 0, 1, 1)
        self.FileDir = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FileDir.setFont(font)
        self.FileDir.setObjectName("FileDir")
        self.gridLayout_2.addWidget(self.FileDir, 0, 0, 1, 1)
        self.Select_dir = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Select_dir.setFont(font)
        self.Select_dir.setObjectName("Select_dir")
        self.gridLayout_2.addWidget(self.Select_dir, 0, 1, 1, 1)
        self.change_list = QtWidgets.QListWidget(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.change_list.setFont(font)
        self.change_list.setObjectName("change_list")
        self.gridLayout_2.addWidget(self.change_list, 4, 0, 1, 2)
        self.change = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.change.setFont(font)
        self.change.setObjectName("change")
        self.gridLayout_2.addWidget(self.change, 5, 1, 1, 1)
        self.type1 = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.type1.setFont(font)
        self.type1.setChecked(True)
        self.type1.setObjectName("type1")
        self.gridLayout_2.addWidget(self.type1, 2, 0, 1, 1)
        self.Start_rename = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Start_rename.setFont(font)
        self.Start_rename.setObjectName("Start_rename")
        self.gridLayout_2.addWidget(self.Start_rename, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rename"))
        self.type2.setText(_translate("MainWindow", "Number_Name"))
        self.filename_willchange.setPlaceholderText(_translate("MainWindow", "What name you will Change"))
        self.FileDir.setText(_translate("MainWindow", "File Dir"))
        self.Select_dir.setText(_translate("MainWindow", "    Select File Dir    "))
        self.change.setText(_translate("MainWindow", "VideoCapture"))
        self.type1.setText(_translate("MainWindow", "Name_Number"))
        self.Start_rename.setText(_translate("MainWindow", "   Start Rename   "))
