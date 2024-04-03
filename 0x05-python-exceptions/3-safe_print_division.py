#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        Result_Div = a / b
    except ZeroDivisionError:
        Result_Div = None
    finally:
        print("Inside result: {}".format(Result_Div))
    return Result_Div
