#! python3

class BuyEvent:
    totalCost = 0 #此次购买的总成本 = 注数*2
    singleCost = 2 #单注彩票的价格
    winRate = 0.0 #此次购买中奖的概率
    numArray = [] #购买的数字
    totalFiveCount = 462 #不重复的五个数字的所有组合
    totalThreeCount = 20 #不重复的三个数字的所有组合
    atleastContainThreeOddNumCount = 281 #在462个不重复的号码中, 至少包含3个奇数以上的的号码有281
    threeOddNumAppearRate = 0.6082251082251082 #出现至少三个奇数的概率
    theThreeNumAppearRate = 0.06060606060606061 #某一个三位奇数的数字出现的概率
    everyNumFinalAppearRate = 5/11 #每一个数字出现的总概率用该无限趋近与这个值

    __baseNumArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    __oddArray = [1, 3, 5, 7, 9, 11]

    #每一次开奖可能出现的所有结果
    def fiveNumArray(self):
        totalFiveArray = []
        for a in self.__baseNumArray:
            for b in self.__baseNumArray:
                for c in self.__baseNumArray:
                    for d in self.__baseNumArray:
                        for e in self.__baseNumArray:
                            fiveNumSet = {a, b, c, d, e}
                            if len(fiveNumSet) == 5:
                                totalFiveArray.append(fiveNumSet)

        singleArray = []
        for fiveNumSet in totalFiveArray:
            notContain = True
            for fiveNS in singleArray:
                if fiveNS == fiveNumSet:
                    notContain = False
            if notContain:
                singleArray.append(fiveNumSet)

        return singleArray

    #三位奇数的所有的组合
    def threeNumArray(self):
        totalThreeArray = []
        for i in self.__oddArray:
            for j in self.__oddArray:
                for k in self.__oddArray:
                    threeNumSet = {i, j, k}
                    if len(threeNumSet) == 3:
                        totalThreeArray.append(threeNumSet)

        singleThreeArray = []
        for threeNumSet in totalThreeArray:
            notContain = True
            for threeNS in singleThreeArray:
                if threeNS == threeNumSet:
                    notContain = False
            if notContain:
                singleThreeArray.append(threeNumSet)

        return singleThreeArray

    #在所有的五位数中, 至少包含三个奇数的数字的组合
    def atleastContainThreeOddNumArray(self):
        numArray = []
        for fiveNum in self.fiveNumArray():
            oddCount = 0
            for x in fiveNum:
                if x%2 != 0:
                    oddCount += 1
                if oddCount >= 3:
                    numArray.append(fiveNum)
                    break
        return  numArray

    #某一个特定的三个奇数, 在一次开奖中出现的概率
    def theThreeNumAppearRate(self):
        threeNumArray = self.threeNumArray()
        threeNum = threeNumArray[0]
        appearCount = 0
        for fiveNum in self.fiveNumArray():
            if threeNum == (fiveNum & threeNum):
                appearCount += 1
        rate = appearCount/self.totalFiveCount
        return rate

    #每一个数字出现的总概率用该无限趋近与这个值
    def everyNumFinalAppearRate(self):
        appearCount = 0
        for fiveNum in self.fiveNumArray():
            if 1 in fiveNum:
                appearCount += 1
        rate = appearCount/self.totalFiveCount
        return  rate






