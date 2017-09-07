#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

# def solution(roman):
#     return roman.count('M')*1000+roman.count('D')*500+roman.count('C')*100+roman.count('L')*50+roman.count('X')*10+roman.count('V')*5+roman.count('I')-roman.count('CM')*200-roman.count('CD')*200-roman.count('XC')*20-roman.count('XL')*20-roman.count('IX')*2-roman.count('IV')*2

values = [('M', 1000), ('CM', -200), ('D', 500), ('CD', -200),
          ('C', 100), ('XC', -20), ('L', 50), ('XL', -20),
          ('X', 10), ('IX', -2), ('V', 5), ('IV', -2),
          ('I', 1)]
def solution(roman):
    return sum(roman.count(s)*v for s,v in values)

print(solution('XXI'))

end = dt.datetime.now()
print(end - start)
