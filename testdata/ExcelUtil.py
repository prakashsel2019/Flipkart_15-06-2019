import xlrd
import os

def select_cell_val(file_name, sheet_name, input_val):
    path = os.getcwd()
    wb = xlrd.open_workbook(path + "\\testdata\\" + file_name)
    ws = wb.sheet_by_name(sheet_name)
    row_val = ws.nrows
    col_val = ws.ncols
    for i in range(row_val):
        for j in range(col_val):
            if input_val == ws.cell_value(i, j):
                return ws.cell_value(i + 1, j)
        break

# val = select_cell_val("C:\\Users\\Harish\\Desktop\\book1.xlsx", "setup", "Un")
# print(val)

