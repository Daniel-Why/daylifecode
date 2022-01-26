import os,csv,random

def str_to_int(trace_data):#将 str 转换为 int
    new_trace_data=[]
    for coord_list_str in trace_data:
        new_coord_list = []
        coord_list=coord_list_str.split(",")
        for i in coord_list:
            new_coord_list.append(int(i))
        new_trace_data.append(new_coord_list)
    return new_trace_data

def cut_trace(x,trace_data):
    new_trace = []
    current = 0
    n = 0
    for trace in trace_data:
        current = current + trace[0]
        n+=1
        if current >= x:
            break
    #print(current)
    if current == x:
        new_trace.extend(trace_data[:n])
        return new_trace
    elif abs(x-current) > abs(x-(current-trace_data[n-1][0])):
        new_trace.extend(trace_data[:n-1])
        delt_x = x-(current-trace_data[n-1][0])
        new_trace.append([delt_x,0])
    elif abs(x-current) < abs(x-(current-trace_data[n-1][0])):
        new_trace.extend(trace_data[:n])
        delt_x = x-current
        new_trace.append([delt_x,0])
    
    x_result = 0
    for trace in new_trace:
        x_result = x_result+trace[0]
    #print(x_result)
    return new_trace

    



def get_trace(x):
    os.chdir(r"D:\Personal\daylifecode\captcha_example\Selenium_slide_captcha_cross")
    trace_datas = csv.reader(open(r".\mouse_record\clean_data\trace_record.csv"))
    trace_list = []
    for i,data_row in enumerate(trace_datas):
        if i !=0:
            trace_list.append(data_row)
    num = random.randrange(0,len(trace_list))
    trace_data = trace_list[num]
    new_trace_data = str_to_int(trace_data)
   # print(new_trace_data)
    trace = cut_trace(x,new_trace_data)
    return trace

if __name__=='__main__':
    get_trace(66)
