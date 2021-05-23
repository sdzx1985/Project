from openpyxl import Workbook
wb = Workbook() # new work book create
ws = wb.active # call activated sheet
ws.title = "Python" # change the name of the sheet
wb.save("sample.xlsx")
wb.close()
