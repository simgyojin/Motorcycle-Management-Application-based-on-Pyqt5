# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:35:42 2020

@author: SAMSUNG
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import pandas as pd
import re

class Crawling_list:
    def get_drive(self,see, user_id, user_pass):
        ### 동작하는거 굳이 안보고 싶을 때###
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument('window-size=1920x1080')
        options.add_argument('__log-level=3')
        
        ###같은 dir에 있는 firefox driver의 path 가져옴
        dirr = os.path.dirname(__file__)
        driver_path = os.path.join(dirr, 'geckodriver.exe')

        ###driver의 동작 보기
        if see == 'want':
            driver = webdriver.Firefox(executable_path=driver_path)
            
        ### firefox_options=options 동작 보지 않음
        elif see == "not want":
            driver = webdriver.Firefox(firefox_options=options, executable_path=driver_path)
        

        ###로그인
        driver.get('')  #페이지 URL
        driver.find_element_by_name('user_id').send_keys(user_id)
        driver.find_element_by_name('password').send_keys(user_pass)
        driver.find_element_by_xpath('//*[@class="btn_login"]').click()

        ###페이지로 이동
        driver.get('')  #페이지 URL
        '''
        필요한 정보 크롤링
        '''
        
    
        
craw = Crawling_list()
ww = ['want', 'not want']
craw.get_drive(ww[0], 'id', 'pass')
