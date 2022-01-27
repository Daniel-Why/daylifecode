#%%
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split,learning_curve
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle


def pic_print(data_arrary,target_arrary,pic_shape="3D"):
    cancer_ALL = np.c_[target_arrary,data_arrary]
    cancer_obj = pd.DataFrame(cancer_ALL)
    cancer_negative = cancer_obj.loc[cancer_obj[0] == 0][[1,2,3]]
    cancer_positive = cancer_obj.loc[cancer_obj[0] == 1][[1,2,3]]
    if pic_shape == "3D":
        ax = plt.figure("cancer 3D",dpi=100,figsize=(10,10)).add_subplot(111,projection="3d")
        ax.scatter(cancer_positive[1],cancer_positive[3],cancer_positive[2],s=15,marker='o',c="red")
        ax.scatter(cancer_negative[1],cancer_negative[3],cancer_negative[2],s=15,marker='x',c="black")      
    elif pic_shape == "2D":
        plt.scatter(cancer_positive[1],cancer_positive[2],marker='o',s=20,c="red")
        plt.scatter(cancer_negative[1],cancer_negative[2],marker='x',s=15,c="black")
    plt.show()





#%%
cancer = datasets.load_breast_cancer()
cancer_X = cancer.data
cancer_Y = cancer.target
#print(type(cancer_X))
#print(cancer_X.shape)
#print(type(cancer_Y))
#print(cancer_Y.shape)


#%%
#pic_print(cancer_X,cancer_Y,pic_shape="3D")


#%%

X_train,X_test,Y_train,Y_test=train_test_split(cancer_X,cancer_Y,test_size=0.3)


#%%
pic_print(X_train,Y_train,pic_shape="3D")
#%% 逻辑回归模型
clf = LogisticRegression(penalty="l1",max_iter=5000,solver="liblinear",multi_class="ovr",n_jobs=4)
clf.fit(X_train,Y_train)

#%%
clf_y_predict = clf.predict(X_test)
#print(clf_y_predict)
#%%
# 预测值
pic_print(X_test,clf_y_predict,pic_shape="3D")

#%%
#真实值
pic_print(X_test,Y_test,pic_shape="3D")
#%%
score = clf.score(X_test,Y_test)
print(score)

#%%
#比较
new_result_ALL = np.c_[Y_test,clf_y_predict,X_test]
new_result_obj = pd.DataFrame(new_result_ALL)
new_result_negative = new_result_obj.loc[new_result_obj[0] != new_result_obj[1]][[2,3,4]]
new_result_positive = new_result_obj.loc[new_result_obj[0] == new_result_obj[1]][[2,3,4]]
ax = plt.figure("cancer 3D",dpi=100,figsize=(10,10)).add_subplot(111,projection="3d")
ax.scatter(new_result_positive[2],new_result_positive[4],new_result_positive[3],s=15,marker='o',c="red")
ax.scatter(new_result_negative[2],new_result_negative[4],new_result_negative[3],s=15,marker='x',c="black")
plt.show()


# %% [markdown]
# 保存模型
# %%
with open("model.pickle","wb") as f:
    pickle.dump(clf,f)
print("保存成功")

