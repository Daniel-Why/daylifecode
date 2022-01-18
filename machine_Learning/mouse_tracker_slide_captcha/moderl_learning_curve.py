#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pickle
from sklearn.model_selection import learning_curve
import os

# 绘制学习曲线
def plot_learning_curve(estimator,title,X,y,ylim=None,cv=None,n_jobs =1,train_sizes=np.linspace(.05,1.,20),verbose=0,plot=True):
    '''
    estimator:模型
    X:输入特征数据
    y:分类结果 
    '''

    # learning_curve 跑学习曲线数据，训练集大小、训练分数、验证得分
    train_sizes,train_scores,test_scores = learning_curve(estimator,X,y,cv=cv,n_jobs=n_jobs,train_sizes=train_sizes,verbose=verbose)

    # mean:每一行的平均值；std：每一行的标准差
    train_scores_mean = np.mean(train_scores,axis=1)
    train_scores_std = np.std(train_scores,axis=1)
    test_scores_mean = np.mean(test_scores,axis=1)
    test_scores_std = np.std(test_scores,axis=1)

    # 绘图
    if plot:
        plt.figure()
        plt.title(title)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.xlabel(u"训练样本数")
        plt.ylabel(u"得分")

        # #plt.gca().invert_yaxis()Y轴逆序

        plt.grid() #显示网格线

        # train_sizes 横坐标，train_scores_mean - train_scores_std,train_scores_mean + train_scores_std 展示误差偏离，即图上的色块范围
        plt.fill_between(train_sizes,train_scores_mean - train_scores_std,train_scores_mean + train_scores_std,alpha = 0.1,color = "b")
        plt.fill_between(train_sizes,test_scores_mean - test_scores_std,test_scores_mean + test_scores_std,alpha = 0.1,color = "r")

        # train_sizes 横坐标，train_scores_mean 得分平均值，即点线
        plt.plot(train_sizes,train_scores_mean,'o-',color='b',label=u'训练集上得分')
        plt.plot(train_sizes,test_scores_mean,'o-',color='r',label=u'交叉验证集上得分')

        plt.legend(loc="best")#图例，loc为图例位置，best代表随机选最好的位置
        plt.draw()

#%%
'''
os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")

# plot 展示中文字体
matplotlib.rc('font',family='MicroSoft YaHei',weight='bold')

# 打开模型
with open("mouse_tracker_model.pickle","rb") as nf:
    bc_model = pickle.load(nf)

# 获取 sklearn cancer数据集
mouse_data = np.load(".\clean_data\clean_data_step_03.npy")
mouse_X = mouse_data.T[1:].T # 特征数据
mouse_Y= mouse_data.T[0].T   # 分类结果

# 绘制学习曲线
plot_learning_curve(bc_model,u"学习曲线02",mouse_X,mouse_Y,n_jobs=8)

'''
#%%