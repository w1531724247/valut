#! python3
#! 中奖率计算类

import reptileModule
import threeOddNumMudole
import fiveNumMudole

class WinRate:
    #从11位数中取5位, 总共有462中情况, 每天84期, 相当于从462个数中取84个数, 但是有10个数,出现了两次, 所以一天这84个数中,
    #有74个都是只出现一次的, 所以每一个五位数, 每一次出现的概率是1/462, 每一天出现的概率是84/462, 也就是说假如一个数今天出现过了,
    #那么今天再次出现的概率就很小,基本可以忽略不计,
    #所以再买的话就从今天还没出现过的数字里买
    #因为是以84期为一个单位, 而追号期数为5期, 所以要以之前79期作为接下来五期的依据, 一遍过去的79期, 与接下来的5期组成一个单位周期
    #每一组三位奇数, 每天平均出现5次, 每次出现的平均间隔是16期, 所以在过去13期内出现过的奇数组合, 在接下来的5期内出现的概率变小
    #在过去的32期里面总共出现了33次三个奇数的情况, 涉及15个奇数组, 平均每个出现了两次,
    #在过去的16期里面总共出现了19次三个奇数的情况, 涉及12个奇数组, 有7个出现了两次
    #在过去的13期里面总共出现了14次三个奇数的情况, 涉及11个奇数组, 有3个出现了两次
    
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
    countOfEveryThreeOddNumAppearEveryDay = 5 #每天每个三位奇数组合出现的总次数因该是5~6次

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

        resultArray = []
        for set in singleArray:
            fiveNum = fiveNumMudole.fiveNum()
            fiveNum.numSet = set
            resultArray.append(fiveNum)

        return resultArray

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

        resultArray = []
        for set in singleThreeArray:
            threeOddNum = threeOddNumMudole.threeOddNum()
            threeOddNum.numSet = set
            resultArray.append(threeOddNum)

        return resultArray

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
        lastFiveNum = self.__reptlie.lastArrayOfCount(10)
        #因为连续出现10次和连续10次出现都是不可能的
        for x in self.__baseNumArray:
            for numSet in lastFiveNum:
                if x in numSet: #在过去的10次里,每出现一次,则下面一次出现的概率减0.1
                    newRate = self.everyNumAppearRateInNextThreeTimes[x]
                    newRate -= 0.1
                    self.everyNumAppearRateInNextThreeTimes = newRate
                else: #在过去的10次里,每少出现一次,则下面一次出现的概率加0.1
                    newRate = self.everyNumAppearRateInNextThreeTimes[x]
                    newRate += 0.1
                    self.everyNumAppearRateInNextThreeTimes = newRate
        return

    #每一个数字在过去80次中出现的概率与平均概率只差越大, 下面1次出现的概率越大
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

    def toDayNotAppearNum(self): #今天还没出现过的号码, 选的时候就从这里面选
        fiveNumArray = self.fiveNumArray()
        historyArray = self.__reptlie.historyResultArray()

        for fiveNumSet in historyArray:
            for fiveNumModel in fiveNumArray:
                if fiveNumModel.numSet == fiveNumSet:
                    fiveNumArray.remove(fiveNumModel)
                    print("删除了一个数字", fiveNumSet)

        return fiveNumArray

    #每一个三位奇数组成的组合今天已经出现的次数
    def everyThreeOddNumHasAppearTimes(self):
        threeOddNumArray = self.threeNumArray()
        referenceArray = self.__reptlie.referenceArray()
        totalCount = 0
        for threeOddNumModel in threeOddNumArray:
            appearCount = 0
            threeNumSet = threeOddNumModel.numSet
            for numSet in referenceArray:
                if threeNumSet == (threeNumSet & numSet):
                    appearCount += 1
                    totalCount += 1
            print(threeNumSet, ":appearcount = ", appearCount)
        print("totalCount: ", totalCount)
        return

    #统计在最近的13期中出现过的三位奇数的组合
    def appearedThreeOddNumArrayInLast13Terms(self):
        last13TermNum = self.__reptlie.lastArrayOfCount(13)
        appearArray = []
        for threeOddNumModel in self.threeNumArray():
            threeNumSet = threeOddNumModel.numSet
            for fiveNumSet in last13TermNum:
                if threeNumSet == (threeNumSet & fiveNumSet):
                    appearArray.append(threeNumSet)
        return appearArray

    #在最近13期中没有出现的三位奇数的组合在,接下来五期中出现的概率变大
    def notAppearedThreeOddNumArrayInLast13Terms(self):
        threeNumArray = []
        for threeNumModel in self.threeNumArray():
            threeNumArray.append(threeNumModel.numSet)
        print("threeNumArray: ", len(threeNumArray))
        appearedNumArray = self.appearedThreeOddNumArrayInLast13Terms()
        print("appearedNumArray: ", len(appearedNumArray))
        notAppearNumArray = []
        for numSet in threeNumArray:
            notFound = True
            for appearNumSet in appearedNumArray:
                if appearNumSet == numSet:
                    notFound = False
            if notFound:
                notAppearNumArray.append(numSet)
        print("notAppearNumArray: ", len(notAppearNumArray))
        return notAppearNumArray

    #充值每一个数字在接下来的三次里出现的概率
    def resetEveryNumAppearRateInNextThreeTimes(self):
        r = 5/11
        self.everyNumAppearRateInNextThreeTimes = {1:r,2:r,3:r,4:r,5:r,6:r,7:r,8:r,9:r,10:r,11:r}
        return


