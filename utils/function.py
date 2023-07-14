from utils.model import Address


def read_cell(workbook, address: Address):
    """
        Read a cell in the Excel file

        :param workbook The Excel workbook that contain the file
        :param address The address of cell that will be read
    """

    sheet = workbook.Sheets(address.sheet)
    value = sheet.Range(address.cell)

    return value


def write_cell(workbook, address: Address, value):
    """
        Read a cell in the Excel file

        :param workbook The Excel workbook that contain the file
        :param address The address of cell that will be changed
        :param value The value to write

        Notice that this function doesn't save the change in the file
    """
    sheet = workbook.Sheets(address.sheet)
    sheet.Range(address.cell).Value = value
