#! /usr/bin/env python2.7

''' Print a multiplication table for a sequence of numbers '''

import sys
from argparse import ArgumentParser

from sequence import primes, fib
import times_table


SEQS = {'primes': primes,
        'fib': fib}


def parse_args(args=sys.argv[1:]):
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--count', help='the number of prime numbers in the table',
                        type=int, default=10)
    parser.add_argument('--seq', help='the type of number sequence',
                        choices=SEQS.keys(), default='primes')
    return parser.parse_args(args)


def lines(gen, n):
    nums = list(gen(n))
    table = times_table.table(nums)
    return times_table.table_lines(nums, table)


def main():
    args = parse_args()

    for line in lines(SEQS[args.seq].gen, args.count):
        print line


if __name__ == '__main__':
    main()