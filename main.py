#! python3

import winRate
import reptileModule

winR = winRate.WinRate()
notAppearNumarray = winR.notAppearedThreeOddNumArrayInLast13Terms()

oddNumArray = [1,3,5,7,9,11]
oddNumRemainCount = {}

print(notAppearNumarray)

for num in oddNumArray:
    appearCount = 0
    for numSet in notAppearNumarray:
        if num in numSet:
            appearCount += 1
    oddNumRemainCount[num] = appearCount

print(oddNumRemainCount)