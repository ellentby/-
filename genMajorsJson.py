import openpyxl, json

def readExcel(filepath):
    wb = openpyxl.load_workbook(filepath)
    ws = wb.active  # 当前活跃的表单
    result = []
    count = 0
    for row in ws.rows:
        row_content = []
        for cell in row:
            row_content.append(cell.value)
        result.append(row_content)
        count += 1
        if count % 1000 == 0:
            print("读取excel：已处理{}/{}行".format(count, ws.max_row+1))
    return result

result = readExcel("./majors.xlsx")
result_dict = []
for line in result[1:]:
    ele_dict = {"major": line[1], "code": line[3], "department": line[0]}
    result_dict.append(ele_dict)

with open("./majors.json","w+") as f:
    json.dump(result_dict, f, ensure_ascii=False)
    print("专业列表已写入majors.json")

