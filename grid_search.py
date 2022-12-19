# https://www.hackerrank.com/challenges/the-grid-search/problem
from inputs import data
import logging

logging.getLogger().setLevel(logging.DEBUG)

def grid_search(G, P):
    search = P[0][0]
    found = "NO"
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
                found = "YES"
                return found
            check = str(grid_val[j + 1:len(grid_val)]).find(str(search))
            if check < 0:
                break
            j = j + check + 1
    return found


if __name__ == "__main__":
    for _ in data.grid_search_test_data:
        # G = ['123412',
        #      '561212',
        #      '123634',
        #      '781288']
        # P = ['12',
        #      '34']
        G=_[0]
        P=_[1]
        found = grid_search(G, P )
        logging.info("found:%s" % found)
