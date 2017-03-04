#! python3

import urllib.request
import re

class Reptile:
    url = "http://trend.baidu.lecai.com/gd11x5/baseTrend.action?recentDay=1&onlyBody=false&phaseOrder=up"

    def htmlString(self):
        data = urllib.request.urlopen(self.url).read()
        htmlString = data.decode('UTF-8')

        return htmlString

    #获取结果列表数据
    def tBody(self):
        startString = "<tbody>"
        endString = "</tbody>"
        htmlString = self.htmlString()
        startIndex = htmlString.find(startString)
        endIndex = htmlString.find(endString)
        tBodyHtmlString = htmlString[startIndex:endIndex+len(endString)]

        return  tBodyHtmlString

    #最近一天的历史开奖结果
    def historyResultArray(self):
        tBodyString = self.tBody()
        pattern = re.compile(r'<td class="chart_table_td red_ball.>\d\d</td>')
        elementStringArray = re.findall(pattern, tBodyString)

        numberArray =[]
        winNumber = set()
        for str in elementStringArray:
            subPattern = re.compile(r'<td class="chart_table_td red_ball.>')
            subString = re.sub(subPattern, "", str)
            subPattern = re.compile(r'</td>')
            subString = re.sub(subPattern, "", subString)
            winNumber.add(int(subString))
            if len(winNumber) == 5:#提取出来一个号码
                numberArray.append(winNumber)
                winNumber = set()

        return numberArray

     #最近一天的历史开奖结果, 删除最早的5期, 将剩下的79期作为参考, 与接下来追号的5期, 组成一个完整的周期
    def  referenceArray(self):
        historyArray = self.historyResultArray()
        for i in range(0, 5):
            del historyArray[i]

        return historyArray

    #获取最近几期的结果
    def lastArrayOfCount(self, count = 0):
        historyArray = self.historyResultArray()
        resultArray = historyArray[-count:]

        return resultArray
