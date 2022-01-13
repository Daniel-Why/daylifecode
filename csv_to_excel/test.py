import csv
import os

os.chdir(r'D:\Personal\daylifecode\csv_to_excel\ua_ip')
with open('test.csv',"w") as f:
    input_list=[["app","10.10.10.3"]]
    f_csv=csv.writer(f)
    f_csv.writerows(input_list)


