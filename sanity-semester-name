#!/usr/bin/env python3.11

import pandas as pd

dfa = pd.read_excel('Mata Kuliah by Semester.xlsx')
dfa = dfa[dfa['Kode'].notna()]
dfa['Kode'] = dfa['Kode'].str.replace(r'\*$', '', regex=True)
dfa.columns = ['code_a', 'name_a', 'weight_a', 'semester_a', 'category_a']

dfb = pd.read_excel('Mata Kuliah All.xlsx')[['Code', 'Category', 'Credits', 'Semester', 'Name']]
# dfb = pd.read_excel('Mata Kuliah Fixed.xlsx')[['Code', 'Category', 'Credits', 'Semester', 'Name']]
dfb.columns = ['code_b', 'category_b', 'weight_b', 'semester_b', 'name_b']

# print(dfa.to_string())
# print(dfb.to_string())

dfc = pd.merge(dfa, dfb, left_on='code_a', right_on='code_b', how='outer')
dfc['sanity_name'] = dfc['name_a'] == dfc['name_b']
dfc['sanity_weight'] = dfc['weight_a'] == dfc['weight_b']
dfc['sanity_semester'] = dfc['semester_a'] == dfc['semester_b']
dfc = dfc[['code_a', 'code_b', 'name_a', 'name_b', 'sanity_name', 'weight_a', 'weight_b', 'sanity_weight', 'semester_a', 'semester_b', 'sanity_semester', 'category_a', 'category_b']]

# print(dfc.to_string())

dfd = dfc[dfc['code_a'].notna() & dfc['code_b'].notna()]

print(dfd.to_string())

print('Hello, world!')
