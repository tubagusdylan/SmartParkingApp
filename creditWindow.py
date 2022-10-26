from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreditWindow(object):
    def setupUi(self, CreditWindow):
        CreditWindow.setObjectName("CreditWindow")
        CreditWindow.resize(353, 283)
        CreditWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(CreditWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #4F90BD;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 70, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 160, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 130, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 101, 101))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("image/gambar.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(240, 200, 93, 28))
        self.close_button.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"    color: #4F90BD;\n"
"    border: 1px solid #4F90BD;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #4F90BD;\n"
"    color: white;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.close_button.setObjectName("close_button")
        CreditWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreditWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 26))
        self.menubar.setObjectName("menubar")
        CreditWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreditWindow)
        self.statusbar.setObjectName("statusbar")
        CreditWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CreditWindow)
        QtCore.QMetaObject.connectSlotsByName(CreditWindow)


    def retranslateUi(self, CreditWindow):
        _translate = QtCore.QCoreApplication.translate
        CreditWindow.setWindowTitle(_translate("CreditWindow", "Credits"))
        self.label.setText(_translate("CreditWindow", "Smart Parking App"))
        self.label_2.setText(_translate("CreditWindow", "Miftahul Tirta Irawan E\'20"))
        self.label_3.setText(_translate("CreditWindow", "Aisyah Rafa Maharani E\'20"))
        self.label_4.setText(_translate("CreditWindow", "Tubagus Dylan Rachmat E\'20"))
        self.label_5.setText(_translate("CreditWindow", "Raihan Nagib E\'20"))
        self.close_button.setText(_translate("CreditWindow", "Close"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreditWindow = QtWidgets.QMainWindow()
    ui = Ui_CreditWindow()
    ui.setupUi(CreditWindow)
    CreditWindow.show()
    sys.exit(app.exec_())
