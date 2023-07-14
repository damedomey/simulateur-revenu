from openpyxl import load_workbook
from pycel import ExcelCompiler
from utils.model import Address
import win32com.client as win32


def read_cell(file_path, address: Address):
    excel_app = win32.Dispatch("Excel.Application")
    workbook = excel_app.Workbooks.Open(file_path)
    sheet = workbook.ActiveSheet
    value = sheet.Range(address.cell)
    #workbook.close()
    #excel_app.Quit()
    return value

def write_cell(file_path, address: Address, value):
    wb = load_workbook(filename=file_path)
    sheet = wb[address.sheet]
    sheet[address.cell].value = value
    wb.save(file_path)
    wb.close()
