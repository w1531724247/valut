#! python3

import winRate
import reptileModule

reptileM = reptileModule.Reptile()
winR = winRate.WinRate()
historyArray = winR.toDayNotAppearNum()
print(len(historyArray))
"""
dCount  = 0
while count > 0:
    numSet = historyArray.pop()
    for num in historyArray:
        if num == numSet:
            dCount += 1
            print(num, " == ", numSet)
    count -= 1

print(dCount)
"""