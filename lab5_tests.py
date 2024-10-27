import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.
    # Part 2
    #    Part 2 tests should be in data_tests.py.
    # Part 3
    def test_time_add_1(self):
        input1, input2 = data.Time(12, 24, 36), data.Time(2,36,24)
        result = lab5.time_add(input1, input2)
        expected = data.Time(hour = 15, minute = 1, second = 0)
        self.assertEqual(expected, result)
    def test_time_add_1(self):
        input1, input2 = data.Time(2, 30, 30), data.Time(2, 30, 40)
        result = lab5.time_add(input1, input2)
        expected = data.Time(hour = 5, minute = 1, second = 10)
        self.assertEqual(expected, result)
    # Part 4
    def test_is_descending_1(self):
        input = [0.4,2.0,0.3,1]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected, result)
    def test_is_descending_2(self):
        input = [4.0, 3.0, 2.0, 1.0]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected, result)
    # Part 5
    def test_largest_between_1(self):
        input1, input2, input3 = [4, 2, 1, 3], 3, 1
        result = lab5.largest_between(input1, input2, input3)
        expected = None
        self.assertEqual(expected, result)
    def test_largest_between_2(self):
        input1, input2, input3 = [4, 999, 0, 75, 9999, 99999, 1], 0, 6
        result = lab5.largest_between(input1, input2, input3)
        expected = 5
        self.assertEqual(expected, result)
    # Part 6
    def test_furthest_from_origin_1(self):
        input = [data.Point(4, 40), data.Point(8, 25), data.Point(5, 30)]
        result = lab5.furthest_from_origin(input)
        expected = data.Point(4, 40)
        self.assertEqual(expected, result)
    def test_furthest_from_origin_2(self):
        input = [data.Point(7, 20), data.Point(8, 10), data.Point(6, 30)]
        result = lab5.furthest_from_origin(input)
        expected = data.Point(6, 30)
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
