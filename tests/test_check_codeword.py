from lib.check_codeword import *

def test_horse():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

def test_HORSE():
    result = check_codeword('HORSE')
    assert result == 'WRONG!'

def test_hORSe():
    result = check_codeword('hORSe')
    assert result == 'Close, but nope.'