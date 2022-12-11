def grid_search(gr, sr):
    low = 0
    high = len(sr)
    prev = 0
    count = 0
    found = "NO"
    ln = len(gr)
    print(ln)
    for i in range(0, ln):
        src = sr[low]
        grd = gr[i]
        if src in grd:
            if prev == 0:
                count = count + 1
                if low < high:
                    low = low + 1
                    prev = i + 1
            elif prev == i:
                count = count + 1
                if low < high:
                    low = low + 1
                    if count == len(sr):
                        found = "YES"
                        return found
                    prev = i + 1
    return found


grid = [
    '400453592126560',
    '114213133098692',
    '474386082879648',
    '522356951189169',
    '887109450487496',
    '252802633388782',
    '502771484966748',
    '075975207693780',
    '511799789562806',
    '404007454272504',
    '549043809916080',
    '962410809534811',
    '445893523733475',
    '768705303214174',
    '650629270887160', ]

search = [
    '99',
    '99',
]

grid = ['7283455864',
        '6731158619',
        '8988242643',
        '3830589324',
        '2229505813',
        '5633845374',
        '6473530293',
        '7053106601',
        '0834282956',
        '4607924137',
        ]
search = [
    '9505',
    '3845',
    '3530',
]

if __name__ == "__main__":
    res = grid_search(grid, search)
    print(res)
