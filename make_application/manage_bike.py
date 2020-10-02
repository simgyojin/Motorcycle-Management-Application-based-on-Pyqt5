# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SAMSUNG\Desktop\알바\바이크뱅크\program\manage_bike_whghl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import math
import os
import re
import pandas as pd
import time

from PyQt5.QtWidgets import QFileDialog, QProgressBar, QDialog
#from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QProgressBar, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from save_firebase import *
from save_database import *
import pymysql

class Ui_manage_bike_whghl(object):
    def manage_bike_whghl_setupUi(self, manage_bike_whghl, what):
        manage_bike_whghl.setObjectName("manage_bike_whghl")
        manage_bike_whghl.resize(1502, 949)
        self.tableWidget = QtWidgets.QTableWidget(manage_bike_whghl)
        self.tableWidget.setGeometry(QtCore.QRect(40, 240, 1431, 681))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.tableWidget.setFont(font)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
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
        
        self.pushButton = QtWidgets.QPushButton(manage_bike_whghl)
        self.pushButton.setGeometry(QtCore.QRect(1250, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        ###
        self.pushButton.clicked.connect(lambda: self.whghl())
        ###
        self.lineEdit = QtWidgets.QLineEdit(manage_bike_whghl)
        self.lineEdit.setGeometry(QtCore.QRect(940, 160, 291, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(manage_bike_whghl)
        self.comboBox.setGeometry(QtCore.QRect(700, 160, 231, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(manage_bike_whghl)
        self.label.setGeometry(QtCore.QRect(40, 80, 351, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(manage_bike_whghl)
        self.label_2.setGeometry(QtCore.QRect(850, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(manage_bike_whghl)
        self.textBrowser.setGeometry(QtCore.QRect(40, 150, 431, 61))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(15)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser") 
        self.textBrowser.append(what)
        self.dateEdit_2 = QtWidgets.QDateEdit(manage_bike_whghl)
        self.dateEdit_2.setGeometry(QtCore.QRect(1050, 20, 201, 41))
        
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(manage_bike_whghl)
        self.pushButton_2.setGeometry(QtCore.QRect(1260, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        ###ddbb
        self.udata = upload_db()    
        cc = ['vehicle_number', 'contract_start', 'contract_end', 'model', 'manufacture', 
              'insur_info', 'take', 'vehicle_str', 'lease_aff','admin_no', 'branch_no']
        if what == '전체 이륜자동차 조회':
            qu = '''select branch_name, admin_no, admin_id, admin_pass, last_update from bikebank_branch;'''
            cu = ['branch_name', 'admin_no', 'admin_id', 'admin_pass','last_update']
            branch_table = self.udata.make_dataframe(qu,cu)
            self.pushButton_2.setDisabled(True)
            qq = '''select * from lease_contract_info'''
            data_table = self.udata.make_dataframe(qq,cc)
            date = QDate.currentDate()
            self.dateEdit_2.setDate(date)
            self.tableWidget.setRowCount(len(data_table))
            b2b_qq = '''select branch_no, branch_name from hangang_b2b_branch;'''
            b2b_cc = ['branch_no','branch_name']
            b2b_table = self.udata.make_dataframe(b2b_qq,b2b_cc)
            b2b_name_list = list(np.array(b2b_table['branch_name'].tolist()))
            for idx in range(len(data_table)):
                try:        #본사 리스
                    name_list = list(np.array(branch_table['branch_name'].tolist()))
                    nnn = int(data_table['admin_no'][idx])
                    admin_n = name_list[nnn-1]
                    lease_aff = data_table['lease_aff'][idx]
                except:
                    try:    #B2B리스
                        int(data_table['branch_no'][idx])
                        nmber = data_table['branch_no'][idx]
                        admin_n=data_table['lease_aff'][idx]
                        lease_aff = b2b_name_list[int(nmber)-1]
                    except: #개인리스
                        admin_n='바이크'
                        lease_aff="개인리스"
                self.tableWidget.setItem(idx, 0, QTableWidgetItem(str(admin_n)))
                self.tableWidget.setItem(idx, 6, QTableWidgetItem(data_table['manufacture'][idx]))
                self.tableWidget.setItem(idx, 2, QTableWidgetItem(data_table['model'][idx]))
                self.tableWidget.setItem(idx, 3, QTableWidgetItem(data_table['vehicle_number'][idx]))
                self.tableWidget.setItem(idx, 4, QTableWidgetItem(data_table['vehicle_str'][idx]))
                self.tableWidget.setItem(idx, 5, QTableWidgetItem(data_table['insur_info'][idx]))
                self.tableWidget.setItem(idx, 1, QTableWidgetItem(lease_aff))
                self.tableWidget.setItem(idx, 7, QTableWidgetItem(str(data_table['contract_start'][idx])))
                self.tableWidget.setItem(idx, 8, QTableWidgetItem(str(data_table['contract_end'][idx])))
                self.tableWidget.setItem(idx, 9, QTableWidgetItem(data_table['take'][idx]))
        
        else:
            if what == '바이크 이륜자동차 조회':
                self.pushButton_2.setDisabled(True)
                qq = '''select * from lease_contract_info where lease_aff="바이크" or lease_aff="대리점"'''
        #cc = ['vehicle_number', 'contract_start', 'contract_end', 'model', 'manufacture', 
        #      'insur_info', 'take', 'vehicle_str', 'lease_aff','admin_no', 'branch_no']
                data_table = self.udata.make_dataframe(qq,cc)
                date = QDate.currentDate()
                self.dateEdit_2.setDate(date)
                self.tableWidget.setRowCount(len(data_table))
                b2b_qq = '''select branch_no, branch_name from hangang_b2b_branch;'''
                b2b_cc = ['branch_no','branch_name']
                b2b_table = self.udata.make_dataframe(b2b_qq,b2b_cc)
                b2b_name_list = list(np.array(b2b_table['branch_name'].tolist()))
                for idx in range(len(data_table)):
                    try:    #B2B리스
                        int(data_table['branch_no'][idx])
                        nmber = data_table['branch_no'][idx]
                        admin_n=data_table['lease_aff'][idx]
                        lease_aff = b2b_name_list[int(nmber)-1]
                    except: #개인리스
                        admin_n='바이크'
                        lease_aff="개인리스"
                    self.tableWidget.setItem(idx, 0, QTableWidgetItem(str(admin_n)))
                    self.tableWidget.setItem(idx, 6, QTableWidgetItem(data_table['manufacture'][idx]))
                    self.tableWidget.setItem(idx, 2, QTableWidgetItem(data_table['model'][idx]))
                    self.tableWidget.setItem(idx, 3, QTableWidgetItem(data_table['vehicle_number'][idx]))
                    self.tableWidget.setItem(idx, 4, QTableWidgetItem(data_table['vehicle_str'][idx]))
                    self.tableWidget.setItem(idx, 5, QTableWidgetItem(data_table['insur_info'][idx]))
                    self.tableWidget.setItem(idx, 1, QTableWidgetItem(lease_aff))
                    self.tableWidget.setItem(idx, 7, QTableWidgetItem(str(data_table['contract_start'][idx])))
                    self.tableWidget.setItem(idx, 8, QTableWidgetItem(str(data_table['contract_end'][idx])))
                    self.tableWidget.setItem(idx, 9, QTableWidgetItem(data_table['take'][idx]))
            else:  
                qu = '''select branch_name, admin_no, admin_id, admin_pass, last_update from bikebank_branch where branch_name="{}";'''.format(what[:-9])
                cu = ['branch_name', 'admin_no', 'admin_id', 'admin_pass','last_update']
            
                branch_table = self.udata.make_dataframe(qu,cu)
                self.popup = PopUpProgressB(user_id =branch_table['admin_id'],
                                        user_pass =branch_table['admin_pass'],
                                        admin_no=branch_table['admin_no'][0])
                self.pushButton_2.clicked.connect(self.popup.start_progress)
                dfd = branch_table['last_update'][0]
                date = QDate.fromString(str(dfd),"yyyy-MM-dd")
                self.dateEdit_2.setDate(date)
                try:
                    qq = '''select * from lease_contract_info where admin_no={};'''.format(branch_table['admin_no'][0])
                    data_table = self.udata.make_dataframe(qq,cc)
                    name_list = list(np.array(branch_table['branch_name'].tolist()))
                    nnn = int(data_table['admin_no'][0])
                    admin_n = name_list[0]
                except:
                    load_data={'vehicle_number':[], 'contract_start':[], 'contract_end':[], 'model':[], 'manufacture':[], 
                               'insur_info':[], 'take':[], 'vehicle_str':[], 'lease_aff':[],'admin_no':[], 'branch_no':[]}
                    data_table = pd.DataFrame(load_data, columns=cc)
                self.tableWidget.setRowCount(len(data_table))
                b2b_qq = '''select branch_no, branch_name from hangang_b2b_branch;'''
                b2b_cc = ['branch_no','branch_name']
                b2b_table = self.udata.make_dataframe(b2b_qq,b2b_cc)
                b2b_name_list = list(np.array(b2b_table['branch_name'].tolist()))
        
                for idx in range(len(data_table)):
                    try:        #본사 리스
                        lease_aff = data_table['lease_aff'][idx]
                    except:
                        try:    #B2B리스
                            int(data_table['branch_no'][idx])
                            nmber = data_table['branch_no'][idx]
                            admin_n=data_table['lease_aff'][idx]
                            lease_aff = b2b_name_list[int(nmber)-1]
                        except: #개인리스
                            admin_n='바이크'
                            lease_aff="개인리스"
                    self.tableWidget.setItem(idx, 0, QTableWidgetItem(str(admin_n)))
                    self.tableWidget.setItem(idx, 6, QTableWidgetItem(data_table['manufacture'][idx]))
                    self.tableWidget.setItem(idx, 2, QTableWidgetItem(data_table['model'][idx]))
                    self.tableWidget.setItem(idx, 3, QTableWidgetItem(data_table['vehicle_number'][idx]))
                    self.tableWidget.setItem(idx, 4, QTableWidgetItem(data_table['vehicle_str'][idx]))
                    self.tableWidget.setItem(idx, 5, QTableWidgetItem(data_table['insur_info'][idx]))
                    self.tableWidget.setItem(idx, 1, QTableWidgetItem(lease_aff))
                    self.tableWidget.setItem(idx, 7, QTableWidgetItem(str(data_table['contract_start'][idx])))
                    self.tableWidget.setItem(idx, 8, QTableWidgetItem(str(data_table['contract_end'][idx])))
                    self.tableWidget.setItem(idx, 9, QTableWidgetItem(data_table['take'][idx]))
                    
        self.retranslateUi(manage_bike_whghl)
        QtCore.QMetaObject.connectSlotsByName(manage_bike_whghl)                

    def retranslateUi(self, manage_bike_whghl):
        _translate = QtCore.QCoreApplication.translate
        manage_bike_whghl.setWindowTitle(_translate("manage_bike_whghl", "관리중인 이륜차 조회"))      
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("manage_bike_whghl", "지사"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("manage_bike_whghl", "제조사"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("manage_bike_whghl", "차종"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("manage_bike_whghl", "차량번호"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("manage_bike_whghl", "차대번호"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("manage_bike_whghl", "보험정보"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("manage_bike_whghl", "리스지점"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("manage_bike_whghl", "리스계약시작일"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("manage_bike_whghl", "리스계약종료일"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("manage_bike_whghl", "인수/반납"))
        
        self.pushButton.setText(_translate("manage_bike_whghl", "조회"))
        self.pushButton_2.setText(_translate("manage_bike_whghl", "목록 업데이트"))
        self.comboBox.setItemText(0, _translate("manage_bike_whghl", "차대번호"))
        self.comboBox.setItemText(1, _translate("manage_bike_whghl", "차량번호"))
        self.label.setText(_translate("manage_bike_whghl", "관리중인 이륜차 조회"))
        self.label_2.setText(_translate("manage_bike_whghl", "마지막 업데이트 날짜"))

    def whghl(self):            
        
        msg=QtWidgets.QMessageBox()
        if len(self.lineEdit.text()) == 0:
            {msg.information(QtWidgets.QDialog(), "알림", "빈 칸을 채워주세요")}
        else:
            try:
                self.tableWidget.setRowCount(1)
                if self.comboBox.currentText() == '차대번호':
                    num = 'str'
                elif self.comboBox.currentText() == '차량번호':
                    num = 'number'
                qq = '''select * from lease_contract_info where vehicle_{}='{}';'''.format(num,self.lineEdit.text().strip())
                cc = ['vehicle_number', 'contract_start', 'contract_end', 'model', 'manufacture', 
                      'insur_info', 'take', 'vehicle_str', 'lease_aff','admin_no', 'branch_no']
                data_table = self.udata.make_dataframe(qq,cc)
                try:    #본사
                    qu = '''select branch_name, admin_no last_update from bikebank_branch where admin_no={};'''.format(data_table['admin_no'][0])
                    cu = ['branch_name']
                    branch_table = self.udata.make_dataframe(qu,cu)
                    admin_n = branch_table['branch_name'][0]
                    lease_aff=data_table['lease_aff'][0]
                except:
                    try:    #B2B리스
                        b2b_qq = '''select branch_no, branch_name from hangang_b2b_branch where branch_no={};'''.format(data_table['branch_no'][0])
                        b2b_cc = ['branch_name']
                        b2b_table = self.udata.make_dataframe(b2b_qq,b2b_cc)
                        admin_n=data_table['lease_aff'][0]
                        lease_aff = b2b_table['branch_name'][0]
                    except: #개인리스
                        admin_n='바이크'
                        lease_aff="개인리스"
                self.tableWidget.setItem(0, 0, QTableWidgetItem(str(admin_n)))
                self.tableWidget.setItem(0, 6, QTableWidgetItem(data_table['manufacture'][0]))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(data_table['model'][0]))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(data_table['vehicle_number'][0]))
                self.tableWidget.setItem(0, 4, QTableWidgetItem(data_table['vehicle_str'][0]))
                self.tableWidget.setItem(0, 5, QTableWidgetItem(data_table['insur_info'][0]))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(lease_aff))
                self.tableWidget.setItem(0, 7, QTableWidgetItem(str(data_table['contract_start'][0])))
                self.tableWidget.setItem(0, 8, QTableWidgetItem(str(data_table['contract_end'][0])))
                self.tableWidget.setItem(0, 9, QTableWidgetItem(data_table['take'][0]))

        
            except:
                self.tableWidget.setRowCount(0)
                {msg.information(QtWidgets.QDialog(), "알림", "없는 이륜자동차 입니다.")}
        
        

class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)
    strReady = pyqtSignal(str)

    @pyqtSlot()
    def proc_counter(self, see, user_id, user_pass, admin_no):  # A slot takes no params
        count = 0
        self.strReady.emit('업데이트 실행 중, 본사로 연결을 실행중이니 시간이 걸려도 기다려 주세요.')
        self.intReady.emit(1)
        ### 동작하는거 굳이 안보고 싶을 때###
        options = Options()
        options.add_argument( "--headless" )
        dirr = os.path.dirname(__file__)
        chromedriver_path = os.path.join(dirr, 'geckodriver.exe')
        
        ### ,chrome_options=options 드라이버 = 크롬 드라이버 뒤에 붙이기
        if see == 'want':
            driver = webdriver.Firefox(executable_path=chromedriver_path)
        
        elif see == "not want":
            driver = webdriver.Firefox(firefox_options=options, executable_path=chromedriver_path)
        count += 1
        time.sleep(1)
        self.intReady.emit(count)
        self.strReady.emit('홈페이지로 이동하는 중')
        a=1
        #로그인
        #if a==1:
        try:
            driver.get('login page')
            driver.find_element_by_name('user_id').click()
            driver.find_element_by_name('user_id').send_keys(user_id)
            driver.find_element_by_name('password').click()
            driver.find_element_by_name('password').send_keys(user_pass)
            driver.find_element_by_xpath('//*[@class="btn_login"]').click()

            #페이지로 이동
            driver.get('want data page')
            page_num = driver.find_element(By.CSS_SELECTOR,'table caption span.view').text
            count += 1
            self.intReady.emit(count)
            self.strReady.emit('홈페이지에 로그인 후 이륜차 정보를 가져오는 중')
        
            #for num in range(1,16):
            all_nn = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[1]'.format(1)).text
            last_page = (int(all_nn)//15)+1
            last_page_num=int(all_nn)%15
            bike_dic = {}



            #db에서 없는 이륜차만 가지고 오기 위해
            self.udata = upload_db()
            ccc='select vehicle_number from lease_contract_info'
            col=['vehicle_number']
            v_num=self.udata.make_dataframe(ccc,col)
            v_num_list=list(np.array(v_num['vehicle_number']))
        
            now_page=1
            while True:
                    if count>=80:
                        count -=20
                        self.intReady.emit(count)
                    #마지막 페이지면 작업하고 종료하기
                    if now_page == last_page:
                        for num in range(1, last_page_num+1):
                            vehicle_number = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[6]'.format(num)).text
                            if vehicle_number !='' and vehicle_number not in v_num_list:
                                print(vehicle_number)
                                car_count = driver.find_element(By.XPATH, '//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[1]'.format(num)).text
                                manufacture = driver.find_element(By.XPATH, '//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[2]'.format(num)).text
                                model = driver.find_element(By.XPATH, '//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[3]'.format(num)).text
                                vehicle_str = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[5]'.format(num)).text
                                contract = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[7]/span'.format(num)).text
                                insur_info = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[8]/span'.format(num)).text
                                lease_aff = re.sub('\n', ' ', driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[9]/span'.format(num)).text)
                                take = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[10]/span/strong'.format(num)).text
                                contract_start = int(contract[:8].replace('.', ''))
                                contract_end = int(contract[9:].replace('.', ''))
                            
                                bike_dic[car_count] = [vehicle_number, contract_start, contract_end, model, manufacture, 
                                               insur_info, take, vehicle_str, lease_aff, admin_no]
                                count += 0.25
                                self.intReady.emit(count)
                                self.strReady.emit('새로운 바이크: {} 정보를 가져오는 중'.format(vehicle_number))
                            else:
                                count += 0.25
                                self.intReady.emit(count)
                                self.strReady.emit('기존 바이크: {} 정보를 가져오는 중'.format(vehicle_number))
                        break
                    else:
                        for num in range(1,16):
                            vehicle_number = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[6]'.format(num)).text
                            if vehicle_number !='' and vehicle_number not in v_num_list:
                                car_count = driver.find_element(By.XPATH, '//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[1]'.format(num)).text
                                manufacture = driver.find_element(By.XPATH, '//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[2]'.format(num)).text
                                model = driver.find_element(By.XPATH, '//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[3]'.format(num)).text
                                vehicle_str = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[5]'.format(num)).text
                                contract = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[7]/span'.format(num)).text
                                insur_info = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[8]/span'.format(num)).text
                                lease_aff = re.sub('\n', ' ', driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[9]/span'.format(num)).text)
                                take = driver.find_element(By.XPATH,'//*[@id="MainContents"]/div/div/div[2]/table/tbody/tr[{}]/td[10]/span/strong'.format(num)).text
                                contract_start = int(contract[:8].replace('.', ''))
                                contract_end = int(contract[9:].replace('.', ''))
                            
                                bike_dic[car_count] = [vehicle_number, contract_start, contract_end, model, manufacture, 
                                               insur_info, take, vehicle_str, lease_aff, admin_no]
                                count += 0.25
                                self.intReady.emit(count)
                                self.strReady.emit('새로운 바이크: {} 정보를 가져오는 중'.format(vehicle_number))
                            else:
                                count += 0.25
                                self.intReady.emit(count)
                                self.strReady.emit('기존 바이크: {} 정보를 가져오는 중'.format(vehicle_number))

                        
                #다음 페이지로 넘어가기
                now_page+=1
                driver.get('page={}'.format(now_page))
            
            driver.close()
            driver.quit()
            cpnn = pymysql.connect(host='', port=3306, user='', passwd='', db='')
            curs = cpnn.cursor()
            #curs.execute('delete from lease_contract_info where year(contract_end)=year(curdate()) and month(contract_end)=month(curdate())-1;')
            curs.execute('UPDATE bikebank_branch SET last_update = {} where admin_no={};'.format(QDate.currentDate().toString('yyyyMMdd'),admin_no))
            cpnn.commit()
            cpnn.close()
            #ddbb 수정
            bike_df = pd.DataFrame(bike_dic).T
            if len(bike_df) >= 1:
                bike_df.columns=['vehicle_number', 'contract_start', 'contract_end', 'model', 'manufacture', 
                             'insur_info', 'take', 'vehicle_str', 'lease_aff', 'admin_no']
                self.udata.upload_database(bike_df, 'lease_contract_info')
            msg=QtWidgets.QMessageBox()
            self.finished.emit()
            {msg.information(QtWidgets.QDialog(), "성공", "목록 업데이트를 완료하였습니다.")}
        #else:
        except:
            self.finished.emit()
            msg=QtWidgets.QMessageBox()
            {msg.information(QtWidgets.QDialog(), "에러", "페이지에서 불러오지 못했습니다. \n잠시후 다시 시도해주세요.")}
            




class PopUpProgressB(QWidget):
    ###
    def __init__(self, user_id, user_pass, admin_no):
    ###
        self.user_id = user_id
        self.user_pass = user_pass
        self.admin_no = admin_no
        super().__init__()
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(20, 70, 691, 51)
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(14)
        self.pbar.setFont(font)
        self.pbar.setMaximum(100)
        

        self.pbar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(20, 140, 681, 221))
        self.textBrowser.setObjectName("textBrowser")
        
        
        QtCore.QMetaObject.connectSlotsByName(self)
        
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "진행상황"))       


        self.obj = Worker()
        self.thread = QThread()
        self.obj.intReady.connect(self.on_count_changed)
        self.obj.strReady.connect(self.on_str_append)
        self.obj.moveToThread(self.thread)
        self.obj.finished.connect(self.thread.quit)
        self.obj.finished.connect(self.hide)  # To hide the progress bar after the progress is completed
        ###
        self.thread.started.connect(lambda:self.obj.proc_counter('not want', self.user_id, self.user_pass, self.admin_no))
        ###
        # self.thread.start()  # This was moved to start_progress

    def start_progress(self):  # To restart the progress every time
        #self.textBrowser.clear()
        self.show()
        self.thread.start()

    def on_count_changed(self, value):
        self.pbar.setValue(value)
        
    def on_str_append(self, value):
        self.textBrowser.append(value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manage_bike_whghl = QtWidgets.QWidget()
    ui = Ui_manage_bike_whghl()
    ui.manage_bike_whghl_setupUi(manage_bike_whghl,'이륜자동차 조회')
    manage_bike_whghl.show()
    sys.exit(app.exec_())
