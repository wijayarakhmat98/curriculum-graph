#!/usr/bin/env python3.11

import pandas as pd

dfa = pd.read_excel('Mata Kuliah All.xlsx')[['Code', 'Requires', 'Name']]
dfb = pd.read_excel('Mata Kuliah Prerequisites.xlsx')

# print(dfa.to_string())
# print(dfb.to_string())

dfc = pd.merge(dfa, dfb[['Code', 'Prerequisite']], left_on='Code', right_on='Code', how='left')
dfc.rename(columns={'Prerequisite': 'Sanity Requires'}, inplace=True)
dfc.loc[dfc['Sanity Requires'].notna(), 'Sanity Requires'] = 1

# print(dfc.to_string())

dfd = dfc.groupby('Code', as_index=False)[['Sanity Requires']].sum()
dfd = pd.merge(dfa, dfd, left_on='Code', right_on='Code')
dfd['Equal Requires'] = dfd['Requires'] == dfd['Sanity Requires']
dfd = dfd[['Code', 'Name', 'Requires', 'Sanity Requires', 'Equal Requires']]

print(dfd.to_string())

print('Hello, world!')
