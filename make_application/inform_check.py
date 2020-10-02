# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SAMSUNG\Desktop\알바\바이크뱅크\program\inform_check.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from save_database import *

class Inform_check(object):
    def setupUi(self, widget, value1, value2):
        widget.setObjectName("widget")
        widget.resize(640, 718)
        self.horizontalLayoutWidget = QtWidgets.QWidget(widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("a고딕16")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 450, 70))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.textBrowser_8.setMaximumSize(QtCore.QSize(450, 90))
        
        ###126 361/50
        self.textBrowser_8.append(value1)
        self.textBrowser_8.append(value2)
        ###
        
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.horizontalLayout_2.addWidget(self.textBrowser_8)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 160, 621, 529))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 50, 601, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_4)
        self.textBrowser.setMaximumSize(QtCore.QSize(451, 59))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_4.addWidget(self.textBrowser)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 130, 601, 61))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(451, 59))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_5.addWidget(self.textBrowser_2)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 210, 601, 61))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_6)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(451, 59))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_6.addWidget(self.textBrowser_3)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 290, 601, 61))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_7)
        self.textBrowser_4.setMaximumSize(QtCore.QSize(451, 59))
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_7.addWidget(self.textBrowser_4)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 370, 601, 61))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_8)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(451, 59))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_8.addWidget(self.textBrowser_5)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 450, 601, 61))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("a고딕13")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_9)
        self.textBrowser_6.setMaximumSize(QtCore.QSize(451, 59))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout_9.addWidget(self.textBrowser_6)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 530, 601, 61))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.textBrowser_7 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_10)
        self.textBrowser_7.setMaximumSize(QtCore.QSize(451, 59))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.horizontalLayout_10.addWidget(self.textBrowser_7)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(10, 610, 601, 61))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.textBrowser_9 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_11)
        self.textBrowser_9.setMaximumSize(QtCore.QSize(451, 59))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.horizontalLayout_11.addWidget(self.textBrowser_9)
        self.horizontalLayout_3.addWidget(self.groupBox)

        self.udata = upload_db()
        if value1 == '차량번호':
            valuee = 'vehicle_number'
            
        elif value1 =='차대번호':
            valuee='vehicle_str'
        qu = '''select branch_no, admin_no, lease_aff, model, insur_info, vehicle_str, vehicle_number from lease_contract_info where {}='{}';'''.format(valuee,value2)
        cu = ['branch_no','admin_no', 'lease_aff', 'model', 'insur_info', 'vehicle_str', 'vehicle_number']
        self.data_table = self.udata.make_dataframe(qu,cu)
        try:    #본사
            qu = '''select branch_name, admin_no last_update from bikebank_branch where admin_no={};'''.format(self.data_table['admin_no'][0])
            cu = ['branch_name']
            branch_table = self.udata.make_dataframe(qu,cu)
            admin_n = branch_table['branch_name'][0]
            lease_aff=self.data_table['lease_aff'][0]
        except:
            try:    #B2B리스
                b2b_qq = '''select branch_no, branch_name from hangang_b2b_branch where branch_no={};'''.format(self.data_table['branch_no'][0])
                b2b_cc = ['branch_name']
                b2b_table = self.udata.make_dataframe(b2b_qq,b2b_cc)
                admin_n=self.data_table['lease_aff'][0]
                lease_aff = b2b_table['branch_name'][0]
            except: #개인리스
                admin_n='바이크'
                lease_aff="개인리스"

        try:
            self.textBrowser_3.setText(self.data_table['model'][0])
            self.textBrowser_4.setText(self.data_table['insur_info'][0])
            self.textBrowser_6.setText(self.data_table['vehicle_str'][0])
            self.textBrowser_5.setText(self.data_table['vehicle_number'][0])
            self.textBrowser.setText(admin_n)
            self.textBrowser_2.setText(lease_aff)
        except:
            msg=QtWidgets.QMessageBox()
            {msg.information(QtWidgets.QDialog(), "알림", "없는 이륜자동차입니다.")}
        
        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "이륜자동차 정보조회"))
        self.label.setText(_translate("widget", "이륜자동차 정보조회"))
        self.label_2.setText(_translate("widget", "(으)로 정보조회 결과 "))
        self.groupBox.setTitle(_translate("widget", "이륜자동차 정보 "))
        self.label_4.setText(_translate("widget", "관리 회사"))
        self.label_5.setText(_translate("widget", "관리 지점"))
        self.label_6.setText(_translate("widget", "가입 차종"))
        self.label_7.setText(_translate("widget", "보험 정보"))
        self.label_8.setText(_translate("widget", "차량번호"))
        self.label_9.setText(_translate("widget", "차대번호"))


'''
    def closeMyApp_OpenNewApp(self):         
        widget = QtWidgets.QWidget()
        widget.close()
'''
"""
        if self.data_table['admin_no'][0] is None and self.data_table['branch_no'][0] is None:  #개인리스
            admin_n='바이크 개인리스'
            lease_aff=""
        elif self.data_table['admin_no'][0] is None:  #B2B리스
            b2b_qq = '''select branch_no, branch_name from hangang_b2b_branch where branch_no={};'''.format(self.data_table['branch_no'][0])
            b2b_cc = ['branch_name']
            b2b_table = self.udata.make_dataframe(b2b_qq,b2b_cc)
            admin_n=self.data_table['lease_aff'][0]
            lease_aff = b2b_table['branch_name'][0]
        elif self.data_table['branch_no'][0] is None: #본사 리스
            qu = '''select branch_name, admin_no last_update from bikebank_branch where admin_no={};'''.format(self.data_table['admin_no'][0])
            cu = ['branch_name']
            branch_table = self.udata.make_dataframe(qu,cu)
            admin_n = branch_table['branch_name'][0]
            lease_aff=self.data_table['lease_aff'][0]
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Inform_check()
    ui.setupUi(widget, '차량번호','대구서하')
    widget.show()
    sys.exit(app.exec_())
