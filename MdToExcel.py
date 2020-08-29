import xlwt
import xlrd
from xlutils.copy import copy
import os
def scan_md_list(file_dir): #读取目标文件夹内所有 .md 文件
    aa=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.md':
                aa.append(os.path.join(file))
    return aa
def read_md_list(md_list_path): #读取txt中每一行
    aa = []
    with open(md_list_path, "r", encoding='UTF-8') as f:
        for line in f.readlines():
            aa.append(line)
    return aa
def read_md(md_path):#读取 .md 转换为 str
    fo = open( md_path , "r",encoding='UTF-8')
    md_orgin_name = os.path.basename(md_path)
    md_name = md_orgin_name[6:]
    md_id = md_orgin_name[:6]
    md_category_id = md_orgin_name[:3]
    print ("--------")
    print ("resource：", md_id)
    print ("category id：", md_category_id)
    print ("title ", md_name)
    aa = fo.readlines()
    md_text = ''.join(aa)
    # 关闭文件
    fo.close()
    return md_text,md_name,md_id,md_category_id
def create_excel():#新建excel
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('auto_attack_attack_tips')
    worksheet.write(0,3,'content')
    worksheet.write(0,2,'title')
    worksheet.write(0,1,'category_id')
    worksheet.write(0,0,'resource_id')
    workbook.save('auto_attack_attack_tips.xls')
def write_excel(excel_path,row,column,md_text,md_name,md_id,md_category_id):#插入excel
    workbook = xlrd.open_workbook(r'%s'%(excel_path))
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    #写入 md 数据
    new_worksheet.write(row,column,md_text)
    new_worksheet.write(row,column-1,md_name)
    new_worksheet.write(row,column-2,md_category_id)
    new_worksheet.write(row,column-3,md_id)
    # 保存
    new_workbook.save(r'%s'%(excel_path))
    print('写入完成!')

def main():#扫描文件夹中所有 md 文件，写入excel
    #read_md_path = 'md_list.txt'
    #aa = read_md_list(read_md_path)
    dir = '.\\md_content'
    aa = scan_md_list(dir)
    l = len(aa)
    if os.path.exists('auto_attack_attack_tips.xls') == False:
        print('新建文件成功')
        create_excel()
    for i in range(0, l):
        fname = aa[i].splitlines(False)
        str_fname = ''.join(fname)
        md_path = '{}\\{}'.format(dir,str_fname)
        md_text,md_name,md_id,md_category_id = read_md(md_path)
        excel_path = 'auto_attack_attack_tips.xls'
        write_excel(excel_path,1+i,3,md_text,md_name,md_id,md_category_id)
main()

