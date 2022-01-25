from cmath import nan
import numpy as np
import math 

trace=[[1,1,2],[1,2,3],[1,1,4]]
trace = np.array(trace)
if len(trace.T[0]) >=3 :
    
    adj_point_angle_list = []
    for i in range(1,len(trace.T[0])-1):
        a = ((trace[i+1][0]-trace[i-1][0])**2+(trace[i+1][1]-trace[i-1][1])**2)**0.5 #三角形底边
        b = ((trace[i][0]-trace[i-1][0])**2+(trace[i][1]-trace[i-1][1])**2)**0.5 #前相邻点距离
        c = ((trace[i+1][0]-trace[i][0])**2+(trace[i+1][1]-trace[i][1])**2)**0.5 #后相邻点距离
        r =(a*a-b*b-c*c)/(2*b*c)
        angle_A = math.degrees(math.acos((a*a-b*b-c*c)/(2*b*c)))
        adj_point_angle_list.append(angle_A)
print(adj_point_angle_list)