from openpyxl import load_workbook

wb = load_workbook("14-3Dodgers.xlsx")

result = []

ws = wb.worksheets[0]
for row in ws.iter_rows():
    #List comprehension
    result.append([cell.value for cell in row])
    
print(result)
    