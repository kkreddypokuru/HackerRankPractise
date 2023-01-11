def pageCount(n, p):
    book = []
    cnt = 1
    lp = 0
    while cnt <= n:
        if cnt == 1:
            book.append((None, cnt))
            cnt = cnt + 1

        elif cnt == n:
            book.append((cnt, None))
            cnt = cnt + 1
        else:
            book.append((cnt, cnt + 1))
            cnt = cnt + 2
        lp = lp + 1

    if n - p < n / 2:
        start = len(book)-1
        page_count = 0
        while 0 <= start < len(book):
            if p in book[start]:
                return page_count
            start = start - 1
            page_count = page_count + 1
    else:
        start = 0
        page_count = 0
        while 0 <= start < len(book):
            if p in book[start]:
                return page_count
            start = start + 1
            page_count = page_count + 1


n = 6
p = 2
res = pageCount(n, p)
print(res)
