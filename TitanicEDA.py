# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:29:27 2020

@author: athye
"""

import pandas as pd

data = pd.read_csv("C://Users//athye//OneDrive//MSDS//MSDS 422//M1//train.csv")

print(data['Pclass'].describe())

print(data['Age'].describe())