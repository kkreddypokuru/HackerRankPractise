# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    elif (1700 <= year <= 1917 and year % 4 == 0) or (year > 1918 and year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return "12.09.%s" % year
    else:
        return "13.09.%s" % year


year = 1800
final = dayOfProgrammer(year)
print(final)
