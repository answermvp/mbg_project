import xlwt

def write_excel(sheet_name, excel_name):
    # 创建 excel
    wbk = xlwt.Workbook()
    # 创建 sheet 页
    sheet = wbk.add_sheet(sheet_name)
    # 写入内容：行，列，数据
    sheet.write(0,1,'test text')
    # 保存，默认保存到桌面
    wbk.save(excel_name)
