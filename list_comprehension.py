# import re
#
# # with open("D:/IdeaProjects/HackerRankPractise/text_data/sample.txt", "r") as f:
# #     s = {w.lower() for ln in f for w in re.split(r"\W+", ln) if w}
# # print(s)
#
# import this
import timeit
code1='''
sum_val = sum([x*x for x in range(10)])
'''
print(timeit.Timer(code1).timeit())

code2='''
sum_val = sum(x*x for x in range(10))
'''

print(timeit.Timer(code2).timeit())