from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(8) # 8th line 7th data
# ws.delete_rows(8, 3) # delete 3 rows from 8th line 7th data

# wb.save("sample_delete_row.xlsx")

# ws.delete_cols(2) # delete 2th columns
ws.delete_cols(2, 2) # delete 2 columns from 2th columns

wb.save("sample_delete_cols.xlsx")