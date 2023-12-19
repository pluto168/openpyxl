from openpyxl import Workbook 
import csv

data_rows = [fields for fields in csv.reader(open("14-1file.csv", newline = ""))]

# print(data_rows)
wb = Workbook()
ws = wb.active
ws.title = "MyFile"
ws.sheet_properties.tabColor = "1072BA" #設定顏色
for row in data_rows:
    ws.append(row)
    
wb.save("Myfile.xlsx")