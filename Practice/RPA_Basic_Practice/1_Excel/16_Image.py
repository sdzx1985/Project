from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("Untitled.png")

# Insert the img to C3
ws.add_image(img, "C3")

wb.save("sample_img.xlsx")