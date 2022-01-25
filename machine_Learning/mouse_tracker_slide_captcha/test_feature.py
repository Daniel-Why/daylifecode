#特征筛选
#计算轨迹特征

#%%
import os
import pickle
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.feature_selection import VarianceThreshold,SelectKBest,f_classif,chi2,SelectFromModel


os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
mouse_data = np.load(".\clean_data\clean_data_step_03.npy")
mouse_X = mouse_data.T[1:].T # 特征数据
mouse_Y= mouse_data.T[0].T   # 分类结果

#Variance_data = VarianceThreshold().fit_transform(mouse_data)
#SelectKBest_data = SelectKBest(chi2,k=2).fit_transform(mouse_data,mouse_Y)

f2=open("model.pickle","rb")
clf=pickle.loads(f2.read())
selectFromModel_data = SelectFromModel(clf).fit_transform(mouse_data,mouse_Y)


#%%