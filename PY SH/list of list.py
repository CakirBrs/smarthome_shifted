import xlrd 

# Give the location of the file 
loc = ("list.xlsx") 

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
a= sheet.cell_value(0, 0)
print(a)
print(sheet.nrows) 
print(sheet.ncols) 
print(type(sheet.row_values(1)))
liste=[]
liste.append(sheet.row_values(1))
print("asdasd")
print("asdasdasd2")
a=10
a=-a
print(a)
b=20
print(b+a)

print(sheet.cell_value(0, 0))
print(sheet.cell_value(1, 1))
print(sheet.cell_value(1, 0))
print(sheet.cell_value(0, 1))