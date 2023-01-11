def sockMerchant(n, ar):
    # Write your code here
    pair = []
    i_skip_index = []
    for i, i_val in enumerate(ar):
        if i in i_skip_index:
            continue
        i_skip_index.append(i)
        for j, j_val in enumerate(ar):
            if j in i_skip_index:
                continue
            if i_val == j_val:
                pair.append(i_val)
                i_skip_index.append(j)
                break

    return len(pair)


arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = len(arr)
res = sockMerchant(n,arr)
print(res)
