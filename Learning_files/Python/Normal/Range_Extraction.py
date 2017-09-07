#!/usr/bin/env python2
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

def solution(args):
    result = '' + str(args[0])
    for i in xrange(1,len(args)-1):
        if args[i] - args[i-1] - 1 or args[i+1] - args[i] - 1:
            if result[-1] == '-':
                result += str(args[i]) + ','
            elif i == len(args) - 2:
                result += ',' + str(args[i]) + ','
            elif result[-1] == ',':
                result += str(args[i])
            else:
                result += ',' + str(args[i])
        else:
            if not result[-1] == '-':
                result += '-'
    result += str(args[-1])
    return result

print(solution([-3,-2,-1,2,10,15,16,18,19,20]))
print(solution([-88,-85,-84,-81,-80,-77,-75,-72,-71,-69,-68,-65,-62,-61,-60,-58,-55,-54,-51,-50,-48,-45,-43,-42,-40]))

end = dt.datetime.now()
print(end - start)
