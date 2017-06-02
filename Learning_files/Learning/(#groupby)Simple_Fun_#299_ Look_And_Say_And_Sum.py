#!/usr/bin/env python3
# coding: utf-8
# Test.assert_equals(look_and_say_and_sum(1),1)
# Test.assert_equals(look_and_say_and_sum(2),2)
# Test.assert_equals(look_and_say_and_sum(3),3)
# Test.assert_equals(look_and_say_and_sum(4),5)
# Test.assert_equals(look_and_say_and_sum(5),8)
import datetime as dt
start = dt.datetime.now()

# def generator(n):
#     if n == 1:return '1'
#     last = generator(n - 1)
#     length = len(last)
#     temp = last[0]
#     result = ''
#     for i in range(1,length):
#         if last[i] == temp[-1]:
#             temp += last[i]
#         else:
#             result += str(len(temp)) + temp[0]
#             temp = last[i]
#     result += str(len(temp)) + temp[0]
#     return result
#
# def look_and_say_and_sum(n):
#     return sum(map(int,generator(n)))

look_and_say_and_sum=l=lambda n,s='1':n<2and sum(map(int,s))or l(n-1,''.join(str(len(list(g)))+k for k,g in __import__('itertools').groupby(s)))
for i in range(1,10):
    print(i,look_and_say_and_sum(i))

end = dt.datetime.now()
print(end - start)
