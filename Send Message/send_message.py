# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:42:12 2020

@author: SAMSUNG
"""

import pyairmore
from ipaddress import IPv4Address # for your IP address
from pyairmore.request import AirmoreSession # to create an AirmoreSession
from pyairmore.services.messaging import MessagingService # to send messages
import datetime

class Send_message:  
    def employee_send(self, ip_addr, port, cellPhone, name, info):
        # Airmore 활성화
        ipAddress = ip_addr
        ip = IPv4Address(ipAddress)
 
        session = AirmoreSession(ip, int(port))
        service = MessagingService(session) 
        now_date = datetime.date.today()
        #보낼 문자내용
        if info == '직원등록':
            message = '{}일자로 {}님의 직원등록이 완료되었습니다.'.format(now_date, name)
        elif info == '직원수정':
            message ='{}님의 정보가 변경 완료되었습니다.'.format(name)
        elif info=='보험사서류발송':
            message ='처리 서류를 메일로 발송하였습니다. 확인 부탁드립니다.'.format(name)
        elif info =='관리자등록':
            message = '{}일자로 {}님의 관리자등록이 완료되었습니다.'.format(now_date, name)
        service.send_message(cellPhone, message)

    
    def send_insurance(self, ip_addr, cellPhone, name, message):
        ipAddress = ip_addr
        ip = IPv4Address(ipAddress)
        session = AirmoreSession(ip, 2333)
        service = MessagingService(session)
        sendMessage = "{}님 안녕하세요. {}".format(name, message)
        service.send_message(cellPhone, sendMessage)              
