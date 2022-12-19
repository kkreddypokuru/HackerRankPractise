import re

with open("D:/IdeaProjects/HackerRankPractise/text_data/sample.txt", "r") as f:
    s = {w.lower() for ln in f for w in re.split(r"\W+", ln) if w}
print(s)
