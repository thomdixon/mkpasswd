#!/usr/bin/env python

from __future__ import print_function

import argparse
from random import choice, shuffle
from string import *

LEGNTH = 10
MIN_LOWERCASE = 2
MIN_UPPERCASE = 2
MIN_DIGITS = 2
MIN_SPECIAL = 1


def mkpasswd(length=LEGNTH,
             min_lower=MIN_LOWERCASE,
             min_upper=MIN_UPPERCASE,
             min_digits=MIN_DIGITS,
             min_special=MIN_SPECIAL):
    lower = [choice(ascii_lowercase) for i in range(min_lower)]
    upper = [choice(ascii_uppercase) for i in range(min_upper)]
    nums = [choice(digits) for i in range(min_digits)]
    special = [choice(punctuation) for i in range(min_special)]

    minimum = min_lower + min_upper + min_digits + min_special
    remaining = (length - minimum) if length > minimum else 0
    rest = [choice(ascii_letters) for i in range(remaining)]

    result = upper + lower + nums + special + rest
    shuffle(result)

    return ''.join(result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l',
                        '--length',
                        help='password length',
                        type=int,
                        default=LEGNTH)
    parser.add_argument('-c',
                        '--lower',
                        help='minimum number of lowercase characters',
                        type=int,
                        default=MIN_LOWERCASE)
    parser.add_argument('-C',
                        '--upper',
                        help='minimum number of UPPERCASE characters',
                        type=int,
                        default=MIN_UPPERCASE)
    parser.add_argument('-d',
                        '--digits',
                        help='minimum number of digits',
                        type=int,
                        default=MIN_DIGITS)
    parser.add_argument('-s',
                        '--special',
                        help='minimum number of special characters',
                        type=int,
                        default=MIN_SPECIAL)
    args = parser.parse_args()

    print(mkpasswd(args.length, args.lower,
          args.upper, args.digits, args.special))
