from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # insert the line at the 8th row
# ws.insert_rows(8, 5) # insert 5 lines from the 8th row
# wb.save("sample_insert_rows.xlsx")

# ws.insert_cols(2) # B column
ws.insert_cols(2, 3) # insert 3 colums from B column
wb.save("sample_insert_cols.xlsx")

