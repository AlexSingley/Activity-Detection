# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 01:37:13 2018

@author: singl
"""

import pandas as pd

bodyParts = ['THEAD', 'LSHO', 'RSHO', 'LMW', 'RMW', 'LPSIS', 'RPSIS', 'LLEK', 'RLEK', 'LHEE', 'RHEE', 'LTOE', 'RTOE']

i = 3

def excelToCSV():
    if(i<10):
        wbName = '00' + str(i)
    elif(i<100):
        wbName = '0' + str(i)
    else:
        wbName = str(i)
    
    df = pd.read_excel('C:\\Users\\singl\\Documents\\Dips Lab\\' + wbName + '.xlsx', sheetname='mocap-' + wbName, index_col=None)
    df.to_csv(csvName, encoding='utf-8')

def csvToCSV():
    cols = []
    j = 0
    k = 0
    if(i<10):
        wbName = '00' + str(i)
    elif(i<100):
        wbName = '0' + str(i)
    else:
        wbName = str(i)
       
    df = pd.read_csv('C:\\Users\\singl\\Documents\\Dips Lab\\' + wbName + '.csv')
    while(j<len(bodyParts)):
        if any(df.columns.str.contains(str(bodyParts[j]))):
            cols.append(str(bodyParts[j]) + '.PosX')
            cols.append(str(bodyParts[j]) + '.PosY')
            cols.append(str(bodyParts[j]) + '.PosZ')
            print('here')
            
        j+=1

    if(cols != []):
        while(k<j):
            start = 0
            end = 99
            
            while(end<63999):
                df.loc[[start, end], cols[k] + ' Std. Dev.'] = df.loc[[start, end], cols[k]].std()
                print(start)
                print(end)
                print(k)
                start+=100
                end+=100
                
            cols.append(cols[k] + ' Std. Dev.')
            k+=1
    if(cols != []):
        df.to_csv(wbName + 'c.csv', columns=cols, encoding='utf-8', index=False)

while(i<=81):
    if(i<10):
        csvName = '00' + str(i) + '.csv'
    elif(i<100):
        csvName = '0' + str(i) + '.csv'
    else:
        csvName = str(i) + '.csv'
        
    csvToCSV()
    i+=1
    if(i == 37):
        i = 40