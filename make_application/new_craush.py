# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SAMSUNG\Desktop\알바\바이크뱅크\program\z_ui\new_craush.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from save_database import *


class New_crush_Ui_Form(object):
    def new_crush_setupUi(self, Form):
        self.msg=QtWidgets.QMessageBox()
        self.udata = upload_db()
        Form.setObjectName("Form")
        Form.resize(1649, 874)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 1611, 841))
        font = QtGui.QFont()
        font.setFamily("a고딕17")
        font.setPointSize(17)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(550, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_2.setGeometry(QtCore.QRect(690, 70, 281, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 150, 511, 671))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(10, 350, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 470, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(10, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 530, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 290, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 410, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 230, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")

        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_5.setGeometry(QtCore.QRect(200, 50, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.comboBox_5.setFont(font)
        self.comboBox_5.addItem("차량번호")
        self.comboBox_5.addItem("차대번호")
        
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(200, 110, 140, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        ###
        #self.lineEdit_11.setValidator(QtGui.QIntValidator(0, 9999999999))
        ###
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 255, 150, 50))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.lineEdit_12 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(200, 170, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_15 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(200, 350, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(200, 410, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(200, 470, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.textEdit_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 530, 301, 131))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(200, 230, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(200, 290, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        ###
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(550, 150, 511, 671))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(15)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 290, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 350, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 410, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 50, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 110, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 230, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 290, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 350, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        ###
        self.lineEdit_9.setValidator(QtGui.QIntValidator(0, 9999999999))
        ###
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(200, 410, 302, 251))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_4.setGeometry(QtCore.QRect(200, 170, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        ###
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_22.setGeometry(QtCore.QRect(20, 680, 150, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setObjectName("lineEdit_22")
        
        self.comboBox_4.currentIndexChanged.connect(self.change_combo_4)
        ###
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(1080, 150, 511, 531))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(15)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(10, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_19.setGeometry(QtCore.QRect(200, 50, 301, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_3.setGeometry(QtCore.QRect(200, 110, 302, 181))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(10, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 300, 491, 221))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 130, 22))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.label_30 = QtWidgets.QLabel(self.groupBox_5)
        self.label_30.setGeometry(QtCore.QRect(20, 90, 61, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 40, 130, 22))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_31 = QtWidgets.QLabel(self.groupBox_5)
        self.label_31.setGeometry(QtCore.QRect(230, 90, 21, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(15)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setGeometry(QtCore.QRect(250, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_32 = QtWidgets.QLabel(self.groupBox_5)
        self.label_32.setGeometry(QtCore.QRect(400, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        self.label_33.setGeometry(QtCore.QRect(20, 160, 61, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit.setGeometry(QtCore.QRect(80, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 160, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        ###
        self.radioButton_2.toggled.connect(self.disable_lineedit)
        self.radioButton.toggled.connect(self.able_lineedit)
        ###
        ###
        self.lineEdit.setValidator(QtGui.QIntValidator(0, 100))
        self.lineEdit_2.setValidator(QtGui.QIntValidator(0, 999999999))
        self.lineEdit.textChanged.connect(self.verse)
        #
        ###
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(1080, 690, 511, 121))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.dateTimeEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateTimeEdit.setGeometry(QtCore.QRect(170, 70, 321, 41))
        
        ###
        now_date = QDate.currentDate()
        self.dateTimeEdit.setDate(now_date.addDays(-1))
        self.dateEdit_2.setDate(now_date)
        ###
        
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(lambda: self.bike_whghl())
        self.pushButton.clicked.connect(lambda: self.bike_enroll())
        #차량차대번호self.lineEdit_11.setText('ddd')
    
    def bike_enroll(self):
        acci_ddr = self.lineEdit_19.text()
        acci_vehicle_number = self.lineEdit_4.text()
        acci_model = self.lineEdit_5.text()
        acci_num = self.lineEdit_7.text()
        acci_charge_name = self.lineEdit_8.text()
        acci_charge_call = self.lineEdit_9.text()
        reception_detail = self.textEdit.toPlainText()
        accident_detail = self.textEdit_3.toPlainText()
        if len(self.lineEdit.text()) !=0 and len(self.lineEdit_2.text())!=0:
            fault = self.lineEdit.text()
            idemnity=self.lineEdit_2.text()
        else:
            fault = 0
            idemnity=0
        accident_date = str(self.dateEdit_2.date().toString('yyyyMMdd'))
        reception_date = str(self.dateTimeEdit.date().toString('yyyyMMdd'))
        if self.comboBox_4.currentIndex()==17:
            insur_com=self.lineEdit_22.text()
        else:
            insur_com = self.comboBox_4.currentText()
        if len(acci_num)!=0 and len(acci_charge_call)!=0:
            if len(accident_detail) <=500 and len(reception_detail) <=500:
                acci_col = ['insur_recept_no', 'insur_com', 'insur_charge_name', 'charge_call', 'reception_detail', 'accident_date', 
                            'reception_date', 'accident_detail', 'accident_addr', 'vehicle_number', 'fault','indemnity']
                acci_dic={'insur_recept_no':[acci_num], 'insur_com':[insur_com], 'insur_charge_name':[acci_charge_name], 
                          'charge_call':[acci_charge_call], 'reception_detail':[reception_detail], 'accident_date':[accident_date], 
                          'reception_date':[reception_date], 'accident_detail':[accident_detail], 'accident_addr':[acci_ddr], 
                          'vehicle_number':[self.lineEdit_12.toPlainText()], 'fault':[fault],'indemnity':[idemnity]}
                acci_table = pd.DataFrame(acci_dic,columns=acci_col)
                try:
                    self.udata.upload_database(acci_table, 'accident_partner')
                    {self.msg.information(QtWidgets.QDialog(), "알림", "신규 사고가 정상적으로 등록되었습니다.")}
                except:
                    {self.msg.information(QtWidgets.QDialog(), "알림", "이미 등록된 접수번호입니다.")}
            else:
                {self.msg.information(QtWidgets.QDialog(), "알림", "사고 경위와 접수내용은 500자를 초과할 수 없습니다.")}
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "보험접수번호와 담당자 전화번호는 반드시 채워야합니다.")}
            
        
    def disable_lineedit(self, enabled):
        if enabled:
            self.textBrowser.clear()
            self.lineEdit.clear()
            self.lineEdit.setDisabled(True)
            self.lineEdit_2.clear()
            self.lineEdit_2.setDisabled(True)
    
    def able_lineedit(self, enabled):
        if enabled:
            self.lineEdit.setDisabled(False)
            self.lineEdit_2.setDisabled(False)

    def change_combo_4(self, value):
        if value == 17:
            self.comboBox_4.setGeometry(QtCore.QRect(200, 170, 120, 41))
            self.lineEdit_22.setGeometry(QtCore.QRect(330, 170, 169, 41))
            #200, 170, 301, 41
        else:
            self.comboBox_4.setGeometry(QtCore.QRect(200, 170, 301, 41))
            self.lineEdit_22.setGeometry(QtCore.QRect(20, 680, 150, 41))
    
    def verse(self):
        self.textBrowser.clear()
        if len(self.lineEdit.text()) >=1:
            self.textBrowser.append(str(100-int(self.lineEdit.text())))
    
    def bike_whghl(self):
        self.lineEdit_12.setText("")
        self.lineEdit_17.setText("")
        self.lineEdit_15.setText("")
        self.lineEdit_16.setText("")
        self.textBrowser_2.setText("")
        self.textBrowser_3.setText("")
        self.textEdit_2.setText("")
        if self.comboBox_5.currentText() == '차대번호':
            valuee = 'vehicle_str'
        elif self.comboBox_5.currentText() =='차량번호':
            valuee='vehicle_number'
        qu = '''select contract_start, contract_end, branch_no, admin_no, lease_aff, model, insur_info, vehicle_str, vehicle_number from lease_contract_info where {}='{}';'''.format(valuee,self.lineEdit_11.text())
        cu = ['contract_start', 'contract_end','branch_no','admin_no', 'lease_aff', 'model', 'insur_info', 'vehicle_str', 'vehicle_number']
        try:
            data_table = self.udata.make_dataframe(qu,cu)
            try:    #본사
                qu = '''select branch_name from bikebank_branch where admin_no={};'''.format(data_table['admin_no'][0])
                cu = ['branch_name']
                branch_table = self.udata.make_dataframe(qu,cu)
                admin_n = branch_table['branch_name'][0]
                lease_aff=data_table['lease_aff'][0]
            except:
                try:    #B2B리스
                    b2b_qq = '''select branch_name from hangang_b2b_branch where branch_no={};'''.format(data_table['branch_no'][0])
                    b2b_cc = ['branch_name']
                    b2b_table = self.udata.make_dataframe(b2b_qq,b2b_cc)
                    admin_n=data_table['lease_aff'][0]
                    lease_aff = b2b_table['branch_name'][0]
                except: #개인리스
                    admin_n='바이크'
                    lease_aff="개인리스" 
            try:
                self.lineEdit_12.setText(data_table['vehicle_number'][0])
                self.lineEdit_17.setText(data_table['vehicle_str'][0])
                self.lineEdit_15.setText(admin_n)
                self.lineEdit_16.setText(lease_aff)
                self.textBrowser_3.append(data_table['insur_info'][0])
                self.textBrowser_2.append(data_table['model'][0])
                self.textEdit_2.append(str(data_table['contract_start'][0]))
                self.textEdit_2.append('~'+str(data_table['contract_end'][0]))
            except:
                {self.msg.information(QtWidgets.QDialog(), "알림", "없는 이륜자동차입니다.")}
        except:
            {self.msg.information(QtWidgets.QDialog(), "알림", "정확한 차량번호를 입력해주십시오.")}


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "신규 사고 등록"))
        self.groupBox.setTitle(_translate("Form", "신규 사고 등록"))
        self.label.setText(_translate("Form", "사고 일자 :"))
        self.label_2.setText(_translate("Form", "접수 일자 :"))
        self.groupBox_2.setTitle(_translate("Form", "사고자"))
        self.label_20.setText(_translate("Form", "관      리      사:"))
        self.label_15.setText(_translate("Form", "차 대        번 호:"))
        self.label_17.setText(_translate("Form", "조              회"))
        self.label_18.setText(_translate("Form", "차 량        번 호:"))
        self.label_13.setText(_translate("Form", "계 약        기 간:"))
        self.label_14.setText(_translate("Form", "보 험       정 보:"))
        self.label_12.setText(_translate("Form", "지               사:"))
        self.label_19.setText(_translate("Form", "차               종:"))
        self.groupBox_3.setTitle(_translate("Form", "상대방"))
        self.label_5.setText(_translate("Form", "차 량       번 호:"))
        self.label_6.setText(_translate("Form", "보       험     사:"))
        self.label_7.setText(_translate("Form", "보 험  접수번호:"))
        self.label_8.setText(_translate("Form", "보 험   담 당 자:"))
        self.label_9.setText(_translate("Form", "차               종:"))
        self.label_10.setText(_translate("Form", "보험담당자번호:"))
        self.label_11.setText(_translate("Form", "접 수        내 용:"))
        self.comboBox_4.setItemText(0, _translate("Form", "DB손해보험"))
        self.comboBox_4.setItemText(1, _translate("Form", "삼성화재"))
        self.comboBox_4.setItemText(2, _translate("Form", "한화손해보험"))
        self.comboBox_4.setItemText(3, _translate("Form", "MG손해보험"))
        self.comboBox_4.setItemText(4, _translate("Form", "KB손해보험"))
        self.comboBox_4.setItemText(5, _translate("Form", "하나손해보험(구)더케이 손해보험"))
        self.comboBox_4.setItemText(6, _translate("Form", "현대해상"))
        self.comboBox_4.setItemText(7, _translate("Form", "메리츠화재"))
        self.comboBox_4.setItemText(8, _translate("Form", "롯데손해보험"))
        self.comboBox_4.setItemText(9, _translate("Form", "악사"))
        self.comboBox_4.setItemText(10, _translate("Form", "흥국생명"))
        self.comboBox_4.setItemText(11, _translate("Form", "NH손해보험"))
        self.comboBox_4.setItemText(12, _translate("Form", "개인택시공제"))
        self.comboBox_4.setItemText(13, _translate("Form", "법인택시공제"))
        self.comboBox_4.setItemText(14, _translate("Form", "화물공제조합"))
        self.comboBox_4.setItemText(15, _translate("Form", "렌터카공제"))
        self.comboBox_4.setItemText(16, _translate("Form", "버스공제"))
        self.comboBox_4.setItemText(17, _translate("Form", "기타 직접입력"))
        self.groupBox_4.setTitle(_translate("Form", "사고경위"))
        self.label_25.setText(_translate("Form", "주               소:"))
        self.label_28.setText(_translate("Form", "사 고       경 위:"))
        self.groupBox_5.setTitle(_translate("Form", "과 실     비 율"))
        self.radioButton.setText(_translate("Form", "협의 완료"))
        self.label_30.setText(_translate("Form", "자차"))
        self.radioButton_2.setText(_translate("Form", "협의 중"))
        self.label_31.setText(_translate("Form", ":"))
        self.label_32.setText(_translate("Form", "상대차"))
        self.label_33.setText(_translate("Form", "면책금"))
        self.pushButton.setText(_translate("Form", "신규 사고 등록"))
        self.pushButton_2.setText(_translate("Form", "이륜자동차 조회"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_crush_Form = QtWidgets.QWidget()
    ui = New_crush_Ui_Form()
    ui.new_crush_setupUi(new_crush_Form)
    new_crush_Form.show()
    sys.exit(app.exec_())
