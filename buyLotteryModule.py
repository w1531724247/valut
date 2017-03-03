#! python3

import reptileModule

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

    everyNumAppearRateInNextThreeTimes = {} #每一个数字在接下来的三次里出现的概率
    __reptlie = reptileModule.Reptile() #爬虫
    __baseNumArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    __oddArray = [1, 3, 5, 7, 9, 11]
    __smaleNumArray = [1,2,3,4] #小号
    __middleNumArray = [5, 6, 7] #中号
    __bigNumArray = [8, 9, 10, 11]#大号

    #选号
    def giveMeANumber(self):
        self.resetEveryNumAppearRateInNextThreeTimes()
        self.everyNumHasAppearRateInPass80Times()
        self.analysisSmaleMiddleAndBigRate()
        self.everyNumLast10TimesAppearDecrease()
        self.everyNumLast10TimesAppearDecrease()
        self.analysisEveryNumAppearRateInNextThreeNum()

        return self.everyNumAppearRateInNextThreeTimes

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

    #分析每一个数字在接下来的三次里出现的概率
    def analysisEveryNumAppearRateInNextThreeNum(self):
        lastFiveNum = self.__reptlie.lastArrayOfCount(5)
        for x in self.__baseNumArray:
            appearCount = 0
            for numSet in lastFiveNum:
                if x in numSet:
                    appearCount += 1
            if appearCount == 5:#如果连续出了五次,则认为接下来三次出现的概率是0
                self.everyNumAppearRateInNextThreeTimes[x] = 0.0
            elif appearCount == 0:#如果连续五次没出,则认为接下来三次总出现的概率是1
                self.everyNumAppearRateInNextThreeTimes[x] = 1.0
        return

    #每一个数字在过去80次中出现的概率与平均概率只差越大, 下面三次出现的概率越大
    def everyNumHasAppearRateInPass80Times(self):
        numArray = self.__reptlie.lastArrayOfCount(80)
        for x in self.__baseNumArray:
            appearCount = 0
            for numSet in numArray:
                if x in numSet:
                    appearCount += 1
            oldAppearRate = appearCount/80 #已经出现的概率
            averageRate = 5/11 #平均出现的概率
            if averageRate > oldAppearRate:
                newRate = self.everyNumAppearRateInNextThreeTimes[x]
                if newRate < 1:
                    newRate += (averageRate-oldAppearRate)
                    self.everyNumAppearRateInNextThreeTimes[x] = newRate
        return

    #分析最近5期和最近6到10期的小中大号的分布情况
    def analysisSmaleMiddleAndBigRate(self, middleNumCount=None):
        lastTenNum = self.__reptlie.lastArrayOfCount(10)
        ontToFiveNum = lastTenNum[-5:] #最近5期
        tenToSixNum = lastTenNum[:5] #最近6到10期

        bigAppear = False
        middleAppear = False
        smaleAppear = False

        bigNumCount = 0
        middleNumCount = 0
        smaleNumCount = 0
        for num in ontToFiveNum:
            for x in num:
                if x in self.__smaleNumArray:
                    smaleNumCount += 1
                elif x in self.__middleNumArray:
                    middleNumCount += 1
                elif x in self.__bigNumArray:
                    bigNumCount += 1
        bigNum = 0
        if bigNumCount > middleNumCount:
            bigNum = bigNumCount
        else:
            bigNum = middleNumCount

        if bigNum > smaleNumCount:
            bigNum = bigNum
        else:
            bigNum = smaleNumCount

        if bigNum == bigNumCount:
            bigAppear = True
        elif bigNum == middleAppear:
            middleAppear = True
        elif smaleAppear == smaleNumCount:
            smaleAppear = True

        bigNumCount = 0
        middleNumCount = 0
        smaleNumCount = 0
        for num in tenToSixNum:
            for x in num:
                if x in self.__smaleNumArray:
                    smaleNumCount += 1
                elif x in self.__middleNumArray:
                    middleNumCount += 1
                elif x in self.__bigNumArray:
                    bigNumCount += 1
        bigNum = 0
        if bigNumCount > middleNumCount:
            bigNum = bigNumCount
        else:
            bigNum = middleNumCount

        if bigNum > smaleNumCount:
            bigNum = bigNum
        else:
            bigNum = smaleNumCount

        if bigNum == bigNumCount:
            bigAppear = True
        elif bigNum == middleAppear:
            middleAppear = True
        elif smaleAppear == smaleNumCount:
            smaleAppear = True

        if smaleAppear == False:
            for x in self.__smaleNumArray:
                newRate = self.everyNumAppearRateInNextThreeTimes[x]
                newRate += 0.01
                self.everyNumAppearRateInNextThreeTimes[x] = newRate
        elif middleAppear == False:
            for x in self.__middleNumArray:
                newRate = self.everyNumAppearRateInNextThreeTimes[x]
                newRate += 0.01
                self.everyNumAppearRateInNextThreeTimes[x] = newRate
        elif bigAppear == False:
            for x in self.__middleNumArray:
                newRate = self.everyNumAppearRateInNextThreeTimes[x]
                newRate += 0.01
                self.everyNumAppearRateInNextThreeTimes[x] = newRate
        return

    #过去10次中出现次数最多的数,接下来三次出现的概率变小
    def everyNumLast10TimesAppearIncrease(self):
        lastTenNum = self.__reptlie.lastArrayOfCount(10)
        numAndAppearTimes = {} #数字在过去10期中出现的次数
        for x  in self.__baseNumArray:
            appearCount = 0
            for num in lastTenNum:
                if x in num:
                    appearCount += 1
                    numAndAppearTimes[x] = appearCount

        bigCountNum = 0
        for y in range(0,10):
            preAppearCount = numAndAppearTimes[y+1]
            nextAppearCount = numAndAppearTimes[y+2]
            tempNum = 0
            if preAppearCount > nextAppearCount:
                tempNum = preAppearCount
            else:
                tempNum = nextAppearCount

            if tempNum > bigCountNum:
                bigCountNum = tempNum
            else:
                bigCountNum = bigCountNum

        for z in self.__baseNumArray:
            appearCount = numAndAppearTimes[z]
            if appearCount == bigCountNum:
                newRate = self.everyNumAppearRateInNextThreeTimes[z]
                newRate -= 0.01
                self.everyNumAppearRateInNextThreeTimes[z] = newRate
        return

    #过去10次中出现次数最少的数, 接下来出现的概率变大
    def everyNumLast10TimesAppearDecrease(self):
        lastTenNum = self.__reptlie.lastArrayOfCount(10)
        numAndAppearTimes = {} #数字在过去10期中出现的次数
        for x  in self.__baseNumArray:
            appearCount = 0
            for num in lastTenNum:
                if x in num:
                    appearCount += 1
                    numAndAppearTimes[x] = appearCount

        smaleCountNum = 0
        for y in range(0,10):
            preAppearCount = numAndAppearTimes[y+1]
            nextAppearCount = numAndAppearTimes[y+2]
            tempNum = 0
            if preAppearCount < nextAppearCount:
                tempNum = preAppearCount
            else:
                tempNum = nextAppearCount

            if tempNum < smaleCountNum:
                smaleCountNum = tempNum
            else:
                smaleCountNum = smaleCountNum

        for z in self.__baseNumArray:
            appearCount = numAndAppearTimes[z]
            if appearCount == smaleCountNum:
                newRate = self.everyNumAppearRateInNextThreeTimes[z]
                newRate += 0.01
                self.everyNumAppearRateInNextThreeTimes[z] = newRate
        return

    #充值每一个数字在接下来的三次里出现的概率
    def resetEveryNumAppearRateInNextThreeTimes(self):
        self.everyNumAppearRateInNextThreeTimes = {1:0.0, 2:0.0, 3:0.0, 4:0.0, 5:0.0, 6:0.0, 7:0.0, 8:0.0, 9:0.0, 10:0.0, 11:0.0}
        return


