from calculator import calculator
calc = calculator()

def test_sum_positive_nums():
    calc = calculator
    res = calc.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    res = calc.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    res = calc.sum(-6, 6)
    assert res == 0

def test_sum_float_nums():
    calc = Calculator()
    res = calc.sum(10, 0)
    assert == 10

# res = calc.sum(-6, 6)
# assert res == 0
#
# #round result?
# res = calc.sum(5.6, 4.3)
# print(res)
# res = round(res, 1)
# print(res)
# assert res == 9.9
#
# res = calc.sum(10, 0)
# assert res == 10
#
# res = calc.div(10, 2)
# assert res == 5
#
# numbers = []
# res = calc.avg(numbers)
# assert res == 0
#
# numbers = [1,2,3,4,5,6,7,8,9,5]
# res = calc.avg(numbers)
# print(res)
# assert round(res, 1) == 10
#

# print('finih')
#
# res = calc.div(10, 0)
# assert  res == None
