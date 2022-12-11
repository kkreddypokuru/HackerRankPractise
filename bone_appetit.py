# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


def get_bon_appetit(bill, k, b):
    bc = 0
    for index, val in enumerate(bill):
        if index == k:
            continue
        bc = bc + val
    if bc / 2 == b:
        return "Bon Appetit"
    else:
        return int(b - (bc / 2))


bill = [3, 10, 2, 9]
k = 1
b = 12
res = get_bon_appetit(bill, k, b)
print(res)
