# -*- coding: utf-8 -*-

import pandas as pd
from openpyxl import Workbook
import openpyxl
import os
from save_database import *

class get_excel:
    def get_acci_excel(self, save_path, accident):
        udata = upload_db()
        work_file = openpyxl.load_workbook(os.path.join(os.path.abspath("."), '사고처리 내역서.xlsx'))
        wsfile = work_file.get_sheet_by_name('사고처리내역서')
        xl_query = 'select * from accident_partner where insur_recept_no="{}";'.format(accident)
        xl_col = ['insur_recept_no', 'insur_com', 'insur_charge_name', 'charge_call', 'charge_mail', 'reception_detail', 'messege_setting', 'accident_date', 
                  'reception_date', 'accident_detail', 'accident_addr', 'is_close', 'vehicle_number', 'fault', 'estimate_date', 'doc_date', 'repair_date', 
                  'get_pay', 'pay_bank', 'estim_pay']
        xl_df = udata.make_dataframe(xl_query, xl_col)

        wsfile['B7']=xl_df['accident_date'][0]
        wsfile['C7']=xl_df['reception_date'][0]
        wsfile['D7']=xl_df['estimate_date'][0]
        wsfile['E7']=xl_df['doc_date'][0]
        wsfile['F7']=xl_df['repair_date'][0]
        
        wsfile['D16']=xl_df['vehicle_number'][0]
        wsfile['G16']=xl_df['insur_com'][0]
        wsfile['D17']=xl_df['accident_detail'][0]
        
        wsfile['D22']=xl_df['insur_charge_name'][0]
        wsfile['G22']=xl_df['insur_com'][0]
        wsfile['D23']=xl_df['charge_call'][0]
        wsfile['G23']=xl_df['insur_recept_no'][0]
        wsfile['D24']=xl_df['reception_detail'][0]

        wsfile['D29']=xl_df['accident_date'][0]
        wsfile['D30']=xl_df['accident_detail'][0]
        wsfile['D31']=xl_df['accident_addr'][0]
        wsfile['D33']=xl_df['fault'][0]
        wsfile['E33']=100-int(xl_df['fault'][0])
        
        wsfile['D38']=xl_df['estim_pay'][0]
        wsfile['D39']=xl_df['get_pay'][0]
        wsfile['G38']=xl_df['repair_date'][0]
        wsfile['G39']=xl_df['pay_bank'][0]
        
        work_file.save(save_path+'/{}_사고처리내역서.xlsx'.format(accident))
        
