import xlrd

def get_testdata(file_name, sheet_name, linestart, lineend, columnstart, columnend):
    # 打开 excel 文件
    excel = xlrd.open_workbook(file_name)
    # 指定 sheet 名称
    sheet = excel.sheet_by_name(sheet_name)
    data_list = []
    # 读取行，不包括 end 行在内
    for i in range(linestart, lineend):
        # 读取第 i 行的列，不包括 end 列在内
        j = sheet.row_values(i, columnstart, columnend)
        # 将读取的数据添加到列表中
        data_list.append(j)
    # 返回列表
    return data_list
