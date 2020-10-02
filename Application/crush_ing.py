# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *

from insurance_call import *
from real_send_mail import *
from get_excel import *
from save_database import *
from save_firebase import *
import pymysql

class Opne_crush_ing:
    def open_insurance_call(self, accident):
        self.insurance_call_Form = QtWidgets.QWidget()
        self.insurance_call_ui = insurance_call_Ui_Form()
        self.insurance_call_ui.insurance_call_setupUi(self.insurance_call_Form, accident)
        self.insurance_call_Form.show()
    
    def open_real_send_mail(self, accident):
        self.real_send_mail_Form = QtWidgets.QWidget()
        self.real_send_mail_ui = real_send_mail_Ui_Form()
        self.real_send_mail_ui.real_send_mail_setupUi(self.real_send_mail_Form, accident)
        self.real_send_mail_Form.show()

class crush_ing_Ui_Form(object):
    def crush_ing_setupUi(self, Form):
        self.udata = upload_db()
        Form.setObjectName("Form")
        Form.resize(1916, 944)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 731, 851))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 711, 721))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(520, 50, 201, 61))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(170, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 70, 112, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(760, 80, 1141, 851))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 800, 221, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 800, 221, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(360, 40, 761, 81))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 321, 81))
        font.setFamily("a고딕15")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 360, 361, 431))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 181, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 181, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 181, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 330, 231, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 280, 261, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 280, 71, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        
        ###
        self.pushButton_7.clicked.connect(lambda: self.upload_mail())
        ###        
        
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 370, 341, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(190, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_5.setGeometry(QtCore.QRect(190, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_6.setGeometry(QtCore.QRect(190, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_7.setGeometry(QtCore.QRect(190, 190, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 360, 371, 431))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 40, 351, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(11)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 100, 351, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(11)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 160, 351, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(11)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 220, 171, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(11)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 290, 351, 101))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(13)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_17.setGeometry(QtCore.QRect(190, 220, 171, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(11)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_17.setObjectName("pushButton_17")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(760, 360, 371, 431))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 290, 351, 101))
        font = QtGui.QFont()
        font.setFamily("a고딕14")
        font.setPointSize(13)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setObjectName("pushButton_6")

        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_5)
        self.dateEdit.setGeometry(QtCore.QRect(10, 80, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        ###
        now_date = QDate.currentDate()
        self.dateEdit.setDate(now_date)
        ###
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(10, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(10, 220, 131, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.textBrowser_8 = QtWidgets.QLineEdit(self.groupBox_5)
        self.textBrowser_8.setGeometry(QtCore.QRect(150, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(13)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 170, 211, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 220, 211, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 140, 1101, 201))
        self.groupBox_6.setObjectName("groupBox_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 40, 171, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_3.setGeometry(QtCore.QRect(660, 70, 431, 121))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(660, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(20, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(390, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.textBrowser_9 = QtWidgets.QLineEdit(self.groupBox_6)
        self.textBrowser_9.setGeometry(QtCore.QRect(20, 140, 141, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setObjectName("textBrowser_9")
        
        self.textBrowser_11 = QtWidgets.QLineEdit(self.groupBox_6)
        self.textBrowser_11.setGeometry(QtCore.QRect(390, 140, 231, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_11.setFont(font)
        self.textBrowser_11.setObjectName("textBrowser_11")
        
        ###
        self.textBrowser_9.setValidator(QtGui.QIntValidator(0, 100))
        self.textBrowser_11.setValidator(QtGui.QIntValidator(0, 999999999))
        self.textBrowser_9.textChanged.connect(self.verse)
        ###
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_10.setGeometry(QtCore.QRect(200, 140, 141, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser_10.setFont(font)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(170, 140, 16, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕11")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 481, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕17")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(200, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_12.setObjectName("pushButton_12")
        
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(480, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_13.setObjectName("pushButton_13")
        
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(230, 40, 91, 22))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 40, 130, 22))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        
        acci_query='''select insur_recept_no,insur_com,reception_date,is_close,vehicle_number,fault,get_pay,pay_bank,estim_pay,indemnity from accident_partner'''
        acci_col = ['insur_recept_no', 'insur_com','reception_date','is_close', 'vehicle_number', 'fault','get_pay','pay_bank','estim_pay','indemnity']
        acci_df = self.udata.make_dataframe(acci_query,acci_col)
        self.tableWidget.setRowCount(len(acci_df))
        for idx in range(len(acci_df)):
            if acci_df['is_close'][idx] == '종결':
                closee = '종결'
            else:
                closee='미종결'
            if np.isnan(acci_df['indemnity'][idx])==False:
                indemnity=str(acci_df['indemnity'][idx]).split('.')[0]
            else:
                indemnity=str('')
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(str(acci_df['reception_date'][idx])))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(acci_df['vehicle_number'][idx]))
            self.tableWidget.setItem(idx, 2, QTableWidgetItem(acci_df['fault'][idx]))
            self.tableWidget.setItem(idx, 3, QTableWidgetItem(indemnity))
            self.tableWidget.setItem(idx, 4, QTableWidgetItem(acci_df['insur_com'][idx]))
            self.tableWidget.setItem(idx, 5, QTableWidgetItem(acci_df['insur_recept_no'][idx]))
            self.tableWidget.setItem(idx, 6, QTableWidgetItem(closee))
            self.tableWidget.setItem(idx, 7, QTableWidgetItem(str(acci_df['estim_pay'][idx]).split('.')[0]))
            self.tableWidget.setItem(idx, 8, QTableWidgetItem(str(acci_df['get_pay'][idx]).split('.')[0]))
            self.tableWidget.setItem(idx, 9, QTableWidgetItem(acci_df['pay_bank'][idx]))
        self.msg=QtWidgets.QMessageBox()
        ###
        ###
        self.pushButton_2.clicked.connect(lambda: self.whghl())
        self.pushButton.clicked.connect(lambda: self.select_acci_manage())
        self.pushButton_8.clicked.connect(lambda: self.run_insurance_call(self.textBrowser_5.toPlainText()))
        self.pushButton_9.clicked.connect(lambda: self.acci_pic_load())
        self.pushButton_10.clicked.connect(lambda: self.repair_pic_load())
        self.pushButton_11.clicked.connect(lambda: self.estimate_load())
        self.pushButton_15.clicked.connect(lambda: self.certificate_load())
        self.pushButton_16.clicked.connect(lambda: self.run_real_send_mail())
        self.pushButton_17.clicked.connect(lambda: self.bb_load())
        self.pushButton_6.clicked.connect(lambda: self.acci_end())
        self.pushButton_4.clicked.connect(lambda: self.get_excell())
        self.pushButton_3.clicked.connect(lambda: self.delete_acci())
        self.pushButton_12.clicked.connect(lambda: self.update_fault())
        self.pushButton_13.clicked.connect(lambda: self.update_idemnity())
        self.yearr = str(QDate.currentDate().year())
        self.lineEdit_3.setValidator(QtGui.QIntValidator(0, 9999999999))
        self.textBrowser_8.setValidator(QtGui.QIntValidator(0, 9999999999))
        self.textBrowser_9.setValidator(QtGui.QIntValidator(0, 100))
        ###
        ###
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def update_idemnity(self):
        if len(self.textBrowser_5.toPlainText())!=0:
            idemnity = self.textBrowser_11.text()
            if len(idemnity) !=0:
                cpnn = pymysql.connect(host='', port=3306, user='', passwd='', db='')
                curs = cpnn.cursor()
                curs.execute('update accident_partner set indemnity="{}" where insur_recept_no="{}";'.format(idemnity, self.textBrowser_5.toPlainText()))
                cpnn.commit()
                cpnn.close()
                {self.msg.information(QtWidgets.QDialog(), "알림", "면책금이 등록되었습니다.")}
            else:
                {self.msg.information(QtWidgets.QDialog(), "알림", "면책금을 입력 후 클릭해주세요.")}    
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 클릭해주세요.")}
            
    def update_fault(self):
        if len(self.textBrowser_5.toPlainText())!=0:
            faults = self.textBrowser_9.text()
            if len(faults) !=0:
                cpnn = pymysql.connect(host='', port=3306, user='', passwd='', db='')
                curs = cpnn.cursor()
                curs.execute('update accident_partner set fault="{}" where insur_recept_no="{}";'.format(faults, self.textBrowser_5.toPlainText()))
                cpnn.commit()
                cpnn.close()
                {self.msg.information(QtWidgets.QDialog(), "알림", "과실이 등록되었습니다.")}
            else:
                {self.msg.information(QtWidgets.QDialog(), "알림", "과실을 입력 후 클릭해주세요.")}    
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 클릭해주세요.")}
            
    def delete_acci(self):
        if len(self.textBrowser_5.toPlainText())!=0:
            result = self.msg.information(QtWidgets.QDialog(), '알림', "삭제하시면 다시 복구되지 않습니다.\n삭제를 진행하시겠습니까?", self.msg.Yes | self.msg.No, self.msg.No)
            if result == self.msg.Yes:
                delete_list_qq = 'select estimate, acci_pictures, repair_pictures, certificate, bankbook from document_send_breakdown where insure_recept_no="{}"'.format(self.textBrowser_5.toPlainText())
                delete_list_col=['estimate', 'acci_pictures', 'repair_pictures', 'certificate', 'bankbook']
                delete_df = self.udata.make_dataframe(delete_list_qq, delete_list_col)
                try:
                    cpnn = pymysql.connect(host='', port=3306, user='', passwd='', db='')
                    curs = cpnn.cursor()
                    curs.execute('delete from accident_partner where insur_recept_no="{}";'.format(self.textBrowser_5.toPlainText()))
                    cpnn.commit()
                    cpnn.close()
                    try:
                        delete_list=[delete_df['estimate'][0],delete_df['acci_pictures'][0],delete_df['repair_pictures'][0],
                             delete_df['certificate'][0],delete_df['bankbook'][0]]
                        ff= upload_firebase()
                        ff.firebase_delete(delete_list)
                        {self.msg.information(QtWidgets.QDialog(), "알림", "{} 사고정보가 삭제되었습니다.".format(self.textBrowser_5.toPlainText()))}
                    except:
                        {self.msg.information(QtWidgets.QDialog(), "알림", "{} 사고정보가 삭제되었습니다.".format(self.textBrowser_5.toPlainText()))}
                except:
                    {self.msg.information(QtWidgets.QDialog(), "알림", "이미 삭제된 사고정보입니다.")}
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 클릭해주세요.")}
    
    def get_excell(self):
        if len(self.textBrowser_5.toPlainText())!=0:
            try:
                {self.msg.information(QtWidgets.QDialog(), "알림", "사고처리내역서를 저장할 위치를 선택해주세요.")}
                save_pathh=str(QFileDialog.getExistingDirectory(None, "Select Directory"))
                aa = self.textBrowser_5.toPlainText()
                self.gg = get_excel()
                self.gg.get_acci_excel(save_pathh, aa)
                {self.msg.information(QtWidgets.QDialog(), "알림", "선택하신 파일에 사고처리내역서를 저장했습니다.\n파일을 확인해주세요.")}
            except:
                {self.msg.information(QtWidgets.QDialog(), "알림", "저장할 위치가 선택되지 않았습니다.")}
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 클릭해주세요.")}

    def acci_end(self):
        if len(self.textBrowser_5.toPlainText())!=0:
            get_pay = self.lineEdit_3.text()
            pay_bank = self.lineEdit_4.text()
            estim_pay =self.textBrowser_8.text()
            if len(get_pay)!=0 and len(pay_bank) and len(estim_pay):
                cpnn = pymysql.connect(host='', port=3306, user='', passwd='', db='')
                curs = cpnn.cursor()
                curs.execute('update accident_partner set get_pay="{2}", pay_bank="{3}", estim_pay={4}, repair_date="{0}",is_close="종결" where insur_recept_no="{1}";'.format(self.dateEdit.date().toString('yyyyMMdd'), self.textBrowser_5.toPlainText(),
                                                                                                                                                                      get_pay, pay_bank, estim_pay))
                cpnn.commit()
                cpnn.close()
                {self.msg.information(QtWidgets.QDialog(), "알림", "사고가 종결되었습니다.")}
            else:
                {self.msg.information(QtWidgets.QDialog(), "알림", "빈 칸을 채워주세요")}
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 클릭해주세요.")}

    def whghl(self):
        self.tableWidget.setRowCount(0)
        if len(self.lineEdit.text()) == 0:
            {self.msg.information(QtWidgets.QDialog(), "알림", "빈 칸을 채워주세요")}
        else:
            try:
                if self.comboBox.currentText() =='종결 여부' and self.lineEdit.text() == '미종결':
                    d_acci_query='''select insur_recept_no,insur_com,reception_date,is_close,vehicle_number,fault,get_pay,pay_bank,estim_pay,indemnity from accident_partner where is_close is null'''
                else:
                    if self.comboBox.currentText() == '차량번호':
                        ww = 'vehicle_number'
                    if self.comboBox.currentText() == '보험사접수번호':
                        ww = 'insur_recept_no'
                    if self.comboBox.currentText() == '종결 여부':
                        ww = 'is_close'
                    d_acci_query='''select insur_recept_no,insur_com,reception_date,is_close,vehicle_number,fault,get_pay,pay_bank,estim_pay,indemnity from accident_partner where {} = "{}"'''.format(ww, self.lineEdit.text())
                d_acci_col = ['insur_recept_no', 'insur_com','reception_date','is_close', 'vehicle_number', 'fault','get_pay','pay_bank','estim_pay','indemnity']
                d_acci_df = self.udata.make_dataframe(d_acci_query,d_acci_col)
                if d_acci_df['is_close'][0] == '종결':
                    closee = '종결'
                else:
                    closee='미종결'
                self.tableWidget.setRowCount(len(d_acci_df))
                for idx in range(len(d_acci_df)):
                    self.tableWidget.setItem(idx, 0, QTableWidgetItem(str(d_acci_df['reception_date'][idx])))
                    self.tableWidget.setItem(idx, 1, QTableWidgetItem(d_acci_df['vehicle_number'][idx]))
                    self.tableWidget.setItem(idx, 2, QTableWidgetItem(d_acci_df['fault'][idx]))
                    self.tableWidget.setItem(idx, 3, QTableWidgetItem(str(d_acci_df['indemnity'][idx])))
                    self.tableWidget.setItem(idx, 4, QTableWidgetItem(d_acci_df['insur_com'][idx]))
                    self.tableWidget.setItem(idx, 5, QTableWidgetItem(d_acci_df['insur_recept_no'][idx]))
                    self.tableWidget.setItem(idx, 6, QTableWidgetItem(closee))
                    self.tableWidget.setItem(idx, 7, QTableWidgetItem(str(d_acci_df['estim_pay'][idx])))
                    self.tableWidget.setItem(idx, 8, QTableWidgetItem(str(d_acci_df['get_pay'][idx])))
                    self.tableWidget.setItem(idx, 9, QTableWidgetItem(d_acci_df['pay_bank'][idx]))
                    if self.radioButton_2.isChecked():
                        self.tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)
                    elif self.radioButton.isChecked():
                        self.tableWidget.sortItems(0, QtCore.Qt.DescendingOrder)   
            except:
                self.tableWidget.setRowCount(0)
                {self.msg.information(QtWidgets.QDialog(), "알림", "없는 사고 이력입니다.")}
        
    def select_acci_manage(self):
        d_acci_query='''select * from accident_partner where insur_recept_no="{}"'''.format(self.tableWidget.item(self.tableWidget.currentRow(), 5).text())
        d_acci_col = ['insur_recept_no', 'insur_com', 'insur_charge_name', 'charge_call', 'charge_mail', 'reception_detail', 'messege_setting', 
                      'accident_date', 'reception_date', 'accident_detail', 'accident_addr', 'is_close', 'vehicle_number', 'fault', 'estimate_date', 
                      'doc_date', 'repair_date', 'get_pay', 'pay_bank', 'estim_pay', 'indemnity']
        d_acci_df = self.udata.make_dataframe(d_acci_query,d_acci_col)
        if d_acci_df['is_close'][0] == '종결':
            closee = '종결'
        else:
            closee='미종결'
        self.textBrowser.clear()
        self.textBrowser.append('차량번호')
        self.textBrowser.append(d_acci_df['vehicle_number'][0])
        self.textBrowser_2.setText(closee)
        self.textBrowser_3.setText(d_acci_df['accident_detail'][0])
        self.textBrowser_4.setText(d_acci_df['insur_com'][0])
        self.textBrowser_5.setText(d_acci_df['insur_recept_no'][0])
        self.textBrowser_6.setText(d_acci_df['insur_charge_name'][0])
        self.textBrowser_7.setText(d_acci_df['charge_call'][0])
        self.textBrowser_9.setText(d_acci_df['fault'][0])
        self.textBrowser_11.setText(str(d_acci_df['indemnity'][0]))
        self.tableWidget_2.setItem(0, 0, QTableWidgetItem(str(d_acci_df['accident_date'][0])))
        self.tableWidget_2.setItem(0, 1, QTableWidgetItem(str(d_acci_df['reception_date'][0])))
        self.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(d_acci_df['estimate_date'][0])))
        self.tableWidget_2.setItem(0, 3, QTableWidgetItem(str(d_acci_df['doc_date'][0])))
        self.tableWidget_2.setItem(0, 4, QTableWidgetItem(str(d_acci_df['repair_date'][0])))
        self.tableWidget_2.setItem(0, 5, QTableWidgetItem(closee))
        
    def verse(self):
        self.textBrowser_10.clear()
        if len(self.textBrowser_9.text()) >=1:
            self.textBrowser_10.setText(str(100-int(self.textBrowser_9.text())))
        

    def run_insurance_call(self, insur_no):
        if len(insur_no) !=0:
            self.open = Opne_crush_ing()
            self.open.open_insurance_call(insur_no)
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 클릭해주세요.")}
    
    def upload_mail(self):
        font = QtGui.QFont()
        font.setPointSize(15)
        try:
            ###db에 담당자 메일 업로드하는 코드###
            if len(self.lineEdit_2.text()) !=0:
                cpnn = pymysql.connect(host='', port=3306, user='', passwd='', db='')
                curs = cpnn.cursor()
                curs.execute('UPDATE accident_partner SET charge_mail="{}" where insur_recept_no="{}";'.format(self.lineEdit_2.text(),self.textBrowser_5.toPlainText()))
                cpnn.commit()
                cpnn.close()
                {self.msg.information(QtWidgets.QDialog(), "알림", "담당자 메일 주소를 업로드 하였습니다.")}
            else:
                {self.msg.information(QtWidgets.QDialog(), "알림", "담당자 메일 주소를 입력해주세요.")}
        except:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 입력해주세요.")}

    def acci_pic_load(self):
        if len(self.textBrowser_5.toPlainText()) !=0:
            self.acc_pic_fname = QFileDialog.getOpenFileName()[0]
            self.acc_pic_name="사고/{2}/{0}/{0} 사고사진.{1}".format(self.textBrowser_5.toPlainText(), self.acc_pic_fname.split('.')[-1],self.yearr)
            if len(self.acc_pic_fname)>=1:
                self.pushButton_9.setStyleSheet("background-color: #A3C1DA")
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 입력해주세요.")}
    def estimate_load(self):
        if len(self.textBrowser_5.toPlainText()) !=0:
            self.estimate_fname = QFileDialog.getOpenFileName()[0]
            self.estimate_name="사고/{2}/{0}/{0} 견적서.{1}".format(self.textBrowser_5.toPlainText(), self.estimate_fname.split('.')[-1],self.yearr)
            if len(self.estimate_fname)>=1:
                self.pushButton_11.setStyleSheet("background-color: #A3C1DA")
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 입력해주세요.")}
    def certificate_load(self):
        if len(self.textBrowser_5.toPlainText()) !=0:
            self.certificate_fname = QFileDialog.getOpenFileName()[0]
            self.certificate_name="사고/{2}/{0}/{0} 신고필증.{1}".format(self.textBrowser_5.toPlainText(), self.certificate_fname.split('.')[-1],self.yearr)
            if len(self.certificate_fname)>=1:
                self.pushButton_15.setStyleSheet("background-color: #A3C1DA")
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 입력해주세요.")}
    def repair_pic_load(self):
        if len(self.textBrowser_5.toPlainText()) !=0:
            self.repair_pic_fname = QFileDialog.getOpenFileName()[0]
            self.repair_pic_name="사고/{2}/{0}/{0} 수리사진.{1}".format(self.textBrowser_5.toPlainText(), self.repair_pic_fname.split('.')[-1],self.yearr)
            if len(self.repair_pic_fname)>=1:
                self.pushButton_10.setStyleSheet("background-color: #A3C1DA")
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 입력해주세요.")}
    def bb_load(self):
        if len(self.textBrowser_5.toPlainText()) !=0:
            self.bb_fname = QFileDialog.getOpenFileName()[0]
            self.bb_name="사고/{2}/{0}/{0} 통장사본.{1}".format(self.textBrowser_5.toPlainText(), self.bb_fname.split('.')[-1],self.yearr)
            if len(self.bb_fname)>=1:
                self.pushButton_17.setStyleSheet("background-color: #A3C1DA")
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 입력해주세요.")}
            
    def run_real_send_mail(self):
        if len(self.textBrowser_5.toPlainText())!=0:
            try:
                ff = upload_firebase()
                ff.firebase_upload(self.estimate_fname, self.estimate_name)
                ff.firebase_upload(self.acc_pic_fname, self.acc_pic_name)
                ff.firebase_upload(self.repair_pic_fname, self.repair_pic_name)
                ff.firebase_upload(self.certificate_fname, self.certificate_name)
                ff.firebase_upload(self.bb_fname, self.bb_name)
                mail_col = ['insure_recept_no', 'estimate', 'acci_pictures', 'repair_pictures', 'certificate', 'bankbook']
                mail_data = {'insure_recept_no':[self.textBrowser_5.toPlainText()], 'estimate':[self.estimate_name], 
                             'acci_pictures':[self.acc_pic_name], 'repair_pictures':[self.repair_pic_name], 'certificate':[self.certificate_name], 'bankbook':[self.bb_name]}
                try:
                    mail_table=pd.DataFrame(mail_data, columns=mail_col)
                    self.udata.upload_database(mail_table, 'document_send_breakdown')
                    self.open = Opne_crush_ing()
                    self.open.open_real_send_mail(self.textBrowser_5.toPlainText())
                except:
                    self.open = Opne_crush_ing()
                    self.open.open_real_send_mail(self.textBrowser_5.toPlainText())
            except:
                {self.msg.information(QtWidgets.QDialog(), "알림", "모든 파일을 업로드 한 후 입력해주세요.")}
        else:
            {self.msg.information(QtWidgets.QDialog(), "알림", "사고를 선택 후 입력해주세요.")}
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "진행중인 사고차 보험관리"))
        self.groupBox.setTitle(_translate("Form", "관리할 사고차 선택"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "접수일자"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "차량번호"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "과실"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "면책금"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "보험사"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "보험접수번호"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "종결 여부"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "수리견적"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "지급수리비"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "지급계좌"))
        self.pushButton.setText(_translate("Form", "선택한 사고차 관리"))
        self.comboBox.setItemText(0, _translate("Form", "차량번호"))
        self.comboBox.setItemText(1, _translate("Form", "종결 여부"))
        self.comboBox.setItemText(2, _translate("Form", "보험사접수번호"))
        self.pushButton_2.setText(_translate("Form", "조회"))
        #self.radioButton.setText(_translate("Form", "최신 순"))
        #self.radioButton_2.setText(_translate("Form", "오래된 순"))
        self.groupBox_2.setTitle(_translate("Form", "보험 및 사고 관리"))
        self.pushButton_3.setText(_translate("Form", "사고내역 삭제"))
        self.pushButton_4.setText(_translate("Form", "사고처리내역서 저장"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "사고 일자"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "접수 일자"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "견적 일자"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "서류발송 일자"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "수리비지급 일자"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", ""))
        #self.pushButton_5.setText(_translate("Form", "사고처리내역서 인쇄"))
        self.groupBox_3.setTitle(_translate("Form", "상대차 보험사 정보"))
        self.label_3.setText(_translate("Form", "보      험       사"))
        self.label_4.setText(_translate("Form", "보 험 접 수 번 호"))
        self.label_5.setText(_translate("Form", "보  험  담  당  자"))
        self.label_6.setText(_translate("Form", "보험 담당자 번호"))
        self.label_7.setText(_translate("Form", "보험 담당자 메일"))
        self.label_8.setText(_translate("Form", "보험 담당자와의 연락"))
        self.pushButton_7.setText(_translate("Form", "등록"))
        self.pushButton_8.setText(_translate("Form", "보험 담당자와의 연락"))
        self.groupBox_4.setTitle(_translate("Form", "서류 발송"))
        self.pushButton_9.setText(_translate("Form", "사고 사진 등록"))
        self.pushButton_10.setText(_translate("Form", "수리 사진 등록"))
        self.pushButton_11.setText(_translate("Form", "견적서 등록"))
        self.pushButton_15.setText(_translate("Form", "신고필증 등록"))
        self.pushButton_16.setText(_translate("Form", "상대 보험사 서류 발송"))
        self.pushButton_12.setText(_translate("Form", "과실비율 등록"))
        self.pushButton_17.setText(_translate("Form", "통장사본 등록"))
        self.pushButton_13.setText(_translate("Form", "면책금 등록"))
        self.groupBox_5.setTitle(_translate("Form", "수리비 지급 내역 등록"))
        self.pushButton_6.setText(_translate("Form", "사고 관리 종결"))
        self.label_10.setText(_translate("Form", "수리비 지급 일자"))
        self.label_13.setText(_translate("Form", "수 리  견 적"))
        self.label_14.setText(_translate("Form", "지급 수리비"))
        self.label_15.setText(_translate("Form", "지 급  계 좌"))
        self.groupBox_6.setTitle(_translate("Form", "사고 정보"))
        self.label_2.setText(_translate("Form", "종결 여부"))
        self.label_9.setText(_translate("Form", "사고 경위"))
        self.label_11.setText(_translate("Form", "과실 비율"))
        self.label_16.setText(_translate("Form", "면책금"))
        self.radioButton.setText(_translate("Form", "최신순"))
        self.radioButton_2.setText(_translate("Form", "오래된순"))
        self.label_12.setText(_translate("Form", ":"))
        self.label.setText(_translate("Form", "진행중인 사고차 보험 및 사고 관리"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = crush_ing_Ui_Form()
    ui.crush_ing_setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

