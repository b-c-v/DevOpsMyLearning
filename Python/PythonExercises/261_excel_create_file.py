import xlsxwriter

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook("tmp.xlsx")
worksheet = workbook.add_worksheet()

workbook.close()
