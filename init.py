# Этот модуль отвечает за считывание данных от пользователя
from ast import Div, Mult, Sub
import math 

import project_sum
import project_sub
import project_div
import project_mult

x = 0
y = 0
operation = '+'


def initialization(a, b, user_operation):
    global x
    global y
    global operation
    x = a
    y = b
    operation = user_operation

def user_operation():
    global x
    global y
    global operation
    if operation == '+':
        return project_sum.summ(x, y)
    if operation == '-':
        return project_sub.subtract(x, y)
    if operation == '*':
        return project_mult.multply(x, y)
    else:
        return project_div.divide(x, y)
    
    