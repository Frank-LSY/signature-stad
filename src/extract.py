#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:14:57 2018

@author: frank-lsy
"""
import time
import re
import pandas as pd 
import csv
import os

f = '../decomposed30.tsv'

#cin_dir = '../data/cin'
#ebv_dir = '../data/ebv'
#msi_dir = '../data/msi'
#gs_dir = '../data/gs'
#out_dir = '../data/not-classified'
male_dir = '../data/male'
female_dir = '../data/female'

#cin = open('../dataset/cin.csv','r')
#ebv = open('../dataset/ebv.csv','r')
#msi = open('../dataset/msi.csv','r')
#gs = open('../dataset/gs.csv','r')
#exist = open('../dataset/no.csv','r')
male = open('../dataset/male.csv','r')
female = open('../dataset/female.csv','r')

#print (cin_arr)

#exist_arr = exist.readlines()
#cin_arr = cin.readlines()
#ebv_arr = ebv.readlines()
#msi_arr = msi.readlines()
#gs_arr = gs.readlines()
male_arr = male.readlines()
female_arr = female.readlines()

def strip(arr):
    p=re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
    #print(arr)
    return arr

def extract(input_file,source_arr,output_file):
    head = "Sample Name\tNumber of Mutations\tSignature.1\tSignature.2\tSignature.3\tSignature.4\tSignature.5\tSignature.6\tSignature.7\tSignature.8\tSignature.9\tSignature.10\tSignature.11\tSignature.12\tSignature.13\tSignature.14\tSignature.15\tSignature.16\tSignature.17\tSignature.18\tSignature.19\tSignature.20\tSignature.21\tSignature.22\tSignature.23\tSignature.24\tSignature.25\tSignature.26\tSignature.27\tSignature.28\tSignature.29\tSignature.30\n"
    g = open(output_file+'.tsv','a+')
    g.writelines(head)
    for item in source_arr:
        f = open(input_file,'r')
        line_num = 0
        print("writing the "+item+" file.")
        while 1:
            line_num += 1
            line = f.readline()
            #print(line)
            match = item+'-[0-9][0-9][A-Z]-[0-9][0-9][A-Z]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]-08'
            #print (item)
            t = re.findall(r''+match,line)
            if (t):
                #print(item)
                #print(line_num)
                g.writelines(line)
            if not line:
                break
        f.close()
    g.close()


#new_exist = strip(exist_arr)
#new_cin = strip(cin_arr)
#new_ebv = strip(ebv_arr)
#new_gs = strip(gs_arr)
#new_msi = strip(msi_arr)
new_male = strip(male_arr)
new_female = strip(female_arr)
'''
extract(f,new_exist,out_dir)
extract(f,new_cin,cin_dir)
extract(f,new_gs,gs_dir)
extract(f,new_msi,msi_dir)
extract(f,new_ebv,ebv_dir)
'''
extract(f,new_male,male_dir)
extract(f,new_female,female_dir)
