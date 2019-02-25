#!/usr/bin/env python
# coding: utf-8

# In[35]:


import panel as pn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [-1,1]
def function(x, Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5/9
    return Celsius

def function_plt(Fahrenheit=100):
    y = function(x, Fahrenheit)
    fig = plt.figure()
    plt.xticks(ticks=[-1, 1], labels=["Fahrenheit", "Celsius"])
    plt.bar(x[0], Fahrenheit)
    plt.bar(x[1], y)
    plt.text(x[0], Fahrenheit, Fahrenheit)
    plt.text(x[1], y, int(y))
    plt.close()
    return fig
    
pn.extension()
pn.interact(function_plt)

