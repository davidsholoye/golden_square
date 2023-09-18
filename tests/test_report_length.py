from lib.report_length import *

def test_length_is_ten():
    result = report_length('qwertyuiop')
    result == "This string is 10 characters long."

def test_length_is_one():
    result = report_length('q')
    result == "This string is 1 characters long."

def test_length_is_twenty_three():
    result = report_length('qwertyuiopasdfghjklmnbv')
    result == "This string is 23 characters long."

def test_length_is_five():
    result = report_length('qwert')
    result == "This string is 5 characters long."

def test_length_is_zero():
    result = report_length('')
    result == "This string is 0 characters long."

