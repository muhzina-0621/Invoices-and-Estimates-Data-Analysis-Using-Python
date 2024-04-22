import numpy as np
import pandas as pd
from pyspark.sql.functions import udf
from pyspark.sql.functions import *


data1=pd.read_csv("Estimates.csv")
data2=pd.read_csv("Invoices.csv")

def mask_customer(name):
    if len(name) <= 2:
        return name  # If the name has 2 or fewer characters, no masking is applied
    else:
        return name[0] + '*' * (len(name) - 2) + name[-1]  
    
data1['Customer Name'] = data1['Customer Name'].apply(mask_customer)
data2['Customer Name'] = data2['Customer Name'].apply(mask_customer)

data1.to_csv('data1_masked.csv', index=False)
data2.to_csv('data2_masked.csv', index=False)