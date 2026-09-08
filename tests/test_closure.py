from utils.practis_20260907 import make_adder

def test_positive():
    add3=make_adder(4)
    assert add3(3)==7

def test_negative():
    add_neg=make_adder(-4)
    assert  add_neg(3)==-1

def test_zero():
    add0=make_adder(0)
    assert add0(3)==4
