#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:11:58 2018

@author: frank-lsy
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def read_csv(input_csv):
    return pd.read_csv(input_csv)

facet = ["cin","ebv","msi","gs","not-classified","male","female"]

cin = read_csv("../sig-count/{}.csv".format(facet[0]))
ebv = read_csv("../sig-count/{}.csv".format(facet[1]))
msi = read_csv("../sig-count/{}.csv".format(facet[2]))
gs = read_csv("../sig-count/{}.csv".format(facet[3]))
no = read_csv("../sig-count/{}.csv".format(facet[4]))
male = read_csv("../sig-count/{}.csv".format(facet[5]))
female = read_csv("../sig-count/{}.csv".format(facet[6]))

facets = [cin,ebv,msi,gs,no,male,female]

#print(ebv)
#print(cin_list)

def draw(input_type,pos):
    #print(input_type)
    for i in range(len(input_type)):
    #print(cin["Signature"][i])
        if (i==0):
            plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],fc = "#4169e1")

        
        else:
            if (input_type["Signature"][i]=='sig2'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#ff8c00")

                
            elif (input_type["Signature"][i]=='sig3'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#ee2c2c")

                
            elif (input_type["Signature"][i]=='sig6'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#2e8b57")
            
            
            elif (input_type["Signature"][i]=='sig10'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#ffff00")

                
            elif (input_type["Signature"][i]=='sig17'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#cd00cd")

                
            elif (input_type["Signature"][i]=='sig15'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#8b8b00")

                
            elif (input_type["Signature"][i]=='sig21'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#8b4513")

                
            elif (input_type["Signature"][i]=='sig24'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#ff00ff")

                
            elif (input_type["Signature"][i]=='sig28'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#8b8386")

                
            elif (input_type["Signature"][i]=='sig30'):
                plt.bar(pos,input_type["Amount"][i],label=input_type["Signature"][i],bottom=sum(input_type["Amount"][:i]),fc="#00ced1")

        #plt.legend()    
        #plt.xlabel("Type")
    my_y_ticks = np.arange(0,350,10)
        #print(my_y_ticks)
    plt.yticks = (my_y_ticks)
    #print(plt.yticks)
    plt.ylim(0,350)
        #plt.yscale('log')
    plt.minorticks_on()
    plt.ylabel("Amount")
    plt.xticks=(np.arange(5), ("cin","ebv","msi","gs","not-classified"))
    plt.gca().set_xticks([])
    #plt.show()
        
for i in range(1,6):
    pos = i
    input_type = facets[i-1]
    draw(input_type,pos)
    plt.savefig("../sig-fig.png",dpi = 2560)