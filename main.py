#! python3

import buyLotteryModule

buy = buyLotteryModule.BuyEvent()

threeArray = buy.threeNumArray()

for th in threeArray:
    print(th.threeNumSet)