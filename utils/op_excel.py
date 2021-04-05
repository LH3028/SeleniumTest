import xlrd


class OpExcel(object):
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            excel_path = "D://Python/HtmlTestRunner/Htmltestrunner/config/case.xls"

        if index == None:
            index = 0

        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        self.rows = self.table.nrows

    @property
    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)
            result.append(col)
        return result

if __name__ == "__main__":

        result= OpExcel().get_data
        print(result)