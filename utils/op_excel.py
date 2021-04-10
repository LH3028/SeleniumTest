import xlrd
from xlutils.copy import copy

class OpExcel(object):
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            excel_path = "D://Python/HtmlTestRunner/Htmltestrunner/config/case.xls"

        else:
            self.excel_path = excel_path
        if index == None:
            index = 0

        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]
        self.rows = self.table.nrows
    @property
    def get_data(self):
        #获取excel数据
        result = []
        rows = self.get_line()
        if rows == None:
            return None
        for i in range(rows):
            col = self.table.row_values(i)
            result.append(col)
        return result


    def get_line(self):
        #获取行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    def get_col_value(self, row, col):
        #获取单元格数据
        if self.get_line() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    def write_result(self, row, value):
        #写入结果
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


if __name__ == "__main__":
    op = OpExcel("D://Python/HtmlTestRunner/Htmltestrunner/config/keys.xls")
    result = op.get_data
    print(result)
    print(op.get_col_value(1,2))
    op.write_result(3, "test")
