import xlwt
import xlrd
from xlutils.copy import copy
import os
import common_use_function as cf

os.chdir('D://YZYImage_full//md//operating_systems')
workbook = xlrd.open_workbook(r'%s'%("new_excel.xls"))
sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
rows = worksheet.nrows
cols = worksheet.ncols
print(rows,cols)