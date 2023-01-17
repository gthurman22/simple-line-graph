#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd

y = {'f(x)' : [2,10,6,8], 'g(x)': [4,2,-2,6]}
x = [1,2,3,4]

graph = pd.DataFrame(y,x)
graph.plot(kind='line', grid =True, title="my graph", ylabel="my y title", xlabel="my x title") 


# In[ ]:




