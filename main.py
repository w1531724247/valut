#! python3

import buyLotteryModule

buyE = buyLotteryModule.BuyEvent()

resultDict = buyE.giveMeANumber()
resultNum = {}

values = []
for x in range(1,12):
    value = resultDict[x]
    values.append(value)

values.sort()
values = values[-3:]

for v in values:
    for w in range(1,12):
        vl = resultDict[w]
        if vl == v:
            resultNum[w] = v

print(resultNum)