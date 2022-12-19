from inputs import data
import logging

logging.getLogger().setLevel(logging.DEBUG)


class GridSearch:
    def __init__(self, G, P):
        self.G = G
        self.P = P
        self.grid_rows = len(self.G)
        self.pattern_rows = len(self.P)
        self.pattern_ln = len(self.P[0])
        self.found = "NO"

    def all_associations(self, grid, pattern):
        lst = []
        tmp = grid
        f = tmp.find(pattern)
        while f>=0:
            lst.append(f)
            i = tmp[f+self.pattern_ln:len(grid)].find(pattern)
            if i>=0:
                f = i + f + self.pattern_ln
            else:
                break
        return lst

    def grid_search(self):
        k = 0
        pattern = self.P[k]
        for g_index, grid in enumerate(self.G):
            _all_associations = self.all_associations(grid, pattern)
            if _all_associations:
                for loc in _all_associations:
                    fnd = self.find_all_patterns(grid, g_index + 1, loc)
                    if fnd == "YES":
                        return fnd
        return self.found

    def find_all_patterns(self, grid, g_index, p_g_index):
        fnd="NO"
        for i in range(1, self.pattern_rows):
            pattern = self.P[i]
            if self.G[g_index][p_g_index:p_g_index + self.pattern_ln] == pattern:
                g_index = g_index+1
                fnd="YES"
                continue
            else:
                fnd= "NO"
        return fnd


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
        found = GridSearch(G, P).grid_search()
        logging.info("found:%s" % found)
