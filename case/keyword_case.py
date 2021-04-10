# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.4.6"

from utils.op_excel import OpExcel
from keywords.action_method import ActionMethod


class KeyWordCase(object):
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = OpExcel("D://Python/HtmlTestRunner/Htmltestrunner/config/keys.xls")
        # 获取总行数
        case_line = handle_excel.get_line()
        print(case_line)
        # 遍历总行数，执行每行的case
        if case_line:
            for i in range(1, case_line):
                is_run = handle_excel.get_col_value(i, 2)
                print(is_run)
                # 判断是否执行
                if is_run == "yes":
                    # 获取执行的方法
                    method = handle_excel.get_col_value(i, 4)
                    # 获取输入的数据
                    input_data = handle_excel.get_col_value(i, 5)
                    # 获取操作元素
                    op_element = handle_excel.get_col_value(i, 6)
                    # 获取预期结果方法
                    except_result_method = handle_excel.get_col_value(i, 7)
                    # 获取预期结果值
                    except_result = handle_excel.get_col_value(i,8)
                    self.run_method(method, input_data, op_element)
                    if except_result != "":
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == "text":
                            result = self.run_method(except_result_method)
                            if except_result[1] in result:
                                handle_excel.write_result(i, "pass")
                            else:
                                handle_excel.write_result(i, "fail")
                        elif except_value[0] == "element":
                            result = self.run_method(except_result_method, op_element=except_value[1])
                            if result:
                                handle_excel.write_result(i, "pass")
                            else:
                                handle_excel.write_result(i, "fail")

                    else:
                        print("预期结果为空")

    def get_except_result_value(self, data):
        return data.split("=")

    def run_method(self, method, input_data= "", op_element= ""):
        method_value = getattr(self.action_method, method)
        # 判断输入数据是否存在
        if input_data == "" and op_element != '':
            result = method_value(op_element)
        elif input_data == '' and op_element == '':
            result = method_value()
        elif input_data != '' and op_element == '':
            result = method_value(input_data)
        else:
            result = method_value(op_element, input_data)
        return result

if __name__ == "__main__":
    KeyWordCase().run_main()
