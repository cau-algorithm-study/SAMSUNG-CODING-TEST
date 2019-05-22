

def main():
    inputfile = open('sample_input.txt', 'r')
    contents = inputfile.readlines()

    totaltestcase = contents[0].rstrip()
    index = 1
    answers = list()

    for i in range(int(totaltestcase)):
        answerList = list()
        first = list()
        second = list()
        third = list()
        fourth = list()
        testCondition = list()

        numOftest = contents[index].rstrip()
        index += 1

        first.append(contents[index].rstrip())
        index += 1
        second.append(contents[index].rstrip())
        index += 1
        third.append(contents[index].rstrip())
        index += 1
        fourth.append(contents[index].rstrip())
        index += 1

        print('=== {} === '.format(i))
        for num in range(int(numOftest)):
            testCondition.append(contents[index].rstrip())
            index += 1

            # Algorithm
            answerList = specialMagnet(first, second, third,
                                       fourth, num, testCondition)
            # print('#{}'.format(answer), end="\n")
        print(answerList)
        answer = checkAnswer(answerList)
        print(answer)
    answers.append(answer)
    print(answers)
    inputfile.close()


def specialMagnet(first, second, third, fourth, num, testCondition):

    eachTestList = eachTestcase(first, second, third, fourth)
    print('init List ')
    print(eachTestList)
    print('test condition : ', testCondition)

    eachTestList = execute(eachTestList, num, testCondition)
    # print(eachTestList)

    return eachTestList


def checkAnswer(eachTestList):
    answer = 0

    if eachTestList[0][0] == 0:
        answer += 1
    if eachTestList[1][0] == 0:
        answer += 2
    if eachTestList[2][0] == 0:
        answer += 4
    if eachTestList[3][0] == 0:
        answer += 8

    return answer


def execute(eachTestList, num, testCondition):
    eachCondition = testCondition[num].split(" ")
    # print(eachCondition)
    magnet = int(eachCondition[0])
    direction = int(eachCondition[1])
    FirstMagnet = eachTestList[0]
    SecondMagnet = eachTestList[1]
    ThirdMagnet = eachTestList[2]
    FourthMagnet = eachTestList[3]

    checkValue1 = FirstMagnet[2]
    checkValue2 = [SecondMagnet[2], SecondMagnet[6]]
    checkValue3 = [ThirdMagnet[2], ThirdMagnet[6]]
    checkValue4 = FourthMagnet[6]

    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False

    if magnet == 1:
        if checkValue1 != checkValue2[0]:
            flag1 = True
            flag2 = True
        if flag2 and checkValue2[1] != checkValue3[0]:
            flag3 = True
        if flag3 and checkValue3[1] != checkValue4:
            flag4 = True
        FirstMagnet = rotateMagnet(FirstMagnet, direction, flag1)
        SecondMagnet = rotateMagnet(SecondMagnet, -direction, flag2)
        ThirdMagnet = rotateMagnet(ThirdMagnet, direction, flag3)
        FourthMagnet = rotateMagnet(FourthMagnet, -direction, flag4)

    elif magnet == 2:

        if checkValue2[1] != checkValue3[0]:
            flag2 = True
            flag3 = True
        if flag3 and checkValue3[1] != checkValue4:
            flag4 = True
        if checkValue1 != checkValue2[0]:
            flag2 = True
            flag1 = True

        FirstMagnet = rotateMagnet(FirstMagnet, direction, flag1)
        SecondMagnet = rotateMagnet(SecondMagnet, -direction, flag2)
        ThirdMagnet = rotateMagnet(ThirdMagnet, direction, flag3)
        FourthMagnet = rotateMagnet(FourthMagnet, -direction, flag4)

    elif magnet == 3:
        if checkValue2[1] != checkValue3[0]:
            flag3 = True
            flag2 = True
        if flag2 and checkValue1 != checkValue2[0]:
            flag1 = True
        if checkValue3[1] != checkValue4:
            flag3 = True
            flag4 = True

        FirstMagnet = rotateMagnet(FirstMagnet, direction, flag1)
        SecondMagnet = rotateMagnet(SecondMagnet, -direction, flag2)
        ThirdMagnet = rotateMagnet(ThirdMagnet, direction, flag3)
        FourthMagnet = rotateMagnet(FourthMagnet, -direction, flag4)

    elif magnet == 4:
        if checkValue3[1] != checkValue4:
            flag4 = True
            flag3 = True
        if flag3 and checkValue3[0] != checkValue2[1]:
            flag2 = True
        if flag2 and checkValue2[0] != checkValue1:
            flag1 = True

        FirstMagnet = rotateMagnet(FirstMagnet, direction, flag1)
        SecondMagnet = rotateMagnet(SecondMagnet, -direction, flag2)
        ThirdMagnet = rotateMagnet(ThirdMagnet, direction, flag3)
        FourthMagnet = rotateMagnet(FourthMagnet, -direction, flag4)

    return [FirstMagnet, SecondMagnet, ThirdMagnet, FourthMagnet]


def rotateMagnet(lst, direction, flag):
    newlist = list()
    if flag:
        if direction == 1:
            newlist.insert(0, lst[7])
            for i in range(7):
                newlist.append(lst[i])
        elif direction == -1:
            for i in range(7):
                newlist.append(lst[i+1])
            newlist.append(lst[7])

    else:
        #print('not rotated : ', lst)
        return lst
    #print('rotated : ', newlist)
    return newlist


def eachTestcase(first, second, third, fourth):

    eachTestList = list()

    # Init
    eachTestList.append(makeIntlist(first))
    eachTestList.append(makeIntlist(second))
    eachTestList.append(makeIntlist(third))
    eachTestList.append(makeIntlist(fourth))

    return eachTestList


def makeIntlist(lst):
    intList = list()
    newList = lst[0].split(" ")

    for i in range(8):
        intList.append(int(newList[i]))

    return intList


if __name__ == "__main__":
    main()
