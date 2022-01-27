#%% 决策树模型
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd
import graphviz
from IPython.display import display,SVG
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

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
wine = load_wine()
data_X = wine.data
data_Y = wine.target

train_X,test_X,train_Y,test_Y = train_test_split(data_X,data_Y,test_size=0.3,random_state=11)

#%% 决策树模型
clf = tree.DecisionTreeClassifier(criterion="entropy",random_state=6,splitter="best",max_depth=3)
clf.fit(train_X,train_Y)
score = clf.score(test_X,test_Y)

print("score:{}".format(score))

#%% 决策树可视化
feature_name = wine.feature_names
target_name = wine.target_names

dot_data = tree.export_graphviz(clf,out_file=None,feature_names=feature_name,class_names=target_name,filled=True,rounded=True)

graph = graphviz.Source(dot_data)

display(SVG(graph.pipe(format="svg")))
# %% 特征重要性
[*zip(feature_name,clf.feature_importances_)]


#%% 测试
test_leaf_index=clf.apply(test_X)
predict_Y=clf.predict(test_X)

# %% 学习曲线
matplotlib.rc('font',family='MicroSoft YaHei',weight='bold')
plot_learning_curve(clf,u"学习曲线",test_X,test_Y,n_jobs=8)

#%%
