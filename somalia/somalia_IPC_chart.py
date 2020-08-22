#!/usr/local/bin/python3
"""
Plot the % Population of Somalia that are categorized in each IPC level over
time.
The IPC (Integrated Food Security Phase Classification) has 5 levels:
    Level 1: Minimal - Level 2: Stressed - Level 3: Crisis - Level 4: Emergency
    - Level 5: Famine
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-white')

# input_file = 'Dev/IPC Population Figures.xlsx'
input_file = 'IPC Population Figures Tracking Sheet.xlsx'
country = "Somalia"
max_pop = 15500000
col_heads = ['country', 'pop', 'date', 'rev_pop', '%pop', 'period',
             'IPC1-pop', 'IPC1-%rev_pop', 'IPC2-pop', 'IPC2-%rev_pop',
             'IPC3-pop', 'IPC3-%rev_pop', 'IPC4-pop', 'IPC4-%rev_pop',
             'IPC5-pop', 'IPC5-%rev_pop', 'IPC3>-pop', 'IPC3>-%rev_pop']


# plot_cols = ['date', 'IPC1-pop', 'IPC2-pop', 'IPC3-pop', 'IPC4-pop',
#              'IPC5-pop']

plot_cols = ['date', 'IPC1-pop']

excel_dump_df = pd.read_excel(input_file, header=[2], usecols="B,D:T")
# print(excel_dump_df.head())
print(excel_dump_df.columns)
somalia_ipc = excel_dump_df.loc[excel_dump_df['Country'] == country]
# print("columns:", len(somalia_ipc.columns), "rows:", len(somalia_ipc.index))
print(somalia_ipc)
somalia_ipc.columns = col_heads
print(somalia_ipc)
print(somalia_ipc.loc[:, 'period'])
somalia_ipc_chart = somalia_ipc[plot_cols].copy()
print(somalia_ipc_chart)

for idx, row in somalia_ipc_chart.iterrows():
    dt = row['date'].to_pydatetime()
    print('month:', dt.month, type(dt.year), 'year:', dt.year, type(dt.year))
    dt_str = str(dt.month).capitalize() + '-' + str(dt.year)
    print(dt_str, type(dt_str))
    somalia_ipc_chart.ix[idx, 'date'] = dt_str

print(somalia_ipc_chart)

somalia_ipc_chart = somalia_ipc_chart.set_index('date')

print(somalia_ipc_chart)

somalia_ipc_chart = somalia_ipc_chart.transpose()

print(somalia_ipc_chart)

# ============================

# somalia_ipc_chart.plot.hist(grid=True, alpha=0.5,  # normed=True,
#                             histtype='stepfilled', rwidth=0.9,
#                             edgecolor='none')  # color='steelblue',

# plt.title('Somalia IPC Level Population Count')
# plt.xlabel('IPC Level')
# plt.ylabel('Population')
# # plt.xticks(somalia_ipc_chart['date'])
# plt.grid(axis='y', alpha=0.75)
# # plt.text(23, 45, r'$\mu=15, b=3$')


# =============================


sns.set(style="whitegrid")

g = sns.catplot(data=somalia_ipc_chart,
                kind="bar", palette="muted")

# g = sns.relplot(kind="line", data=somalia_ipc_chart)

g.despine(left=True)
g.set_ylabels("survival probability")


# ==============================

# sns.kdeplot(somalia_ipc_chart, shade=True)

# chart = sns.load_dataset(somalia_ipc_chart)
# ax = sns.lineplot(data=chart)

# x = np.linspace(0, 10, 100)

# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))

# plt.savefig('Dev/fig.png')

# fig, ax = plt.subplots(2)
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.cos(x))

# data = np.random.rand(1000)

# plt.hist(data)
# plt.hist(data, bins=30, normed=True, alpha=0.5, histtype='stepfilled',
#          color='steelblue', edgecolor='none')

plt.show()  # should be used only once in a script
