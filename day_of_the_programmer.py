# day of the programmer https://www.hackerrank.com/challenges/day-of-the-programmer/problem


def dayOfProgrammer(year):
    if year < 1918:
        leap = True if year % 4 == 0 else False
    else:
        leap = True if (year % 400 == 0) or (year %
                                             4 == 0 and year % 100 != 0) else False
    d = (13 - (1 if leap else 0), 9, year)
    if year == 1918:
        # transition year from Julian to Gregorian
        # from jan 31 -> feb 14, feb 14 was the 32th day
        d = (26, 9, year)

    return "%02d.%02d.%d" % d

if __name__ == "__main__":
    y = 1918
    print(dayOfProgrammer(y))
    y = 1800
    print(dayOfProgrammer(y))
    y = 2100
    print(dayOfProgrammer(y))
