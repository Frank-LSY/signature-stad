#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:11:27 2018

@author: frank-lsy
"""
import csv
import sh

def summarize(input_csv,output_csv):
    f = open(input_csv,'r')
    reader = csv.reader(f)
    signatures = [row[1] for row in reader]
    f.close()
    sig_count = {'sig1' : 0,'sig2' : 0,'sig3' : 0,
                 'sig4' : 0,'sig5' : 0,'sig6' : 0,
                 'sig7' : 0,'sig8' : 0,'sig9' : 0,
                 'sig10' : 0,'sig11' : 0,'sig12' : 0,
                 'sig13' : 0,'sig14' : 0,'sig15' : 0,
                 'sig16' : 0,'sig17' : 0,'sig18' : 0,
                 'sig19' : 0,'sig20' : 0,'sig21' : 0,
                 'sig22' : 0,'sig23' : 0,'sig24' : 0,
                 'sig25' : 0,'sig26' : 0,'sig27' : 0,
                 'sig28' : 0,'sig29' : 0,'sig30' : 0}
    
    for signature in signatures:
        sig_count[signature] += 1 
        
    g = open(output_csv,'a+')
    g.writelines("Signature,Amount\n")
    for key,value in sig_count.items():
        if (value!=0):
            g.writelines(key+','+str(value)+'\n')
    g.close()
    return sig_count

facets = ["male","female"]
#sh.mkdir("-pv","../sig-count")

for facet in facets:    
    count = summarize("../signature/{}.csv".format(facet),"../sig-count/{}.csv".format(facet))    
    print(count)