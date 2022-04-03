# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).
#
# Note: If the number is a multiple of both 3 and 5, only count it once.
import math


def solution(number):

    multiples_3 = []
    multiples_5 = []
    all_multiples = []
    all_mult_no_dupes = []

    if number < 0:
        return 0
    else:
        # find multiples of 3 or 5 by looking at each value between 1 and 10 where modulus (left overs) = 0
        multiples_3 = [n for n in range(1, number) if n % 3 == 0]
        multiples_5 = [n for n in range(1, number) if n % 5 == 0]
        print('multiples of 3 are', multiples_3)
        print('multiples of 5 are', multiples_5)
        # add list together
        # sort list in number order
        all_multiples = sorted(multiples_3 + multiples_5)
        print('all multiples are', all_multiples)
        # remove duplicates
        all_mult_no_dupes = list(dict.fromkeys(all_multiples))
        print('all mulitples no duplicates are', all_mult_no_dupes)
        # Add all values in list together
        return sum(all_mult_no_dupes)


number = 10
print(solution(number))

number = 50
print(solution(number))