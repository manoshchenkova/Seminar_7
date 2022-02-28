# Координирует между собой модули

import re
from view import request_data, request_data_x
import view

import init

result = 0

def button_click():
    global result
    value_a = view.request_data_x()
    value_b = view.request_data_y()
    operation = view.request_data_op()
    init.initialization(value_a, value_b, operation)
    result = init.user_operation()
    view.view_data(f' Результатом операции будет {result}')