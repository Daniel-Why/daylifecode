# 读取excel中的列表，在对应文件夹生成对应文件。
import xlwt
import xlrd
from xlutils.copy import copy
import os
import shutil

def readexcel(excel_path):
    workbook = xlrd.open_workbook(r'%s'%(excel_path))
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet1 = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第1个表格
    worksheet2 = workbook.sheet_by_name(sheets[1])  # 获取工作簿中所有表格中的的第2个表格
    return worksheet1,worksheet2
def mkdir_and_file(worksheet1,worksheet2):
    rowN1 = worksheet1.nrows
    rowN2 = worksheet2.nrows
    print('rowN1:',rowN1)
    for i in range (rowN1):
        dirname = worksheet1.cell_value(i,1)
        dirid = worksheet1.cell_value(i,0)
        pic = '{}\\pic'.format(dirname)
        os.mkdir(dirname)
        os.mkdir(pic)
        for i in range (rowN2):
            fileSuffix = '.md'    #文件后缀
            filename = worksheet2.cell_value(i,1)
            fileid = worksheet2.cell_value(i,0)
            if fileid == dirid:
                if "Windows" in filename:
                    org_file = 'windows.md'
                    fname = filename + fileSuffix
                    md_path = '{}\\{}'.format(dirname,fname)
                    shutil.copyfile(org_file,md_path)
                elif "Linux" in filename:
                    org_file = 'Linux.md'
                    fname = filename + fileSuffix
                    md_path = '{}\\{}'.format(dirname,fname)
                    shutil.copyfile(org_file,md_path)
                else:
                    org_file = 'other.md'
                    fname = filename + fileSuffix
                    md_path = '{}\\{}'.format(dirname,fname)
                    shutil.copyfile(org_file,md_path)
def main():
    excel_path = "test.xlsx"
    worksheet1,worksheet2 = readexcel(excel_path)
    mkdir_and_file(worksheet1,worksheet2)

main()