import time
from functools import reduce
from main import mins, maxs, sums, mul
import unittest

class SolutionTestCase(unittest.TestCase):
    def test_max():  #тест на максимум
        data = []
        with open("data.txt", 'r') as file_obj:
            data = list(map(int, file_obj.read().split()))
        assert maxs(data) == max(data)


    def test_min():  #тест на минимум
        data = []
        with open("data.txt", 'r') as file_obj:
            data = list(map(int, file_obj.read().split()))
        assert mins(data) == min(data)


    def test_sum():  #тест на сумму
        data = []
        with open("data.txt", 'r') as file_obj:
            data = list(map(int, file_obj.read().split()))
        assert sums(data) == sum(data)


    def proz(numbers):
        try:
            proizden = reduce(lambda x,y: x*y,numbers)
        except OverflowError:
            proizden = "error"
        return proizden


    def test_proiz():  #тест на произведение
        data = []
        with open("data.txt", 'r') as file_obj:
            data = list(map(int, file_obj.read().split()))
        assert mul(data) == proz(data)


    def test_proiz_bolse_sum():  #любой другой тест
        data = []
        with open("data.txt", 'r') as file_obj:
            data = list(map(int, file_obj.read().split()))
        assert mul(data) > sums(data)


    def test_time():  #тест на время
        data = []
        with open("data.txt", 'r') as file_obj:
            data = list(map(int, file_obj.read().split()))
        data1 = data
        for i in range(100):
            data1.append(10**1000)
        time_start = time.time()
        max = maxs(data)
        min = mins(data)
        proiz = mul(data)
        summa = sums(data)
        time_end = time.time()
        time_normal = time_end-time_start
        print("время работы:", time_normal)
        time_start1 = time.time()
        max1 = maxs(data1)
        min1 = mins(data1)
        proiz1 = mul(data1)
        summa1 = sums(data1)
        time_end1 = time.time()
        time_big = time_end1-time_start1
        print("время работы при увеличении файла:", time_big)
