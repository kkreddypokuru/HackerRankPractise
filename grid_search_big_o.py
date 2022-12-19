# https://medium.com/analytics-vidhya/how-to-find-the-time-complexity-of-a-python-code-95b0237e0f2d
import logging
import random as rnd
from big_o import big_o

logging.getLogger().setLevel(logging.DEBUG)

import logging

logging.getLogger().setLevel(logging.DEBUG)


def grid_search(arg):
    G = arg[0]
    P = arg[1]
    search = P[0][0]
    pattern_found = "NO"
    for i, grid_val in enumerate(G):
        j = str(grid_val).find(str(search))
        while j >= 0 and i + len(P) <= len(G) and j + len(P) <= len(grid_val):
            counter = 0
            li = i
            for pattern in P:
                if G[li][j:j + len(pattern)] == pattern:
                    counter += 1
                    li = li + 1
                    continue
                break
            if counter == len(P):
                pattern_found = "YES"
                return pattern_found
            check = str(grid_val[j + 1:len(grid_val)]).find(str(search))
            if check < 0:
                break
            j = j + check + 1
    return pattern_found


def get_inputs(n):
    from inputs import data
    grd_inputs = data.grid_search_test_data
    i = rnd.randrange(0,len(grd_inputs))
    return grd_inputs[i][0] * n, grd_inputs[i][1] * n


if __name__ == "__main__":
    best, others = big_o(grid_search, get_inputs, n_measures=100)
    print(best)
