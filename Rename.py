#-*- coding=utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui

import sys
import os
import re
import cv2
from useui.Main import Ui_MainWindow
from useui.VideoCapture import Ui_VideoCaptureWindow
from useui.updateversion import Ui_updateVersion
from useui.aboutme import Ui_Aboutme

class Rename(QMainWindow):
    signal_change = pyqtSignal()

    def __init__(self):
        super(Rename, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 設定無邊框
        # 設定背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # set Opacity
        self.setWindowOpacity(0.92)

        self.center = self.ui.centralwidget
        self.center.setStyleSheet(
            """
                background-color: #444444;
                border-top-left-radius:{0}px;
                border-bottom-left-radius:{0}px;
                border-top-right-radius:{0}px;
                border-bottom-right-radius:{0}px;
            """.format(20)
        )

        self.select_btn = self.ui.Select_dir
        self.start_btn = self.ui.Start_rename
        self.change_btn = self.ui.change
        self.file_dir = self.ui.FileDir
        self.change_name = self.ui.filename_willchange
        self.list_change_show = self.ui.change_list
        self.groupbox = self.ui.groupBox
        self.type1 = self.ui.type1
        self.type2 = self.ui.type2
        type1_font = QFont()
        type1_font.setFamily("微軟正黑體")
        type1_font.setPointSize(12)
        type1_font.setBold(True)
        QToolTip.setFont(type1_font)
        self.type1.setToolTip("This format Example：\nMyFileName_00.txt")
        self.type1.setStyleSheet(
            "color: #DDDDDD; height:35px"
        )
        type2_font = QFont()
        type2_font.setFamily("微軟正黑體")
        type2_font.setPointSize(12)
        type2_font.setBold(True)
        QToolTip.setFont(type2_font)
        self.type2.setToolTip("This format Example：\n00_MyFileName.txt")
        self.type2.setStyleSheet(
            "color: #DDDDDD; height:35px"
        )
        self.groupbox.setStyleSheet("border:0;")
        self.list_change_show.horizontalScrollBar().setStyleSheet(
            """
            QScrollBar {
            background-color: dimgray;
            margin: 0;
            height: 16px; 
            width: 16px;
            }
            QScrollBar::handle:horizontal {
            background-color: #555555;
            border: 1px #555555;
            border-radius: 6px;
            margin: 2px;
            }
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background-color: transparent;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            height: 0px;
            width: 0px;
            }
            """
        )
        self.list_change_show.verticalScrollBar().setStyleSheet(
            """
            QScrollBar {
            background-color: dimgray;
            margin: 0;
            height: 16px; 
            width: 16px;
            }
            QScrollBar::handle:vertical
            {
            background-color: #555555;
            border: 1px #555555;
            border-radius: 6px;
            margin: 2px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
            {
                background-color: transparent;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical
            {
                height: 0;
                width: 0;
            }
            """
        )


        font = QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        QToolTip.setFont(font)
        self.change_btn.setToolTip("Goto VideoCapture")

        # button style
        self.select_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.start_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.change_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QToolTip{color: #DDDDDD; background-color: #444444; border-radius: 10px; border: 1px solid white}"
        )
        self.file_dir.setStyleSheet(
            "color: #DDDDDD; height:35px"
        )
        self.list_change_show.setStyleSheet(
            "QListView{background-color: dimgray; color: #DDDDDD; border-radius: 10px}"
        )
        self.change_name.setStyleSheet(
            "QLineEdit{background-color: dimgray; color: #DDDDDD; border-radius:10px; height:35px}"
        )

        self.select_btn.clicked.connect(self.getfile)
        self.start_btn.clicked.connect(self.changename)
        self.change_btn.clicked.connect(self.signal_btn)
        self.signal_change.connect(self.ChangeToVideoCapture)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        self.contextMenu = QMenu(self)
        self.updateVersion = self.contextMenu.addAction(u'Update Version')
        self.aboutme_text = self.contextMenu.addAction(u'About Me')

        self.updateVersion.triggered.connect(self.updateversion)
        self.aboutme_text.triggered.connect(self.aboutme_ui)

    def showContextMenu(self, pos):
        self.contextMenu.move(self.pos() + pos)
        self.contextMenu.show()

    def getfile(self):
        path = QFileDialog.getExistingDirectory(self, 'Plaese Select File Dir', "D:\\")
        self.file_dir.setText(path)

    def changename(self):
        if self.change_name.text() != "" and self.file_dir.text() != 'File Dir' and self.file_dir.text() != "":
            path = self.file_dir.text() + '/'
            name = self.change_name.text()
            file = os.listdir(path)
            try:
                if self.type1.isChecked():
                    for i in range(len(file)):
                        extern = file[i].split('.')
                        old = path + file[i]
                        num = str(i+1).zfill(len(str(len(file))))
                        new = path + "{}_{}.{}".format(name, num,extern[1])
                        os.rename(old, new)
                        self.list_change_show.addItem('{} --> {}'.format(file[i], new))
                else:
                    for i in range(len(file)):
                        extern = file[i].split('.')
                        old = path + file[i]
                        num = str(i+1).zfill(len(str(len(file))))
                        new = path + "{}_{}.{}".format(num, name,extern[1])
                        os.rename(old, new)
                        self.list_change_show.addItem('{} --> {}'.format(file[i], new))
                msg = QMessageBox()
                msg.setWindowTitle("Sucess")
                msg.setText("Sucess ReName")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec_()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Something Error")
                msg.setStandardButtons(QMessageBox.Retry)
                msg.setDefaultButton(QMessageBox.Retry)
                msg.setDetailedText('SomethingError，Please Retry')
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please Type What you want to Change name!")
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setDetailedText('Please check where is Null')
            msg.exec_()

    def signal_btn(self):
        self.signal_change.emit()

    def ChangeToVideoCapture(self):
        self.close()
        self.vi = VideoCapture()
        self.vi.show()

    def updateversion(self):
        self.update_ver = UpdateVersion()
        self.update_ver.show()

    def aboutme_ui(self):
        self.ui = AboutMe()
        self.ui.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

class VideoCapture(QMainWindow):

    def __init__(self):
        super(VideoCapture, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_VideoCaptureWindow()
        self.ui.setupUi(self)

        # Close windows border
        # set Windows Transparent Background
        # set Background Opacity
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.94)

        self.center = self.ui.centralwidget
        self.center.setStyleSheet(
            """
                background-color: #444444;
                border-top-left-radius:{0}px;
                border-bottom-left-radius:{0}px;
                border-top-right-radius:{0}px;
                border-bottom-right-radius:{0}px;
            """.format(20)
        )

        self.selectFile_btn = self.ui.selectFile
        self.saveFilePath_btn = self.ui.SaveFileDir
        self.start_btn = self.ui.StartCapture
        self.changeToRename_btn = self.ui.change
        self.orignalFilePath = self.ui.OriginalFilePath
        self.saveFilePath = self.ui.SavePath
        self.frame = self.ui.frame
        self.listShow = self.ui.listcount
        self.groupbox = self.ui.groupBox
        self.groupbox.setStyleSheet("border:0;")
        font = QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        QToolTip.setFont(font)
        self.frame.setValidator(QtGui.QIntValidator())
        self.changeToRename_btn.setToolTip("Goto Rename")

        self.listShow.horizontalScrollBar().setStyleSheet(
            """
            QScrollBar {
            background-color: dimgray;
            margin: 0;
            height: 16px; 
            width: 16px;
            }
            QScrollBar::handle:horizontal {
            background-color: #555555;
            border: 1px #555555;
            border-radius: 6px;
            margin: 2px;
            }
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background-color: transparent;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            height: 0px;
            width: 0px;
            }
            """
        )
        self.listShow.verticalScrollBar().setStyleSheet(
            """
            QScrollBar {
            background-color: dimgray;
            margin: 0;
            height: 16px; 
            width: 16px;
            }
            QScrollBar::handle:vertical {
            background-color: #555555;
            border: 1px #555555;
            border-radius: 6px;
            margin: 2px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background-color: transparent;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
            width: 0px;
            }
            """
        )

        # ui StyleSheet
        self.selectFile_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.saveFilePath_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.start_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.start_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.changeToRename_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius: 10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QToolTip{color: #DDDDDD; background-color: #444444; border-radius: 10px; border: 1px solid white }"
        )
        self.orignalFilePath.setStyleSheet(
            "color: #DDDDDD; height:35px"
        )
        self.saveFilePath.setStyleSheet(
            "color: #DDDDDD; height:35px"
        )
        self.listShow.setStyleSheet(
            "QListView{background-color: dimgray; color: #DDDDDD; border-radius:10px}"
        )
        self.frame.setStyleSheet(
            "QLineEdit{background-color: dimgray; color: #DDDDDD; border-radius:10px; height:35px}"
        )

        self.changeToRename_btn.clicked.connect(self.change_Torename)
        self.selectFile_btn.clicked.connect(self.getfile)
        self.saveFilePath_btn.clicked.connect(self.savefile)
        self.start_btn.clicked.connect(self.StartVideoCpature)

    def change_Torename(self):
        self.close()
        self.ui = Rename()
        self.ui.show()

    def getfile(self):
        path = QFileDialog.getOpenFileName(self, self.tr('Plaese Open File'), './', 'Video Files(*.avi *.mp4 *.mpeg)')
        self.orignalFilePath.setText(path[0])

    def savefile(self):
        path = QFileDialog.getExistingDirectory(self, 'Please Select Save File Dir', './')
        self.saveFilePath.setText(path)

    def StartVideoCpature(self):
        if (self.orignalFilePath.text() != "" and self.saveFilePath.text() != "" and self.frame.text() != "" and self.saveFilePath.text() != "SaveFileDir" and self.orignalFilePath.text() != "FilePath"):
            video = cv2.VideoCapture('{}'.format(self.orignalFilePath.text()))

            if video.isOpened():
                val, frame = video.read()
            else:
                val = False
            c = 1
            millisecond = int(self.frame.text())
            save_path = self.saveFilePath.text()
            save_path = save_path.replace('/', '\\')
            while val:
                val, frame = video.read()
                if (c % millisecond == 0):
                    cv2.imwrite(('{}\\{}.jpg'.format(save_path, str(c))), frame)
                    self.listShow.addItem('{}.jpg --> {}'.format(str(c), self.saveFilePath.text()))
                c = c+1
                cv2.waitKey(1)
            video.release()
            msg = QMessageBox()
            msg.setWindowTitle("Sucess")
            msg.setText("Sucess ReName")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please check where is null!")
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setDetailedText('Please check where is Null')
            msg.exec_()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

class UpdateVersion(QMainWindow):

    def __init__(self):
        super(UpdateVersion, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_updateVersion()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.center = self.ui.centralwidget
        self.center.setStyleSheet(
            """
                background-color: #444444;
                border-top-left-radius:{0}px;
                border-bottom-left-radius:{0}px;
                border-top-right-radius:{0}px;
                border-bottom-right-radius:{0}px;
            """.format(20)
        )

        self.version = self.ui.vversion
        self.version.setStyleSheet(
            "QLabel{background-color: dimgray; color: #DDDDDD; border-radius:10px; height:35px; font: 18px; font-weight:bold}"
        )
        self.title = self.ui.label
        self.title.setStyleSheet(
            "QLabel{background-color: dimgray; color: #DDDDDD; border-radius:10px; height:35px}"
        )
        self.version.setText("\n2021/02/20 version:1.0.0\n"
                             "New Features:     Rename file\n\n"
                             "2021/02/21 version:1.0.1\n"
                             "Update New Ui\n\n"
                             "2021/02/22 version:1.1.0\n"
                             "New Features:     Video Capture\n\n"
                             "2021/02/25 version:1.1.1\n"
                             "Fix Some Ui\n\n"
                             "2021/03/03 version:1.1.2\n"
                             "Add New Ui and New Features\n\n")

        self.close_btn = self.ui.pushButton
        self.close_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.close_btn.clicked.connect(self.close_version)

    def close_version(self):
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

class AboutMe(QMainWindow):

    def __init__(self):
        super(AboutMe, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = Ui_Aboutme()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.center = self.ui.centralwidget
        self.center.setStyleSheet(
            """
                background-color: #444444;
                border-top-left-radius:{0}px;
                border-bottom-left-radius:{0}px;
                border-top-right-radius:{0}px;
                border-bottom-right-radius:{0}px;
            """.format(20)
        )

        self.title = self.ui.label
        self.content = self.ui.label_2
        self.close_btn = self.ui.pushButton

        self.close_btn.setStyleSheet(
            "QPushButton{color: #DDDDDD; height:35px}"
            "QPushButton{background-color:dimgray}"  # 按键背景色
            "QPushButton:hover{color:gray}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:10px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.title.setStyleSheet(
            "QLabel{background-color: dimgray; color: #DDDDDD; border-radius:10px; height:35px}"
        )
        self.content.setStyleSheet(
            "QLabel{background-color: dimgray; color: #DDDDDD; border-radius:10px; height:35px; font: 18px; font-weight:bold}"
        )


        self.content.setText(
            "\nHi I'm STUST CSIE university student\n\n"
            "This Program just developed by interest\n\n"""
            "Thank's for use it"
        )

        self.close_btn.clicked.connect(self.close_version)


    def close_version(self):
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


def main_ui():
    app = QApplication(sys.argv)
    rename = Rename()
    rename.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_ui()