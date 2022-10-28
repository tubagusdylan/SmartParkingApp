from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from proyek_gui import Ui_MainWindow
from creditWindow import Ui_CreditWindow
from userGuideWindow import Ui_UserGuideWindow
from manualWindow1 import Ui_ManualInputIn
from manualWindow2 import Ui_ManualInputOut
import sys
import lpr
from datetime import datetime
from itertools import islice

# GLobal variabel
dataVehicle = {"License" : [], "Time" : [], "Status" : []}

dataNota = {"outTime" : None, "numberPlate" : None, "parkingTime" : None, "parkingPrice" : None}

# class untuk fungsionalitas button
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Parking App")

        # Tombol add image camera in
        self.ui.add_image_in_button.clicked.connect(self.clickInput)
        # Tombol add image camera out
        self.ui.add_image_out_buttom.clicked.connect(self.clickOutput)

        # Tombol pay
        self.ui.pay_button.clicked.connect(self.clicked_pay_button)

        # Menu Credit
        self.ui.actionCredits.triggered.connect(self.show_credit_window)
        # Menu User Guide
        self.ui.actionUser_Guide_2.triggered.connect(self.show_userGuide_window)
        # Menu Manual Input In
        self.ui.actionManual_Input_In.triggered.connect(self.show_manualInputIn_window)
        # Menu Manual Input Out
        self.ui.actionManual_Input_Out.triggered.connect(self.show_manualInputOut_window)


    # =======================================UNTUK TOMBOL INPUT======================================
    # ================== Untuk Save Data ==========================
    def saveData(self, platNumber, dateTime, status):
        self.numPlate = platNumber
        self.dt = dateTime
        self.st = status

        # Memasukkan data ke sebvuah dictionary
        dataVehicle["License"].append(self.numPlate)
        dataVehicle["Time"].append(self.dt)
        dataVehicle["Status"].append(self.st)
        # print(f"{dataVehicle}")
    
    def Data(self, platNumber, dateTime, status):       
        self.saveData(platNumber, dateTime, status)
    # ================= Akhir dari Save Data =======================

    # ================ Fungsi mengambil waktu saat ini =======================
    def get_current_time(self):
        # curr_time = datetime.strftime("%H:%M:%S", datetime.now())
        curr_time = datetime.now()

        return curr_time.strftime("%H:%M:%S")
    # ================ Akhir dari fungsi mengambil waktu saat ini =============

    # Fungsi untuk button input image
    def clickInput(self):
        # Ini diganti dulu directorynya ya
        fname = QFileDialog.getOpenFileName(self, "Open File", ".\\sample_images", "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")
        print(fname)
        # Open the sampe-images
        self.pixmap = QPixmap(fname[0])
        # Add pic to label
        self.ui.input_image.setPixmap(self.pixmap)

        # setelah file terpilih, jalankan LPR
        # Mendapatkan plat nomor yang terdeteksi oleh LPR
        hasil = lpr.extract_platenumber(fname[0])
        waktu = self.get_current_time()
        status = "IN"

        if hasil == None:
            # Jalankan fungsi warning (plat nomor tidak dapat dideteksi)
            self.warning_numplate()
        else:
            self.Data(hasil, waktu, status)
            self.tableLoadData()

    
    def tableLoadData(self):
        row = 0
        # Menentukan batas row, jadi ga infinity loop
        self.ui.data_table.setRowCount(len(dataVehicle["License"]))

        # Loop buat masukin ke table bagian license
        for vehicle in dataVehicle["License"]:
            item = QTableWidgetItem(vehicle)
            self.ui.data_table.setItem(row, 0, item)
            # print(vehicle)
            row = row+1
        
        row = 0
        # Loop buat masukin ke table bagian Time
        for vehicle in dataVehicle["Time"]:
            item = QTableWidgetItem(vehicle)
            self.ui.data_table.setItem(row, 1, item)
            # print(vehicle)
            row = row+1
        
        row = 0
        # Loop buat masukin ke table bagian Status
        for vehicle in dataVehicle["Status"]:
            item = QTableWidgetItem(vehicle)
            self.ui.data_table.setItem(row, 2, item)
            # print(vehicle)
            row = row+1

    def findIndexOfTableToDelete(self):   

        row = 0
        # Loop untuk mencari data plat nomor kendaraan yang ada dengan data plat nomor kendaraan yang kelaur
        for vehicle in dataVehicle["License"]:
            if vehicle == dataNota["numberPlate"]:
                index = row
            row = row + 1

        self.deleteRowInTable(index)


    
    def deleteRowInTable(self, baris):
        # Menghapus satu baris penuh untuk data kendaraan yang keluar pada tabel 
        self.ui.data_table.removeRow(baris)
        
        # Menghapus data "License", "Time", dan "Status" kendaraan yang keluar pada dictionary
        del dataVehicle["License"][baris]
        del dataVehicle["Time"][baris]
        del dataVehicle["Status"][baris]

        # Mengembalikan "dataNota" menjadi None semua sehingga perulangan proses pembayaran dapat dilakukan dengan sesuai
        dataNota["outTime"] = None
        dataNota["numberPlate"] = None
        dataNota["parkingTime"] = None
        dataNota["parkingPrice"] = None
        


          
    # ===========================UNTUK TOMBOL INPUT=============================================================

    # ===========================UNTUK TOMBOL OUT===============================================================
    # Fungsi untuk button ouput image
    def clickOutput(self):
        # Ini diganti dulu directorynya yaa
        fname = QFileDialog.getOpenFileName(self, "Open File", ".\\sample_images", "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")

        # Open the image
        self.pixmap = QPixmap(fname[0])
        # Add pic to label
        self.ui.output_image.setPixmap(self.pixmap)

        # Setelah file terpilih, jalankan LPR
        # Mendapatkan plat nomor yang terdeteksi oleh LPR
        hasil_out = lpr.extract_platenumber(fname[0])
        waktu_out = self.get_current_time()
        # status_out = "OUT"

        if hasil_out == None:
            # Jalankan fungsi warning (plat nomor tidak dapat dideteksi)
            self.warning_numplate()
        else:
            # Cek apakah kendaraan yang ingin keluar, terdaftar di databse tempat parkit atau tidak
            isAvail = self.checkingNumPlate(hasil_out)
            if isAvail == -1:
                # buat window baru
                self.warning_popup()
            else:
                # Jalankan fungsi setParkingTime dan setPricing
                waktu_parkir = self.setParkingTime(waktu_out, isAvail)
                hh, mm, ss = waktu_parkir.split(':')
                parking_time_in_sec = int(hh) * 3600 + int(mm) * 60 + int(ss)
                harga_parkir = self.setPricing(parking_time_in_sec)
                self.saveDataNota(waktu_out, hasil_out, waktu_parkir, harga_parkir)
        
            
    # Fungsi untuk mengecek apakah plat nomor yang ingin keluar dari area parkir terdaftar di database atau tidak
    def checkingNumPlate(self, platNumber):
        i = 0
        for licenseNum in dataVehicle["License"]:
            if platNumber == licenseNum:
                print("Kendaraan ditemukan")
                return i    
            i = i+1
        return -1

    # Fungsi untuk memberi tahu berapa lama kendaraan parkir
    def setParkingTime(self, dateTime, index):
        # Waktu pas keluar parkir
        dateTime_out = datetime.strptime(dateTime, "%H:%M:%S")
        # Waktu pas masuk parkir
        dateTime_in = datetime.strptime(dataVehicle["Time"][index], "%H:%M:%S")
        parking_time = str(dateTime_out - dateTime_in)
        # Cetak waktu parkir ke GUI
        self.ui.hasil_waktu.setText("0" + parking_time)

        return ("0" + parking_time)

    # Fungsi untuk menentukan harga parkir
    def setPricing(self, parkingTime):
        price = str(parkingTime * 1)
        self.ui.hasil_biaya.setText("Rp" + price)
        return ("Rp"+ price)

    def warning_popup(self):
        # membuat popup window menggunakan qmessagebox
        msg = QMessageBox()
        msg.setWindowTitle("Informasi Kendaraan")
        msg.setText("Kendaraan Tidak Ditemukan!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText("Kendaraan yang ingin keluar dari tempat parkir, sebelumnya tidak terdaftar di database")

        msg.exec_()

    # =============================UNTUK TOMBOL OUT=============================================================
    # =============================UNTUK TOMBOL PAY=============================================================
    def saveDataNota(self, jam_keluar, plat_kendaraan, lama_parkir, harga_parkir):
        self.jam_keluar = jam_keluar
        self.plat_kendaraan = plat_kendaraan
        self.lama_parkir = lama_parkir
        self.harga_parkir = harga_parkir

        dataNota["outTime"] = self.jam_keluar
        dataNota["numberPlate"] = self.plat_kendaraan
        dataNota["parkingTime"] = self.lama_parkir
        dataNota["parkingPrice"] = self.harga_parkir


    def clicked_pay_button(self):
        if dataNota["numberPlate"] is not None:
            self.ui.hasil_waktu.setText("00:00:00")
            self.ui.hasil_biaya.setText("Rp0")

            # Mengganti gambar pada label "Kendaraan Keluar" menjadi default (berwarna putih) setelah pembayaran selesai dilakukan
            self.pixmap = QPixmap()
            self.ui.output_image.setPixmap(self.pixmap)

            self.nota_pembayaran()

        else:
            self.warning_pembayaran()


    # =============================UNTUK TOMBOL PAY=============================================================
    # ============================Nota Pembayaran==============================================================
    def nota_pembayaran(self):
        # membuat popup window menggunakan qmessagebox
        msg = QMessageBox()
        msg.setWindowTitle("Nota Pembayaran Kendaraan Parkir")
        msg.setText("Biaya Parkir Kendaraan telah dibayar")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText(f"Plat Kendaraan : {dataNota['numberPlate']}\nWaktu Parkir : {dataNota['parkingTime']}\nHarga Parkir : {dataNota['parkingPrice']}\nJam Keluar Parkir : {dataNota['outTime']}")

        msg.exec_()

        self.findIndexOfTableToDelete()
    
    def warning_pembayaran(self):
        msg = QMessageBox()
        msg.setWindowTitle("Informasi Nota Pembayaran")
        msg.setText("Belum ada kendaraan keluar yang terdeteksi")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText("Harus ada plat nomor kendaraan yang keluar dari tempat parkir yang terdeteksi sehingga pembayaran dapat dilakukan")

        msg.exec_()
    # ============================Nota Pembayaran==============================================================

    # =============================Pop OUT Warning, plat tidak dapat ditekesi======================================
    def warning_numplate(self):
        # membuat warning dengan qmessagebox
        msg = QMessageBox()
        msg.setWindowTitle("Informasi Plat Nomor")
        msg.setText("Plat Nomor Tidak Dapat Dideteksi!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText("Plat Nomor tidak dapat dideteksi, silakan masukkan plat nomor secara manual!")

        msg.exec_()
    # =============================Pop OUT Warning, plat tidak dapat ditekesi======================================

    # =============================Window Credit=======================================
    def show_credit_window(self):
        self.window = QMainWindow()
        self.uiCredit = Ui_CreditWindow()
        self.uiCredit.setupUi(self.window)
        self.window.show()

        self.uiCredit.close_button.clicked.connect(self.clicked_close)

    def clicked_close(self):
        self.window.close()
    # =============================Window Credit=======================================
    # =============================Window User Guide===================================
    def show_userGuide_window(self):
        self.window = QMainWindow()
        self.uiUserGuide = Ui_UserGuideWindow()
        self.uiUserGuide.setupUi(self.window)
        self.window.show()

        self.uiUserGuide.ok_button.clicked.connect(self.clicked_ok)
    
    def clicked_ok(self):
        self.window.close()
    # =============================Window User Guide===================================
    # ============================Window Manual Input In==================================
    def show_manualInputIn_window(self):
        self.window = QMainWindow()
        self.uiManualInputIn = Ui_ManualInputIn()
        self.uiManualInputIn.setupUi(self.window)
        self.window.show()

        self.uiManualInputIn.save_button.clicked.connect(self.clicked_save1)
    
    def clicked_save1(self):
        # Memasukkan setiap yang ditulis ke variabel (ketika tombol save ditekan)
        value = self.uiManualInputIn.lineEdit.text()
        
        if value == "":
            self.warning_input()
        else:
            waktu = self.get_current_time()
            status = "IN"

            self.Data(value, waktu, status)
            self.tableLoadData()
            self.uiManualInputIn.lineEdit.setText("")
    
    # ============================Window Manual Input In==================================
    # ============================Window Manual Input Out==================================
    def show_manualInputOut_window(self):
        self.window = QMainWindow()
        self.uiManualInputOut = Ui_ManualInputOut()
        self.uiManualInputOut.setupUi(self.window)
        self.window.show()

        self.uiManualInputOut.save_button.clicked.connect(self.clicked_save2)

    def clicked_save2(self):
        value = self.uiManualInputOut.lineEdit.text()

        if value == "":
            self.warning_input()
        else:
            waktu = self.get_current_time()
            # status = "OUT"

            isAvail = self.checkingNumPlate(value)
            if isAvail == -1:
                # buat window baru
                self.warning_popup()
            else:
                # Jalankan fungsi setParkingTime dan setPricing
                waktu_parkir = self.setParkingTime(waktu, isAvail)
                hh, mm, ss = waktu_parkir.split(':')
                parking_time_in_sec = int(hh) * 3600 + int(mm) * 60 + int(ss)
                harga_parkir = self.setPricing(parking_time_in_sec)
                self.saveDataNota(waktu, value, waktu_parkir, harga_parkir)

            self.uiManualInputOut.lineEdit.setText("")
    # ============================Window Manual Input Out==================================

    def warning_input(self):
        msg = QMessageBox()
        msg.setWindowTitle("Informasi Plat Nomor")
        msg.setText("Input tidak boleh kosong")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
