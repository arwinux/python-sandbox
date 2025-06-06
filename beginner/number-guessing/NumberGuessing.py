# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NumberGuessing.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowNumberGuessing(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 234)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 256))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PVS/1089781.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.BackgroundBehind_2 = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundBehind_2.setEnabled(True)
        self.BackgroundBehind_2.setGeometry(QtCore.QRect(15, 15, 421, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackgroundBehind_2.sizePolicy().hasHeightForWidth())
        self.BackgroundBehind_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.BackgroundBehind_2.setFont(font)
        self.BackgroundBehind_2.setToolTipDuration(0)
        self.BackgroundBehind_2.setAutoFillBackground(False)
        self.BackgroundBehind_2.setStyleSheet("background: rgba(35, 35, 35, 0.7);\n"
"border-radius:5px;\n"
"")
        self.BackgroundBehind_2.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText)
        self.BackgroundBehind_2.setText("")
        self.BackgroundBehind_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BackgroundBehind_2.setObjectName("BackgroundBehind_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(331, 15, 106, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.help_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.help_btn.setMinimumSize(QtCore.QSize(18, 18))
        self.help_btn.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setBold(True)
        font.setWeight(75)
        self.help_btn.setFont(font)
        self.help_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help_btn.setStyleSheet("background-color: rgb(5,195,221);\n"
"border-radius:8px;")
        self.help_btn.setObjectName("help_btn")
        self.horizontalLayout.addWidget(self.help_btn)
        self.pushButtonMinimize = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonMinimize.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButtonMinimize.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButtonMinimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonMinimize.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius:8px;")
        self.pushButtonMinimize.setText("")
        self.pushButtonMinimize.setObjectName("pushButtonMinimize")
        self.horizontalLayout.addWidget(self.pushButtonMinimize)
        self.pushButtonMaximiz = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonMaximiz.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButtonMaximiz.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButtonMaximiz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonMaximiz.setStyleSheet("background-color: rgb(255, 226, 0);\n"
"border-radius:8px;")
        self.pushButtonMaximiz.setText("")
        self.pushButtonMaximiz.setObjectName("pushButtonMaximiz")
        self.horizontalLayout.addWidget(self.pushButtonMaximiz)
        self.pushButtonExit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonExit.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButtonExit.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButtonExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonExit.setStyleSheet("background-color:rgb(255, 97, 6);\n"
"border-radius:8px;")
        self.pushButtonExit.setText("")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.horizontalLayout.addWidget(self.pushButtonExit)
        self.start = QtWidgets.QLineEdit(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(15, 75, 121, 36))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.start.setFont(font)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("background: rgba(0, 0, 0, 0.7);\n"
"color : rgba(220, 220,220);\n"
"padding-left: 10;\n"
"border-radius:4px;\n"
"\n"
"")
        self.start.setText("")
        self.start.setCursorPosition(0)
        self.start.setClearButtonEnabled(False)
        self.start.setObjectName("start")
        self.stop = QtWidgets.QLineEdit(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(150, 75, 121, 36))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.stop.setFont(font)
        self.stop.setAutoFillBackground(False)
        self.stop.setStyleSheet("background: rgba(0, 0, 0, 0.7);\n"
"color : rgba(220, 220,220);\n"
"padding-left: 10;\n"
"border-radius:4px;\n"
"")
        self.stop.setText("")
        self.stop.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.stop.setCursorPosition(0)
        self.stop.setClearButtonEnabled(False)
        self.stop.setObjectName("stop")
        self.chances = QtWidgets.QLineEdit(self.centralwidget)
        self.chances.setGeometry(QtCore.QRect(285, 75, 151, 36))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.chances.setFont(font)
        self.chances.setAutoFillBackground(False)
        self.chances.setStyleSheet("background: rgba(0, 0, 0, 0.7);\n"
"color : rgba(220, 220,220);\n"
"padding-left: 10;\n"
"border-radius:4px;\n"
"")
        self.chances.setText("")
        self.chances.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.chances.setCursorPosition(0)
        self.chances.setClearButtonEnabled(False)
        self.chances.setObjectName("chances")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(360, 165, 76, 36))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.reset.setFont(font)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setStyleSheet("background: rgba(0,0,0,0.8);\n"
"color : rgba(240,240,240);\n"
"border-radius:4px;\n"
"")
        self.reset.setObjectName("reset")
        self.yourguess = QtWidgets.QLineEdit(self.centralwidget)
        self.yourguess.setGeometry(QtCore.QRect(15, 120, 421, 36))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.yourguess.setFont(font)
        self.yourguess.setAutoFillBackground(False)
        self.yourguess.setStyleSheet("background: rgba(0, 0, 0, 0.7);\n"
"color : rgba(220, 220,220);\n"
"padding-left: 10;\n"
"border-radius:4px;\n"
"")
        self.yourguess.setText("")
        self.yourguess.setCursorPosition(0)
        self.yourguess.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.yourguess.setClearButtonEnabled(False)
        self.yourguess.setObjectName("yourguess")
        self.Suggestioandresult = QtWidgets.QLabel(self.centralwidget)
        self.Suggestioandresult.setGeometry(QtCore.QRect(15, 165, 241, 36))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(13)
        self.Suggestioandresult.setFont(font)
        self.Suggestioandresult.setStyleSheet("background: rgba(0, 0, 0, 0.7);\n"
"color : rgba(220, 220,220);\n"
"padding-left: 10;\n"
"border-radius:4px;\n"
"")
        self.Suggestioandresult.setObjectName("Suggestioandresult")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(270, 165, 76, 36))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.check.setFont(font)
        self.check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check.setStyleSheet("background: rgba(0,0,0,0.8);\n"
"color : rgba(240,240,240);\n"
"border-radius:4px;\n"
"")
        self.check.setObjectName("check")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButtonExit.clicked.connect(MainWindow.close)
        self.pushButtonMinimize.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Number Guessing"))
        self.help_btn.setText(_translate("MainWindow", "H"))
        self.start.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.start.setPlaceholderText(_translate("MainWindow", "Start"))
        self.stop.setPlaceholderText(_translate("MainWindow", "Stop"))
        self.chances.setPlaceholderText(_translate("MainWindow", "Chances"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.yourguess.setPlaceholderText(_translate("MainWindow", "Your guess"))
        self.Suggestioandresult.setText(_translate("MainWindow", "Suggestion and Result"))
        self.check.setText(_translate("MainWindow", "Check"))


