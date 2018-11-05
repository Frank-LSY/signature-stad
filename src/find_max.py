#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:43:42 2018

@author: frank-lsy
"""

import pandas as pd

def find_max(input_tsv,output_csv):
    data = pd.read_csv(input_tsv,sep='\t',header = 0)
    out = open(output_csv,'a+')
    sample = data['Sample Name']
    signature = {'sig1' : data['Signature.1'],
                 'sig2' : data['Signature.2'],
                 'sig3' : data['Signature.3'],
                 'sig4' : data['Signature.4'],
                 'sig5' : data['Signature.5'],
                 'sig6' : data['Signature.6'],
                 'sig7' : data['Signature.7'],
                 'sig8' : data['Signature.8'],
                 'sig9' : data['Signature.9'],
                 'sig10' : data['Signature.10'],
                 'sig11' : data['Signature.11'],
                 'sig12' : data['Signature.12'],
                 'sig13' : data['Signature.13'],
                 'sig14' : data['Signature.14'],
                 'sig15' : data['Signature.15'],
                 'sig16' : data['Signature.16'],
                 'sig17' : data['Signature.17'],
                 'sig18' : data['Signature.18'],
                 'sig19' : data['Signature.19'],
                 'sig20' : data['Signature.20'],
                 'sig21' : data['Signature.21'],
                 'sig22' : data['Signature.22'],
                 'sig23' : data['Signature.23'],
                 'sig24' : data['Signature.24'],
                 'sig25' : data['Signature.25'],
                 'sig26' : data['Signature.26'],
                 'sig27' : data['Signature.27'],
                 'sig28' : data['Signature.28'],
                 'sig29' : data['Signature.29'],
                 'sig30' : data['Signature.30']}
    for i in range(len(sample)):
        m = 'sig1'
        for j in range(1,30):
            if (signature[m][i]<signature["sig{}".format(j+1)][i]):
                m = "sig{}".format(j+1)
        row = sample[i]+','+m+'\n'
        out.write(row)
        print(m)
    out.close()
#find_max("../data/cin.tsv","../signature/cin.csv")
#find_max("../data/gs.tsv","../signature/gs.csv")
#find_max("../data/ebv.tsv","../signature/ebv.csv")
#find_max("../data/msi.tsv","../signature/msi.csv")
#find_max("../data/not-classified.tsv","../signature/not-classified.csv")
find_max("../data/male.tsv","../signature/male.csv")
find_max("../data/female.tsv","../signature/female.csv")
find_max("../data/male-all.tsv","../signature/male-all.csv")
find_max("../data/female-all.tsv","../signature/female-all.csv")