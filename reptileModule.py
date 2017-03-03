#! python3

import urllib.request

class Reptile:
    url = "http://trend.baidu.lecai.com/gd11x5/baseTrend.action?recentDay=1&onlyBody=false&phaseOrder=up"

    def htmlString(self):
        data = urllib.request.urlopen(self.url).read()
        htmlString = data.decode('UTF-8')
        return htmlString

    #获取结果列表数据
    def getTBody(self):

        startString = "<tbody>"
        endString = "</tbody>"
        htmlString = self.htmlString()
        startIndex = htmlString.find(startString)
        endIndex = htmlString.find(endString)
        tBodyHtmlString = htmlString[startIndex:endIndex+len(endString)]
        return  tBodyHtmlString
        