#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=[]):
    ways = [0] * (n + 1)
    start = [1, 1, 2]
    for i in range(len(ways)):
        if i <= 2:
            ways[i] = start[i]
        else:
            ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
    return ways[n]


# 1, 1, 2, 4, 7, 13, 24
# 4:
#     1: 1+1+1 + 1
#     2. 1+2 + 1
#     3. 2+1 + 1
#     4. 3+1
#     5. 2+2
#     6. 1+3
#     7. 1+1+2

# 5:
#     1. 1 * 5
#     2. 1+2
#     7. 1+1 + 2+1
#     1: 1+1 + 1+1+1
#     10. 1+1 + 1+2
#     11. 1+1 + 3
#     2. 1+2 + 1 + 1
#     3. 2+1 + 1 + 1
#     4. 3 + 1 + 1
#     5. 2 + 2 + 1
#     6. 1+3 + 1
#     8. 3 + 2
#     9. 2 + 3
#     12.
#     13.

#     3 + 1+1
#     3 + 2
#     2 + 1+2


# 6:
#     1: 1+1+1 + 1+1+1

#     10. 1+1 + 1+2 + 1
#     11. 1+1 + 3 + 1
#     2. 1+2 + 1 + 1
#     3. 2+1 + 1 + 1
#     4. 3 + 1 + 1 + 1
#     5. 2 + 2 + 1
#     6. 1+3 + 1+1
#     7. 1+1 + 2 + 1+1
#     8. 3 + 2 + 1
#     9. 2 + 3 + 1
#     12. 3+3
#     13. 3 + 1 + 2


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
