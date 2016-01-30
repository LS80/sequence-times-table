''' Unit tests for the number sequence multiplication tables '''

import unittest

from sequence import primes
import times_table
import print_times_table


class TestPrimes(unittest.TestCase):
    def test_one_is_not_prime(self):
        self.assertFalse(primes._is_prime(1))

    def test_two_is_prime(self):
        self.assertTrue(primes._is_prime(2))

    def test_four_is_not_prime(self):
        self.assertFalse(primes._is_prime(4))

    def test_number_of_primes_is_correct(self):
        self.assertEquals(len(list(primes.gen(10))), 10)

    def test_value_of_tenth_prime(self):
        self.assertEquals(list(primes.gen(10))[-1], 29)

    def test_zero_number_of_primes_is_error(self):
        with self.assertRaises(AssertionError):
            next(primes.gen(0))

    def test_invalid_number_of_primes_is_error(self):
        with self.assertRaises(ValueError):
            next(primes.gen('a'))


class TestTimesTable(unittest.TestCase):
    def setUp(self):
        self.nums = range(1, 11)
        
    def test_two_times_table(self):
        self.assertEquals(times_table.table(self.nums[:2]), [[1, 2], [2, 4]])
        
    def test_two_times_table_format(self):
        table = [[1, 2], [2, 4]]
        self.assertEquals(list(times_table.table_lines(self.nums[:2], table)),
                          ['  |1 2',
                           '--+---',
                           '1 |1 2',
                           '2 |2 4'])

    def test_four_times_table_format(self):
        table = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
        self.assertEquals(list(times_table.table_lines(self.nums[:4], table)),
                          ['  | 1  2  3  4',
                           '--+-----------',
                           '1 | 1  2  3  4',
                           '2 | 2  4  6  8',
                           '3 | 3  6  9 12',
                           '4 | 4  8 12 16'])       


class TestPrimesTimesTable(unittest.TestCase):
    def test_parse_count_five(self):
        args = print_times_table.parse_args(['--count', '5'])
        self.assertEquals(args.count, 5)

    def test_default_args(self):
        args = print_times_table.parse_args([])
        self.assertEquals(args.count, 10)

    def test_ten_primes_table(self):
        lines = list(print_times_table.lines(primes.gen, 10))
        self.assertEquals(lines, 
                          ['   |  2   3   5   7  11  13  17  19  23  29',
                           '---+---------------------------------------',
                           ' 2 |  4   6  10  14  22  26  34  38  46  58',
                           ' 3 |  6   9  15  21  33  39  51  57  69  87',
                           ' 5 | 10  15  25  35  55  65  85  95 115 145',
                           ' 7 | 14  21  35  49  77  91 119 133 161 203',
                           '11 | 22  33  55  77 121 143 187 209 253 319',
                           '13 | 26  39  65  91 143 169 221 247 299 377',
                           '17 | 34  51  85 119 187 221 289 323 391 493',
                           '19 | 38  57  95 133 209 247 323 361 437 551',
                           '23 | 46  69 115 161 253 299 391 437 529 667',
                           '29 | 58  87 145 203 319 377 493 551 667 841'])


if __name__ == "__main__":
    unittest.main()