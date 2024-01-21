#!/usr/bin/env python3.11

import pandas as pd

dfa = pd.read_excel('Mata Kuliah Prerequisites.xlsx')
dfb = pd.read_excel('Mata Kuliah All.xlsx')[['Code', 'Name']]

# print(dfa.to_string())
# print(dfb.to_string())

dfc = pd.merge(dfa, dfb, left_on='Code', right_on='Code')
dfc = pd.merge(dfc, dfb, left_on='Require', right_on='Code')
dfc.columns = ['code_a', 'code_b', 'name_a', 'name_b', 'sanity_a', '', 'sanity_b']
dfc = dfc[['code_a', 'name_a', 'sanity_a', 'code_b', 'name_b', 'sanity_b']]
dfc['equal_a'] = dfc['name_a'] == dfc['sanity_a']
dfc['equal_b'] = dfc['name_b'] == dfc['sanity_b']

print(dfc.to_string())

print('Hello, world!')
