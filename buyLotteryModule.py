#! python3

import fiveNumModule
import threeNumModule

class BuyEvent:
    totalCost = 0 #此次购买的总成本 = 注数*2
    singleCost = 2 #单注彩票的价格
    winRate = 0.0 #此次购买中奖的概率
    numArray = [] #购买的数字
    __baseNumArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    __oddArray = [1, 3, 5, 7, 9, 11]

    def fiveNumArray(self): #五个数字的所有组合
        totalArray = [] #所有的情况
        for a in self.__baseNumArray:
            for b in self.__baseNumArray:
                for c in self.__baseNumArray:
                    for d in self.__baseNumArray:
                        for e in self.__baseNumArray:
                            set = {a, b, c, d, e}
                            items = len(set)
                            if items == 5:
                                fiveNum = fiveNumModule.FiveNum()
                                fiveNum.fiveNumSet = set
                                totalArray.append(fiveNum)
        return  totalArray

    def threeNumArray(self):
        threeOddArray = [] #三个奇数号码不重复的所有的情况
        for i in self.__oddArray:
            for j in self.__oddArray:
                for k in self.__oddArray:
                    if ( i != j ) and ( j != k ) and ( i != k ):
                        tempSet = {i, j, k}
                        threeNum = threeNumModule.ThreeNum()
                        threeNum.threeNumSet = tempSet
                        needAdd = True
                        for tnm in threeOddArray:
                            if tnm.threeNumSet == tempSet:
                                needAdd = False
                        if needAdd:
                           threeOddArray.append(threeNum)
        return threeOddArray

    def totalCount(self):
        return  len(self.fiveNumArray())











