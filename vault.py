#! python3

import fiveNumModule
import threeNumModule

baseNumArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
oddArray = [1, 3, 5, 7, 9, 11]
threeOddArray = [] #三个奇数号码的所有的情况

for i in oddArray:
    for j in oddArray:
        for k in oddArray:
            if ( i != j ) and ( j != k ) and ( i != k ):
                tempSet = {i, j, k}
                threeNum = threeNumModule.ThreeNum()
                threeNum.threeNumSet = tempSet
                threeOddArray.append(threeNum)

#排除threeOddArray中三个数字相同但顺序不同的情况
finalThreeOddArray = [] #最终的没有重复情况的三个数字的组合
while len(threeOddArray) > 0:
    currentThreeNum = threeOddArray.pop()
    finalThreeOddArray.append(currentThreeNum)
    for threeNum in threeOddArray:
        if threeNum.threeNumSet == currentThreeNum.threeNumSet:
            threeOddArray.remove(threeNum)
else:
    finalThreeOddArray.pop() #最后总是多出来一个重复的不知道为什么

totalArray = [] #所有的情况
for a in baseNumArray:
    for b in baseNumArray:
        for c in baseNumArray:
            for d in baseNumArray:
                for e in baseNumArray:
                    set = {a, b, c, d, e}
                    items = len(set)
                    if items == 5:
                        fiveNum = fiveNumModule.FiveNum()
                        fiveNum.fiveNumSet = set
                        totalArray.append(fiveNum)

atLeastThreeOddArray = [] #至少包含三个奇数的情况
for fiveNum in totalArray:
    oddCount = 0
    for n in fiveNum.fiveNumSet:
        remainNum = n%2
        if remainNum != 0:
            oddCount += 1
            if oddCount >= 3:
                atLeastThreeOddArray.append(fiveNum)
                break

threeOddNumWinRate = len(atLeastThreeOddArray)/len(totalArray) #三个奇数的情况所占的比例

cost = 2.0
threeNumAppearRateDict = {} #某三个奇数出现的总次数所占的比例
for threeNum in finalThreeOddArray: #三个奇数的情况
    appearCount = 0
    for fiveNum in atLeastThreeOddArray: #至少三个奇数的情况
        if threeNum.threeNumSet == threeNum.threeNumSet & fiveNum.fiveNumSet:
            appearCount += 1
    setString = str(threeNum.threeNumSet)
    threeNumAppearRateDict[setString] = appearCount

#每一个三位奇数的组合出现每一次开奖出现的概率
for threeNum in finalThreeOddArray:
    setString = str(threeNum.threeNumSet)
    appearCount = threeNumAppearRateDict[setString]
    appearRate = appearCount/len(totalArray)

"""
每三个奇数中奖概率 = 出现的总次数/总注数 = 0.06060606060606061
每三个奇数出现的总次数 = 可以在至少有三个奇数的数组中统计出来

每三个奇数中奖概率 = 至少有三个奇数的概率*(每三个奇数出现的总次数/至少有三个奇数的数组总数) = 0.06060606060606061
"""