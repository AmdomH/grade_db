# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:13:08 2022

@author: hp
"""

import pandas as pd 

hmw = {'ex1':100,
            'ex2':51,
            'ex3':92, 
            'ex4':68,
            'ex5':83}

df = pd.Series(data=hmw)
print(df.describe() )

def homework(di):
    total = 0
    count=0 
    for ex, grades in di.items():
        count+=1
        total +=grades 
    return f"Average grade for this is assignment is:{total/count}"

print(homework(hmw))

a = 20191001


print(pd.to_datetime(pd.Series([str(a)]), format="%Y-%m-%d"))
