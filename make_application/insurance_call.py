# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtWidgets import *
from save_database import *

class insurance_call_Ui_Form(object):
    def insurance_call_setupUi(self, Form, accident):
        self.udata=upload_db()
        Form.setObjectName("Form")
        Form.resize(640, 901)
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕15")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 460, 621, 431))
        font = QtGui.QFont()
        font.setFamily("a고딕14")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(210, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(350, 40, 41, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 601, 301))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 79, 181, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 621, 371))
        font = QtGui.QFont()
        font.setFamily("a고딕14")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 211, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateTimeEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(20, 80, 381, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        ###
        now_date = QDate.currentDate()
        now_time = QTime.currentTime()
        self.dateTimeEdit.setDate(now_date)
        self.dateTimeEdit.setTime(now_time)
        ###
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 170, 581, 131))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(220, 310, 171, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        ###
        self.msg=QtWidgets.QMessageBox()
        self.pushButton.clicked.connect(lambda: self.insurance_call_update(accident))
        
        ###call count
        count_query = '''SELECT COUNT(insur_recept_no) FROM partner_call_brekdown where insur_recept_no="{}";'''.format(accident)
        count_col = ['COUNT(insur_recept_no)']
        count_df = self.udata.make_dataframe(count_query, count_col)
        self.textBrowser.clear()
        ccc = int(count_df['COUNT(insur_recept_no)'][0])
        self.textBrowser.setText(str(ccc))
        
        ###call breakdown
        call_query='''select * from partner_call_brekdown where insur_recept_no="{}";'''.format(accident)
        call_col = ['insur_recept_no', 'call_detail', 'call_date']
        call_df = self.udata.make_dataframe(call_query, call_col)
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(call_df))
        for idx in range(len(call_df)):
            self.tableWidget.setItem(idx,0, QTableWidgetItem(str(call_df['call_date'][idx])))
            self.tableWidget.setItem(idx,1, QTableWidgetItem(call_df['call_detail'][idx]))
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def insurance_call_update(self, accident):
        try:
            ###db에 내용 업데이트 코드
            call_datee = self.dateTimeEdit.date().toString('yyyyMMdd')
            call_details=self.textEdit.toPlainText()
            call_column=['insur_recept_no', 'call_detail', 'call_date']
            call_data = {'insur_recept_no':[accident], 'call_detail':[call_details], 'call_date':[call_datee]}
            call_table = pd.DataFrame(call_data, columns=call_column)
            self.udata.upload_database(call_table,'partner_call_brekdown')
            {self.msg.information(QtWidgets.QDialog(),"알림","내용을 업로드 완료 하였습니다.")}
        except:
            {self.msg.information(QtWidgets.QDialog(),"에러","알 수 없는 에러입니다. 다시 시도해 주세요.")}
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "보험 담당자와의 연락 관리"))
        self.label.setText(_translate("Form", "보험 담당자와의 연락 관리"))
        self.groupBox.setTitle(_translate("Form", "누적 연락 정보"))
        self.label_2.setText(_translate("Form", "담당자와 연락 횟수"))
        self.label_3.setText(_translate("Form", "회"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "연락 일자"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "연락 내용"))
        self.label_6.setText(_translate("Form", "연락 내역"))
        self.groupBox_2.setTitle(_translate("Form", "신규 연락 등록"))
        self.label_4.setText(_translate("Form", "신규 연락 일자"))
        self.label_5.setText(_translate("Form", "신규 연락 내용"))
        self.pushButton.setText(_translate("Form", "등록"))


if __name__ == "__main__":
    import sys
    Dialog=QtWidgets.QDialog()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = insurance_call_Ui_Form()
    ui.insurance_call_setupUi(Form,'롯손보123')
    Form.show()
    sys.exit(app.exec_())

