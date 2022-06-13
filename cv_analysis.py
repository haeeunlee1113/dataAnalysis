#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


pip install scikit-learn


# In[4]:


from scipy import stats
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import datasets
from sklearn import metrics
import types
from sklearn.manifold import TSNE


# In[5]:


pip install plotly


# In[6]:


import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


sns.set(style="darkgrid", palette="bright", font_scale=1.5)


# In[8]:


df= pd.read_csv("./Countries-GDP-Data.csv")



print (df['Net migration'].values[2])


for column_name in df:
    if(df[column_name].dtypes =='object'):
        df[column_name]= df[column_name].str.replace(',','.')
        if(df[column_name].str.contains('A').any()==False):
            df[column_name] = pd.to_numeric(df[column_name])


# In[9]:


df.tail(100)


# In[10]:


sns.displot(df['Population'], height = 125, aspect = 3)


# In[11]:


#상관계수? y=ax절대적으로 비례한다는 것이 아니라
# 하나가 증가하면 하나가 감소하는 경향성이 있다 라는 뜻

corrmat =df.corr()
print(corrmat)


# In[12]:


sns.color_palette("Paired")
sns.set(rc = {'figure.figsize':(15, 8)})
sns.heatmap(corrmat,vmax=.9, annot = True, square=True,cmap = "RdYlBu_r", center = 0)


# In[13]:


data = dict(type = 'choropleth', locations= df['Country'], locationmode= 'country names', z=df['Population'],
           text=df['Country'], colorbar= {'title' :'Population '})

layout = dict(title='gdp 2021', geo = dict(showframe=False))

choromap3 = go.Figure(data=[data],layout = layout)
iplot(choromap3)


# In[15]:


corrmat= df.corr()
mask= np.zeros_like(corrmat,dtype = np.bool_)
mask[np.triu_indices_from(mask)] = True
plt.figure(figsize=(15,15))
sns.heatmap(corrmat,vmax=.9, annot = True, square=True,cmap = "RdYlBu_r", center = 0,mask = mask)


# In[16]:


print(np.mean(df))


# In[17]:


#df_s = df['Area (sq. mi.)']
df_f = df.fillna(df.mean())
df_f.tail(80)


# In[18]:


print(np.mean(df))


# In[19]:


stats.kendalltau(df_f['Population'], df_f['GDP ($ per capita)'])
#stats.pearsonr(df_f['Population'], df_f['GDP ($ per capita)'])

#crops
#population


# In[ ]:


import statsmodels.formula.api as smf
from sklearn.datasets import load_boston


# In[ ]:


pip install statsmodels


# In[ ]:




