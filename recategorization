#!/usr/bin/env python3.11

import pandas as pd

dfa = pd.read_excel('Mata Kuliah Fixed.xlsx')
dfa.columns = ['code_a', 'category_a', 'credits_a', 'semester_a', 'requires_a', 'name_a']

dfb = pd.read_excel('Mata Kuliah by Semester.xlsx')
dfb = dfb[dfb['Kode'].notna()]
dfb['Kode'] = dfb['Kode'].str.replace(r'\*$', '', regex=True)
dfb.columns = ['code_b', 'name_b', 'credits_b', 'semester_b', 'category_b']

# print(dfa.to_string())
# print(dfb.to_string())

dfc = pd.merge(dfa, dfb, left_on='code_a', right_on='code_b', how='outer')

# print(dfc.to_string())

dfd = dfc[['code_a', 'name_a', 'semester_a', 'credits_a', 'category_a', 'category_b', 'requires_a']]
dfd.loc[dfc['code_a'].isna(), 'code_a'] = dfc.loc[dfc['code_a'].isna(), 'code_b']
dfd.loc[dfc['name_a'].isna(), 'name_a'] = dfc.loc[dfc['name_a'].isna(), 'name_b']
dfd.loc[dfc['semester_a'].isna(), 'semester_a'] = dfc.loc[dfc['semester_a'].isna(), 'semester_b']
dfd.loc[dfc['credits_a'].isna(), 'credits_a'] = dfc.loc[dfc['credits_a'].isna(), 'credits_b']
dfd.loc[dfd['requires_a'].isna(), 'requires_a'] = 0
dfd.loc[dfd['category_a'].isna(), 'category_a'] = 'UPMB'
dfd.loc[dfd['code_a'] == 'KM184801', 'category_a'] = 'MAT'

# print(dfd.to_string())

dfe = dfd.copy()
dfe['category'] = dfe['category_a']
dfe.loc[dfe['category'] == 'MAT', 'category'] = dfe.loc[dfe['category'] == 'MAT', 'category_b']
dfe.loc[dfe['category'].isna(), 'category'] = 'OTHER'

# print(dfe.to_string())

dff = dfe[['code_a', 'credits_a', 'semester_a', 'category', 'name_a']]
dff.columns = ['code', 'credits', 'semester', 'category', 'name']
dff = dff.astype({
	'code': pd.StringDtype(),
	'credits': pd.UInt8Dtype(),
	'semester': pd.UInt8Dtype(),
	'category': pd.CategoricalDtype(),
	'name': pd.StringDtype()
})

print(dff.to_string())
print(dff.info())

dfg = pd.read_excel('Mata Kuliah Prerequisites.xlsx')[['Code', 'Require']]
dfg = dfg[dfg['Require'].notna()]
dfg.columns = ['code', 'require']
dfg = dfg.astype({
	'code': pd.StringDtype(),
	'require': pd.StringDtype()
})

print(dfg.to_string())
print(dfg.info())

dff.to_csv('mata-kuliah-clean.csv', index=False)
dfg.to_csv('prasyarat-clean.csv', index=False)

print('Hello, world!')
