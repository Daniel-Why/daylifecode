# 测试集
#%%
from re import split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split,learning_curve
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import pickle
import os
from model_learning_curve import plot_learning_curve
# 绘图
def pic_print(data_arrary,target_arrary,pic_shape="3D"):
    mouse_ALL = np.c_[target_arrary,data_arrary]#将特征数据和分类结果数据组合子在一起
    mouse_obj = pd.DataFrame(mouse_ALL)
    mouse_negative = mouse_obj.loc[mouse_obj[0] == 0][[1,2,3]] #反向结果
    mouse_positive = mouse_obj.loc[mouse_obj[0] == 1][[1,2,3]] #正向结果
    # 绘制 3D 图
    if pic_shape == "3D":
        ax = plt.figure("mouse 3D",dpi=100,figsize=(10,10)).add_subplot(111,projection="3d")
        ax.scatter(mouse_positive[1],mouse_positive[2],mouse_positive[3],s=15,marker='o',c="red")
        ax.scatter(mouse_negative[1],mouse_negative[2],mouse_negative[3],s=15,marker='x',c="black") 
    # 绘制 2D 图     
    elif pic_shape == "2D":
        plt.scatter(mouse_positive[1],mouse_positive[2],marker='o',s=20,c="red")
        plt.scatter(mouse_negative[1],mouse_negative[2],marker='x',s=15,c="black")
    plt.show()



################################################## 主函数 ###############################################

#%% 导入数据，将数据分为特征数据和分类结果
os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
mouse_data = np.load(r".\clean_data\test_data.npy")
mouse_X = mouse_data.T[1:].T # 特征数据
mouse_Y= mouse_data.T[0].T   # 分类结果

f2=open(r"mouse_tracker_model.pickle","rb")
clf=pickle.load(f2)

#%% 利用模型进行预测
clf_y_predict = clf.predict(mouse_X) #得到测试结果

# 绘制预测图
pic_print(mouse_X,clf_y_predict,pic_shape="3D")

#绘制真实值
pic_print(mouse_X,mouse_Y,pic_shape="3D")

#%% 计算模型分值
score = clf.score(mouse_X,mouse_Y)
print(score)

#%%
#比较预测值的正确性，并绘图
new_result_ALL = np.c_[mouse_Y,clf_y_predict,mouse_X] #将真实值、预测值和特征数据合并位一个数组
new_result_obj = pd.DataFrame(new_result_ALL)
new_result_negative = new_result_obj.loc[new_result_obj[0] != new_result_obj[1]][[2,3,5]]#提取识别错误的数据
new_result_positive = new_result_obj.loc[new_result_obj[0] == new_result_obj[1]][[2,3,5]]#提取识别正确的数据
ax = plt.figure("mouse 3D",dpi=100,figsize=(10,10)).add_subplot(111,projection="3d")
ax.scatter(new_result_positive[3],new_result_positive[2],new_result_positive[5],s=15,marker='o',c="red")
ax.scatter(new_result_negative[3],new_result_negative[2],new_result_negative[5],s=15,marker='x',c="black")
plt.show()


# %% 学习曲线
matplotlib.rc('font',family='MicroSoft YaHei',weight='bold')
plot_learning_curve(clf,u"学习曲线",mouse_X,mouse_Y,n_jobs=8)

# %%