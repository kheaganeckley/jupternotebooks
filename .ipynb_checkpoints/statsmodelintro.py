#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'notebooks'))
	print(os.getcwd())
except:
	pass

#%%
import numpy as numpy
import pandas as pandas


#%%
df = pandas.read_csv("/home/kheagan/Documents/programing/juypter/TSA/UDEMY_TSA_FINAL/Data/macrodata.csv", index_col=0, parse_dates=True)


#%%
df.head()


#%%
df['realgdp'].plot()


#%%
from statsmodels.tsa.filters.hp_filter import hpfilter


#%%
gdp_cycle, gdp_trend =hpfilter(df['realgdp'], lamb=1600)


#%%
gdp_trend.plot()


#%%
gdp_cycle.plot()


#%%
df['trend']=gdp_trend
df.head()


#%%
df[['trend','realgdp']].plot()


