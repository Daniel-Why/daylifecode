# 计算如何合理利用汉堡王券
import itertools,time
def listcount(para_list):#兑换的食品种类数量
    n0 = para_list.count(0)
    n = len(para_list)-n0
    return n
def num_sum(para_list):#兑换的食品数量
    num = 0
    for i in para_list:
        num += i
    return num 

def para(count,l):#枚举出l种食品，每种食品最多兑换count个的列表
    b = []
    for j in range(count):
        b.append(j)
    a = itertools.product(b, repeat=l)
    return a

k_dict = {'huafu':39,'pi':88,'xindi':129,'qipao':140,'niupai':145,"ala":149,'jk':149,'jt':150,'jtiao':160,'jtb':215,'hb':230}#可兑换的食品种类和积分
len_dict = len(k_dict)#可兑换的食品种类梳理
k_limit = 246 # 当前拥有积分
kv_list = [] 
result_list = []
for i in k_dict.values(): #可兑换食品的积分列表
    kv_list.append(i)
k = 0
para_list_all=para(6,len_dict)

t1 = time.time()
for para_list in para_list_all:
    #print(para_list)
    result_dict = {'num_list':None,'k':0,'num':0,'type':0} #兑换方法结果：每个食品兑换个数列表，兑换总积分，兑换食品的总数，兑换食品的种类数
    for n in range(len_dict):
        kn = kv_list[n]*para_list[n] #兑换总积分计算
        k = k+kn
        if k > k_limit: #若计算超过当前拥有积分则跳出循环
            #print(k)
            break
    if k <=k_limit: #若计算低于当前积分，则进一步处理
        the_resul_dict=result_dict.copy()
        the_resul_dict['num_list']=para_list
        the_resul_dict['k']=k
        the_resul_dict['num']=num_sum(para_list)
        the_resul_dict['type']=listcount(para_list)
        print(the_resul_dict) #打印结果
        #result_list.append(the_resul_dict)
    k =0
t2 = time.time()

delta_t = t2-t1
print(delta_t)
# print(result_list)
