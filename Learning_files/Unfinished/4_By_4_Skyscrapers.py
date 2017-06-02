#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import datetime as dt
start = dt.datetime.now()


# 1:[4,1,2,3],[4,1,3,2],[4,2,1,3],[4,2,3,1],[4,3,1,2],[4,3,2,1]
# ->6
# 2:[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,1,2],[3,4,2,1]
#   [2,1,4,3],[2,4,1,3],[2,4,3,1]
#   [1,4,2,3],[1,4,3,2]
# ->11
# 3:[2,1,3,4],[2,3,1,4],[2,3,4,1]
#   [1,2,4,3],[1,3,2,4],[1,3,4,2]
# ->6
# 4:[1,2,3,4]
# ->1
def funcSolve14(result,clue):
    return 5-clue if clue == 1 or clue == 4 else result
def solvePuzzle(clues):
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for i in range(4):
        result[i][0] = funcSolve14(result[i][0],clues[i])
    for i in range(4,8):
        result[3][i-4] = funcSolve14(result[3][i-4],clues[i])
    for i in range(8,12):
        result[11-i][3] = funcSolve14(result[11-i][3],clues[i])
    for i in range(12,16):
        result[0][15-i] = funcSolve14(result[0][15-i],clues[i])
    return result

print([0,0,1,2,0,2,0,0,0,3,0,0,0,1,0,0])
print(np.array(solvePuzzle([0,0,1,2,0,2,0,0,0,3,0,0,0,1,0,0])))

end = dt.datetime.now()
print(end - start)
