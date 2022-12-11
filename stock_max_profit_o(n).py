import logging

logging.getLogger().setLevel(logging.DEBUG)


def get_max_profit(data):
    logging.info("stock data:%s", data)
    maximum_profit: int = 0
    if data:
        n = len(data)
        if n == 1:
            return maximum_profit
        l, r = 0, 1
        while r < n:
            if data[l] < data[r]:
                tmp = data[r] - data[l]
                maximum_profit = max(maximum_profit, tmp)
            else:
                l = r
            r = r + 1
        return maximum_profit
    else:
        raise Exception("not valid stock data:{data}".format(data=data))


stock_data = [7, 1, 4, 3, 4, 4, 10, 9]
# stock_data = [100, 180, 260, 310, 40, 535, 695]
profit = get_max_profit(stock_data)
logging.info("max_profit:%s", profit)
