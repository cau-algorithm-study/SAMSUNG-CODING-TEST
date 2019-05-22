import os

def main():
    path = os.getcwd()
    try:
        with open(path + "\input.txt", 'r') as ins:
            array = []
            for line in ins:
                li = line.strip()
                array.append(line)

        T = int(array[0])
        K = int(array[1])

        jasuk1 = array[2].split(' ')
        for i in range(len(jasuk1)):
            jasuk1[i] = int(jasuk1[i])
        jasuk2 = array[3].split(' ')
        for i in range(len(jasuk2)):
            jasuk1[i] = int(jasuk2[i])
        jasuk3 = array[4].split(' ')
        for i in range(len(jasuk3)):
            jasuk1[i] = int(jasuk3[i])
        jasuk4 = array[5].split(' ')
        for i in range(len(jasuk4)):
            jasuk1[i] = int(jasuk4[i])

        rotate = array[6].split(' ')
        for i in range(len(rotate)):
            rotate[i] = int(rotate[i])

        rotatefunc(rotate, jasuk1, jasuk2, jasuk3, jasuk4)


    except FileNotFoundError:
        print("No such file or directory.")

#def scoring():

def rotatefunc(rotate, jasuk1, jasuk2, jasuk3, jasuk4):
    temp = [0 for x in range(len(jasuk1))]
    if rotate[0] == 1:
        if rotate[1] == 1:

            for i in range(len(jasuk1)-1):
                temp[i + 1] = int(jasuk1[i])
            temp[0] = int(jasuk1[-1])
            jasuk1 = temp
        else:
            for i in range(len(jasuk1)-1):
                temp[i] = int(jasuk1[i + 1])
            temp[-1] = int(jasuk1[0])
            jasuk1 = temp
        print(jasuk1)

    if rotate[0] == 2:
        if rotate[1] == 1:
            for i in range(len(jasuk2)-1):
                temp[i + 1] = int(jasuk2[i])
            temp[0] = int(jasuk2[-1])
            jasuk2 = temp
        else:
            for i in range(len(jasuk2)-1):
                temp[i] = int(jasuk2[i + 1])
            temp[-1] = int(jasuk2[0])
            jasuk2 = temp
        print(jasuk2)

    if rotate[0] == 3:
        if rotate[1] == 1:
            for i in range(len(jasuk3)-1):
                temp[i + 1] = int(jasuk3[i])
            temp[0] = int(jasuk3[-1])
            jasuk3 = temp

        else:
            for i in range(len(jasuk3)-1):
                temp[i] = int(jasuk3[i + 1])
            temp[-1] = int(jasuk3[0])
            jasuk3 = temp
        print(jasuk3)

    if rotate[0] == 4:
        if rotate[1] == 1:
            for i in range(len(jasuk4)-1):
                temp[i + 1] = int(jasuk4[i])
            temp[0] = int(jasuk4[-1])
            jasuk4 = temp
        else:
            for i in range(len(jasuk4)-1):
                temp[i] = int(jasuk1[i + 1])
            temp[-1] = int(jasuk4[0])
            jasuk4 = temp
        print(jasuk4)
    return jasuk1, jasuk2, jasuk3, jasuk4

if __name__ == "__main__":
    main()