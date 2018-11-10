# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:26:34 2018

@author: singl
"""

import pandas as pd
import csv

bodyPart = ['THEAD', 'SACR', 'STRN', 'LSHO', 'LMEE', 'LMW', 'RSHO', 'RMEE', 'RMW', 'LPSIS', 'RPSIS', 'LLEK', 'LHEE', 'LTOE', 'RLEK', 'RHEE', 'RTOE']
saveColumns = []
k = 0

def search():
    df = pd.read_csv(csvName)
    x, y, z = np.loadtxt(f, unpack=True, delimiter=',')
    while(bodyPart.next):
        for columnn in range(1):
            if any(bodyPart in x[k]):
                saved_column = x[k]
            k += 1
    k = 0
            
def copy():
    
            

while(i<81):
    if(i<10):
        with open('00' + str(i) + '.csv', 'r') as f:
            data = csv.reader(csvName)
            x, y, z = np.loadtxt(f, skiprows=1, unpack=True, delimiter=',')
            for row in range(len(x)):
                if(j>=64000):
                    break
                while(i<100):
                    sum()
                    i+=1
                    j+=1
    elif(i<100):
        with open('0' + str(i) + '.csv', 'r') as f:
            data = csv.reader(csvName)
            x, y, z = np.loadtxt(f, skiprows=1, unpack=True, delimiter=',')
            for row in range(len(x)):
                if(j>=64000):
                    break
                while(i<100):
                    sum()
                    i+=1
                    j+=1
    else:
        with open(str(i) + '.csv', 'r') as f:
            data = csv.reader(csvName)
            x, y, z = np.loadtxt(f, skiprows=1, unpack=True, delimiter=',')
            for row in range(len(x)):
                if(j>=64000):
                    break
                while(i<100):
                    sum()
                    i+=1
                    j+=1