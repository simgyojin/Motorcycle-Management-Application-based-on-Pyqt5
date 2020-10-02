# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SAMSUNG\Desktop\program\z_ui\real_send_mail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDate
from save_database import *
from save_firebase import *
import pymysql
import os
import smtplib
from email import encoders
from email.utils import formataddr
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

        
class real_send_mail_Ui_Form(object):
    def real_send_mail_setupUi(self, Form, accident):
        self.udata = upload_db()
        acci_query = '''select ap.insur_com, ap.charge_mail, lci.vehicle_number, lci.admin_no, lci.branch_no
                        from accident_partner as ap
                        join lease_contract_info as lci
                        on lci.vehicle_number = ap.vehicle_number
                        where ap.insur_recept_no="{}"'''.format(accident)
        acci_col = ['insur_com', 'charge_mail', 'vehicle_number', 'admin_no', 'branch_no']
        acci_df = self.udata.make_dataframe(acci_query,acci_col)
        for idx in range(len(acci_df)):
            try:        #바이크뱅크 리스
                bb_qq = ''''select branch_name from bikebank_branch where admin_no={};'''.format(acci_df['admin_no'][0])
                bb_col = ['branch_name']
                bb_df = self.udata.make_dataframe(bb_qq,bb_col)
                admin_name = bb_df['branch_name'][0]
            except:
                admin_name='한강바이크'
        from_email = 'hangang_ansan@naver.com'
        to_email = acci_df['charge_mail'][0]
        to_name = acci_df['insur_com'][0]
        mail_title = '{}-{}'.format(accident,acci_df['vehicle_number'][0])
        mail_text='보험 접수번호 {}에 대한 견적서, 통장사본, 신고필증, 사고사진, 수리사진입니다. \n\n빠른 확인 후 처리 부탁드립니다. \n\n{} 드림'.format(accident, admin_name)
        
        
        Form.setObjectName("Form")
        Form.resize(647, 860)
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕17")
        font.setPointSize(17)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 130, 611, 151))
        font = QtGui.QFont()
        font.setFamily("a고딕14")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 40, 351, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        ###
        self.lineEdit_5.setText(admin_name)
        ###
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 211, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 90, 351, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        ###
        self.lineEdit_6.setText(from_email)
        ###
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 300, 611, 331))
        font = QtGui.QFont()
        font.setFamily("a고딕14")
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(20, 40, 211, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(240, 40, 351, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        ###
        self.lineEdit_8.setText(to_name)
        ###
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 190, 211, 31))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(240, 90, 351, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        ###
        self.lineEdit_9.setText(to_email)
        ###
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(240, 140, 351, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText(mail_title)
        self.lineEdit_11 = QtWidgets.QTextEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(240, 190, 351, 131))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setText(mail_text)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 790, 231, 51))
        font = QtGui.QFont()
        font.setFamily("a고딕14")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        ###
        Dialog=QtWidgets.QDialog()
        self.pushButton_8.clicked.connect(lambda: self.send_mail('hangang_ansan','hangangbike',Dialog,accident))
        ###
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 251, 41))
        font = QtGui.QFont()
        font.setFamily("a고딕14")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        ###
        self.textBrowser.append(accident)
        ###
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 640, 611, 141))
        font = QtGui.QFont()
        font.setFamily("a고딕14")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 30, 581, 91))
        font = QtGui.QFont()
        font.setFamily("a고딕12")
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        
        self.msg=QtWidgets.QMessageBox()
        self.pushButton_9.clicked.connect(lambda: self.file_accept(accident))
        self.aa = 0
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def file_accept(self, recept_no):
        self.folder_path = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        file_query='''select estimate, acci_pictures, repair_pictures, certificate, bankbook from document_send_breakdown where insure_recept_no='{}';'''.format(recept_no)
        file_col=['estimate', 'acci_pictures', 'repair_pictures', 'certificate', 'bankbook']
        file_table = self.udata.make_dataframe(file_query,file_col)
        self.file_list = [file_table['estimate'][0],file_table['acci_pictures'][0],
                     file_table['repair_pictures'][0],file_table['certificate'][0],file_table['bankbook'][0]]
        s_firebase = upload_firebase()
        s_firebase.firebase_downloas(self.folder_path, self.file_list)
        {self.msg.information(QtWidgets.QDialog(), "알림", "선택한 파일 경로에 관련 파일이 다운로드 되었습니다.")}
        self.aa = 'ok'

    def send_mail(self, user_id, user_pass, Dialog, accident):
        if self.aa == 'ok':
            font = QtGui.QFont()
            font.setPointSize(15)
            {self.msg.information(Dialog,"알림","확인을 누르시면 메일을 전송을 시작합니다. \n완료메세지가 뜨기 전까지 종료하지 말아주세요.")}
            try:
                from_addr = formataddr((self.lineEdit_5.text(), self.lineEdit_6.text()))
                to_addr = formataddr((self.lineEdit_8.text(), self.lineEdit_9.text()))
                session = None
                # SMTP 세션 생성
                session = smtplib.SMTP('smtp.naver.com', 587)
                session.set_debuglevel(True)
    
                # SMTP 계정 인증 설정
                session.ehlo()
                session.starttls()
                session.login(user_id, user_pass)
                
                # 메일 콘텐츠 설정
                message = MIMEMultipart("mixed")
                message_2 = MIMEMultipart("mixed")
            
                # 메일 송/수신 옵션 설정
                message.set_charset('utf-8')
                message['From'] = from_addr
                message['To'] = to_addr
                message['Subject'] = self.lineEdit_10.text()
                
                message_2['From'] = from_addr
                message_2['To'] = from_addr
                message_2['Subject'] = self.lineEdit_10.text()+'   확인용'
 
                # 메일 콘텐츠 - 내용
                body = self.lineEdit_11.toPlainText()
                bodyPart = MIMEText(body, 'html', 'utf-8')
                message.attach( bodyPart )
                
                bodyPart_2 = MIMEText(body+'\n\n위와 같이 전송함', 'html', 'utf-8')
                message_2.attach( bodyPart_2 )
 
                # 메일 콘텐츠 - 첨부파일
                attachments = []
                for i in self.file_list:
                    attachments.append(os.path.join(self.folder_path, i.split('/')[-1]))
 
                for attachment in attachments:
                    attach_binary = MIMEBase("application", "octect-stream")
                    
                    binary = open(attachment, "rb").read() # read file to bytes
 
                    attach_binary.set_payload( binary )
                    encoders.encode_base64( attach_binary ) # Content-Transfer-Encoding: base64
                
                    filename = os.path.basename( attachment )
                    attach_binary.add_header("Content-Disposition", 'attachment', filename=('utf-8', '', filename))
                        
                    message.attach( attach_binary )
                    message_2.attach( attach_binary )

                # 메일 발송
                session.sendmail(from_addr, to_addr, message.as_string())
                session.sendmail(from_addr, from_addr, message_2.as_string())
                    
                cpnn = pymysql.connect(host='112.170.233.23', port=3306, user='gyojin', passwd='endeoddl2', db='hangang_backup')
                curs = cpnn.cursor()
                curs.execute('update accident_partner set estimate_date="{0}", doc_date="{0}" where insur_recept_no="{1}";'.format(QDate.currentDate().toString('yyyyMMdd'), accident))
                cpnn.commit()
                cpnn.close()
                cc = ['insur_recept_no', 'call_detail', 'call_date']
                add_call={'insur_recept_no':[accident], 'call_detail':['자료 메일 발송'], 'call_date':[QDate.currentDate().toString('yyyyMMdd')]}
                add_call_table = pd.DataFrame(add_call, columns=cc)
                self.udata.upload_database(add_call_table,'partner_call_brekdown')    
                {self.msg.information(Dialog,"알림","메일을 전송을 완료하였습니다.")}
            except:
                {self.msg.information(Dialog,"알림","발신자와 수신자의 이메일 주소를 확인해주세요.")}

            if session is not None:
                session.quit()
        else:
            {self.msg.information(Dialog,"알림","발송할 서류를 먼저 확인해주세요.")}
                

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "수리비 청구 서류 발송"))
        self.label_17.setText(_translate("Form", "수리비 청구 서류 발송"))
        self.groupBox.setTitle(_translate("Form", "발송처 확인"))
        self.label_5.setText(_translate("Form", "메   일     발   송   처"))
        self.label_6.setText(_translate("Form", "발 송 처   메 일 주 소"))
        self.groupBox_3.setTitle(_translate("Form", "수신처 및 내용 확인"))
        self.label_8.setText(_translate("Form", "메   일     수   신   처"))
        self.label_7.setText(_translate("Form", "수 신 처   메 일 주 소"))
        self.label_9.setText(_translate("Form", "메    일         제    목"))
        self.label_10.setText(_translate("Form", "메    일         내    용"))
        self.pushButton_8.setText(_translate("Form", "메일 발송"))
        self.groupBox_2.setTitle(_translate("Form", "파일 확인"))
        self.pushButton_9.setText(_translate("Form", "전송할 파일 확인"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = real_send_mail_Ui_Form()
    ui.real_send_mail_setupUi(Form,'123123123')
    Form.show()
    sys.exit(app.exec_())

