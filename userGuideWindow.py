from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserGuideWindow(object):
    def setupUi(self, UserGuideWindow):
        UserGuideWindow.setObjectName("UserGuideWindow")
        UserGuideWindow.resize(439, 463)
        self.centralwidget = QtWidgets.QWidget(UserGuideWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(130, 30, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: #4F90BD;")
        self.label_1.setObjectName("label_1")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 10, 71, 71))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("image/gambar.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(320, 380, 93, 28))
        self.ok_button.setStyleSheet("QPushButton{\n"
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
        self.ok_button.setObjectName("ok_button")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 140, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #4F90BD;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #4F90BD;")
        self.label_3.setObjectName("label_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 270, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        UserGuideWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UserGuideWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 26))
        self.menubar.setObjectName("menubar")
        UserGuideWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UserGuideWindow)
        self.statusbar.setObjectName("statusbar")
        UserGuideWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UserGuideWindow)
        QtCore.QMetaObject.connectSlotsByName(UserGuideWindow)

    def retranslateUi(self, UserGuideWindow):
        _translate = QtCore.QCoreApplication.translate
        UserGuideWindow.setWindowTitle(_translate("UserGuideWindow", "User Guide"))
        self.label_1.setText(_translate("UserGuideWindow", "Smart Parking App"))
        self.ok_button.setText(_translate("UserGuideWindow", "Ok"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("UserGuideWindow", "1. Tekan Tombil Add Image (jika ada mobil yang masuk)"))
        item = self.listWidget.item(1)
        item.setText(_translate("UserGuideWindow", "2. Tunggu sampai plat nomor terdeteksi"))
        item = self.listWidget.item(2)
        item.setText(_translate("UserGuideWindow", "3. Jika plat terdeteksi, bisa lanjut ke mobil selanjutnya"))
        item = self.listWidget.item(3)
        item.setText(_translate("UserGuideWindow", "4. Jika plat tidak bisa dideteksi, input plat nomor secara manual"))
        item = self.listWidget.item(4)
        item.setText(_translate("UserGuideWindow", "5. Ulangi keempat langkah di atas"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("UserGuideWindow", "Kendaraan Masuk"))
        self.label_3.setText(_translate("UserGuideWindow", "Kendaraan Keluar"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("UserGuideWindow", "1. Tekan tombol add output image (jika ada mobil yang keluar parkir)"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("UserGuideWindow", "2. Tunggu sampai plat terdeteksi sehingga muncul waktu dan harga parkir"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("UserGuideWindow", "3. Jika plat tidak terdeteksi, masukkan plat nomor secara manual"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("UserGuideWindow", "4. Tekan tombol pay, untuk membayar parkir"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("UserGuideWindow", "5. Ulangi keempat langkah di atas"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserGuideWindow = QtWidgets.QMainWindow()
    ui = Ui_UserGuideWindow()
    ui.setupUi(UserGuideWindow)
    UserGuideWindow.show()
    sys.exit(app.exec_())