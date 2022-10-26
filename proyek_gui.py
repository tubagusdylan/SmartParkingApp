from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 796)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1291, 111))
        self.widget.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.title_project = QtWidgets.QLabel(self.widget)
        self.title_project.setGeometry(QtCore.QRect(0, 0, 1291, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 144, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.title_project.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_project.setFont(font)
        self.title_project.setStyleSheet("color:#4F90BD;\n"
"font: 25pt \"Swis721 Blk BT\";")
        self.title_project.setAlignment(QtCore.Qt.AlignCenter)
        self.title_project.setObjectName("title_project")
        self.animation = QtWidgets.QLabel(self.widget)
        self.animation.setGeometry(QtCore.QRect(20, 0, 131, 101))
        self.animation.setText("")
        self.animation.setPixmap(QtGui.QPixmap("image/gambar.png"))
        self.animation.setScaledContents(True)
        self.animation.setObjectName("animation")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QtCore.QRect(0, 110, 1291, 641))
        self.widget_2.setStyleSheet("background-color:#4F90BD;")
        self.widget_2.setObjectName("widget_2")
        self.output_image = QtWidgets.QLabel(self.widget_2)
        self.output_image.setGeometry(QtCore.QRect(710, 80, 480, 250))
        self.output_image.setStyleSheet("background-color:white;")
        self.output_image.setText("")
        self.output_image.setObjectName("output_image")
        self.input_image = QtWidgets.QLabel(self.widget_2)
        self.input_image.setGeometry(QtCore.QRect(100, 80, 480, 250))
        self.input_image.setStyleSheet("background-color:white;")
        self.input_image.setText("")
        self.input_image.setAlignment(QtCore.Qt.AlignCenter)
        self.input_image.setObjectName("input_image")
        self.title_in = QtWidgets.QLabel(self.widget_2)
        self.title_in.setGeometry(QtCore.QRect(100, 20, 481, 51))
        self.title_in.setStyleSheet("color:white;\n"
"font: 15pt \"Swis721 Blk BT\";")
        self.title_in.setAlignment(QtCore.Qt.AlignCenter)
        self.title_in.setObjectName("title_in")
        self.title_out = QtWidgets.QLabel(self.widget_2)
        self.title_out.setGeometry(QtCore.QRect(710, 20, 481, 51))
        self.title_out.setStyleSheet("color:white;\n"
"font: 15pt \"Swis721 Blk BT\";")
        self.title_out.setAlignment(QtCore.Qt.AlignCenter)
        self.title_out.setObjectName("title_out")
        self.add_image_in_button = QtWidgets.QPushButton(self.widget_2)
        self.add_image_in_button.setGeometry(QtCore.QRect(270, 340, 151, 51))
        self.add_image_in_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_image_in_button.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    color:#4f90bd;\n"
"    border-radius: 20px;\n"
"    font: 18px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#4f90bd;\n"
"    color:white;\n"
"    border: 2px solid white;\n"
"}\n"
"")
        self.add_image_in_button.setObjectName("add_image_in_button")
        self.data_table = QtWidgets.QTableWidget(self.widget_2)
        self.data_table.setGeometry(QtCore.QRect(10, 410, 731, 211))
        self.data_table.setMinimumSize(QtCore.QSize(731, 0))
        self.data_table.setStyleSheet("background-color:white;\n"
"color:black;")
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(3)
        self.data_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setItem(0, 0, item)
        self.hasil_biaya = QtWidgets.QLabel(self.widget_2)
        self.hasil_biaya.setGeometry(QtCore.QRect(1040, 500, 241, 51))
        self.hasil_biaya.setStyleSheet("color:white;\n"
"font: 15pt \"Swis721 Blk BT\";")
        self.hasil_biaya.setAlignment(QtCore.Qt.AlignCenter)
        self.hasil_biaya.setObjectName("hasil_biaya")
        self.biaya = QtWidgets.QLabel(self.widget_2)
        self.biaya.setGeometry(QtCore.QRect(760, 500, 241, 51))
        self.biaya.setStyleSheet("color:white;\n"
"font: 15pt \"Swis721 Blk BT\";")
        self.biaya.setAlignment(QtCore.Qt.AlignCenter)
        self.biaya.setObjectName("biaya")
        self.waktu = QtWidgets.QLabel(self.widget_2)
        self.waktu.setGeometry(QtCore.QRect(770, 430, 231, 51))
        self.waktu.setStyleSheet("color:white;\n"
"font: 15pt \"Swis721 Blk BT\";")
        self.waktu.setAlignment(QtCore.Qt.AlignCenter)
        self.waktu.setObjectName("waktu")
        self.hasil_waktu = QtWidgets.QLabel(self.widget_2)
        self.hasil_waktu.setGeometry(QtCore.QRect(1040, 430, 241, 51))
        self.hasil_waktu.setStyleSheet("color:white;\n"
"font: 15pt \"Swis721 Blk BT\";")
        self.hasil_waktu.setAlignment(QtCore.Qt.AlignCenter)
        self.hasil_waktu.setObjectName("hasil_waktu")
        self.pay_button = QtWidgets.QPushButton(self.widget_2)
        self.pay_button.setGeometry(QtCore.QRect(800, 570, 451, 51))
        self.pay_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pay_button.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    color:#4f90bd;\n"
"    border-radius: 20px;\n"
"    font: 22px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#4f90bd;\n"
"    color:white;\n"
"    border: 2px solid white;\n"
"}\n"
"")
        self.pay_button.setObjectName("pay_button")
        self.add_image_out_buttom = QtWidgets.QPushButton(self.widget_2)
        self.add_image_out_buttom.setGeometry(QtCore.QRect(890, 340, 151, 51))
        self.add_image_out_buttom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_image_out_buttom.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    color:#4f90bd;\n"
"    border-radius: 20px;\n"
"    font: 18px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#4f90bd;\n"
"    color:white;\n"
"    border: 2px solid white;\n"
"}\n"
"")
        self.add_image_out_buttom.setObjectName("add_image_out_buttom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1292, 26))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menu_Manual_Input = QtWidgets.QMenu(self.menubar)
        self.menu_Manual_Input.setStyleSheet("QMenu{\n"
"    background-color: #4F90BD;\n"
"}")
        self.menu_Manual_Input.setObjectName("menu_Manual_Input")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setStyleSheet("QMenu{\n"
"    background-color: #4F90BD;\n"
"}")
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionManual_Input_In = QtWidgets.QAction(MainWindow)
        self.actionManual_Input_In.setObjectName("actionManual_Input_In")
        self.actionManual_Input_Out = QtWidgets.QAction(MainWindow)
        self.actionManual_Input_Out.setObjectName("actionManual_Input_Out")
        self.actionUser_Guide = QtWidgets.QAction(MainWindow)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionUser_Guide_2 = QtWidgets.QAction(MainWindow)
        self.actionUser_Guide_2.setObjectName("actionUser_Guide_2")
        self.menu_Manual_Input.addAction(self.actionManual_Input_In)
        self.menu_Manual_Input.addAction(self.actionManual_Input_Out)
        self.menu_Manual_Input.addSeparator()
        self.menu_Help.addAction(self.actionUser_Guide_2)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionCredits)
        self.menubar.addAction(self.menu_Manual_Input.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_project.setText(_translate("MainWindow", "Automatic Parking System"))
        self.title_in.setText(_translate("MainWindow", "CAMERA IN "))
        self.title_out.setText(_translate("MainWindow", "CAMERA OUT"))
        self.add_image_in_button.setText(_translate("MainWindow", "Add Image"))
        item = self.data_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "License Number"))
        item = self.data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date & Time"))
        item = self.data_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        __sortingEnabled = self.data_table.isSortingEnabled()
        self.data_table.setSortingEnabled(False)
        item = self.data_table.item(0, 0)
        item.setText(_translate("MainWindow", "P 2834 JB"))
        self.data_table.setSortingEnabled(__sortingEnabled)
        self.hasil_biaya.setText(_translate("MainWindow", "Rp0"))
        self.biaya.setText(_translate("MainWindow", "BIAYA"))
        self.waktu.setText(_translate("MainWindow", "WAKTU"))
        self.hasil_waktu.setText(_translate("MainWindow", "00:00:00"))
        self.pay_button.setText(_translate("MainWindow", "PAY"))
        self.add_image_out_buttom.setText(_translate("MainWindow", "Add Image"))
        self.menu_Manual_Input.setTitle(_translate("MainWindow", "Manual Input"))
        self.menu_Help.setTitle(_translate("MainWindow", "Help"))
        self.actionManual_Input_In.setText(_translate("MainWindow", "Manual Input In"))
        self.actionManual_Input_Out.setText(_translate("MainWindow", "Manual Input Out"))
        self.actionUser_Guide.setText(_translate("MainWindow", "User Guide"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionUser_Guide_2.setText(_translate("MainWindow", "User Guide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
