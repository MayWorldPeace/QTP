# 导入模块
import xlrd
# 读取到excel文件
data = xlrd.open_workbook("student.xlsx")
# 获取列表
table = data.sheet_by_index(0)
# 获取所有的行数
nrows = table.nrows
# # 获取所有的列数
# ncols = table.ncols

# 获取第一行的数据
first_row_name_list = table.row_values(0)
print(first_row_name_list)

# 定义一个列表保存所有行的数据
info_list = []
# 遍历所有行
for rownum in range(1, nrows):
    # 获取
    row = table.row_values(rownum)
    # 如果row有数据
    if row:
        info_list.append(row)

print(info_list)