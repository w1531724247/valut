#! python3

class ThreeNum:
    threeNumSet = {}

    __threeNumArray = [] #三个数字的数组
    def addNum(self, num):
        if len(self.__threeNumArray) == 0:
            if num = 1 or num == 11:
                self.__threeNumArray.append(1)
                self.__threeNumArray.append(11)
            if num = 3 or num == 9:
                self.__threeNumArray.append(3)
                self.__threeNumArray.append(9)
            if num = 5 or num == 7:
                self.__threeNumArray.append(5)
                self.__threeNumArray.append(7)
        elif len(self.__threeNumArray) == 2:
            self.__threeNumArray.append(num)
        else:
            self.threeNumSet = {self.__threeNumArray[0], self.__threeNumArray[1], self.__threeNumArray[2]}
            return
        return




