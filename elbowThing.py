# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:55:42 2017



@author: DHendricks
"""
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
pi,sin,cos,tan = sp.pi,sp.sin,sp.cos,sp.tan

from scipy.signal import savgol_filter, detrend
savCoeff = 201

aa = sp.linspace(0,10,1000)
bb = sp.tanh(aa/1.5-.5)*5 + .7 + sp.rand(len(aa))*.5
bb = savgol_filter(bb,savCoeff,3,deriv = 0)

mbb = (bb[-1]-bb[0])/(aa[-1]-aa[0])
linebb = mbb*aa+bb[0]
bbNoTrend = bb-linebb
bb = bbNoTrend ######################

cc = savgol_filter(bb,savCoeff,3,deriv=1)
dd = savgol_filter(cc,savCoeff,3,deriv=1)
#%%

bbb = sp.tanh(aa/1.5-.5)*4 + 1.7 + sp.rand(len(aa))*.5
bbb = savgol_filter(bbb,savCoeff,3,deriv = 0)

mbbb = (bbb[-1]-bbb[0])/(aa[-1]-aa[0])
linebbb = mbbb*aa+bbb[0]
bbbNoTrend = bbb-linebbb
bbb = bbbNoTrend #####################

ccc = savgol_filter(bbb,savCoeff,3,deriv=1)
ddd = savgol_filter(ccc,savCoeff,3,deriv=1)

p1 = 3
plt.figure(1,facecolor = 'w')
plt.clf()
plt.subplot(p1, 1, 1)
plt.plot(aa,bb)
plt.plot(aa,bbNoTrend)
plt.plot(aa,bbb)
plt.plot(aa,bbbNoTrend)

plt.grid()
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.subplot(p1, 1, 2)
plt.plot(aa,cc)
plt.plot(aa,ccc)
plt.grid()
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.subplot(p1, 1, 3)
plt.plot(aa,dd)
plt.plot(aa,ddd)
plt.grid()
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
