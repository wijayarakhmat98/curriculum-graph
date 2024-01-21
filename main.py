#!/usr/bin/env python3.11

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output

dfa = pd.read_csv('mata-kuliah-clean.csv')
dfb = pd.read_csv('prasyarat-clean.csv')

# print(dfa.to_string())
# print(dfb.to_string())

dfc = dfa.copy()
dfc.loc[dfc['category'] == 'MAIN', 'category'] = 'DEPT'
dfc['name'] = dfc['name'] + ' ' + dfc['category'] + ' ' + dfc['code']
dfc['length'] = 1
dfc['end'] = dfc['semester'] + dfc['length']
dfc = dfc.sort_values(['semester', 'credits'])

# print(dfc.to_string())

categories = dfc['category'].unique()
# print(categories)

def move(df, code):
	if df.loc[df['code'] == code].iloc[0]['moved']:
		return
	df.loc[df['code'] == code, 'semester'] += 2
	df.loc[df['code'] == code, 'moved'] = True
	for require in dfb.loc[dfb['require'] == code, 'code']:
		move(df, require)

df5 = dfc.copy()
df5['moved'] = False
for code in df5.loc[df5['semester'] == 5, 'code']:
	move(df5, code)

df7 = dfc.copy()
df7['moved'] = False
for code in df7.loc[df7['semester'] == 7, 'code']:
	move(df7, code)

# dfc = dff

app = Dash(__name__)
app.layout = html.Div([
	dcc.Checklist(categories, categories, id='category', style={'fontSize': '20px'}, inline=True),
	dcc.RadioItems(['Tidak IISMA', 'IISMA Semester 5', 'IISMA Semester 7'], 'Tidak IISMA', id='iisma', style={'fontSize': '20px'}, inline=True),
	dcc.Graph(id='graph')
])

@app.callback(
	Output('graph', 'figure'),
	Input('category', 'value'),
	Input('iisma', 'value')
)
def filter(category, iisma):
	# print(category)

	if 'IISMA Semester 5' == iisma:
		df = df5.copy()
	elif 'IISMA Semester 7' == iisma:
		df = df7.copy()
	else:
		df = dfc.copy()
	df = df[df['category'].isin(category)]
	df = df.reset_index()
	df = df.drop(columns=['index'])

	dfd = df.groupby('semester').size()
	dfe = df.groupby('semester').apply(lambda group: group.reset_index().iloc[0]['index'], include_groups=False)

	# print(dfd)
	# print(dfe)

	# print(df.shape[0])

	fig = px.timeline(df, x_start="semester", x_end="end", y="name", height=df.shape[0] * 20)
	fig.update_layout(xaxis_dtick=1)
	fig.update_layout(xaxis_type='linear')
	fig.update_layout(yaxis_dtick=1)
	fig.update_yaxes(autorange="reversed") 
	fig.data[0].x = df['length'].to_list()

	for i, row in dfb.iterrows():
		color = 'orange'
		c = df.loc[df['code'] == row['code']].reset_index().to_dict(orient='records')
		r = df.loc[df['code'] == row['require']].reset_index().to_dict(orient='records')
		if len(c) == 0 or len(r) == 0:
			continue
		c = c[0]
		r = r[0]
		offset = (r['index'] - dfe[r['semester']]) / dfd[r['semester']] * 0.8 + 0.1
		fig.add_shape(type='line', x0=r['semester'] + offset, y0=r['index'], x1=r['semester'] + offset, y1=c['index'], line={'color': color})
		fig.add_shape(type='line', x0=r['semester'] + offset, y0=c['index'], x1=c['semester'], y1=c['index'], line={'color': color})

	return fig

app.run_server(debug=True)

print('Hello, world!')
