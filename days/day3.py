from days import day


class Day3(day.Day):

    def __init__(self):
        super(Day3, self).__init__(3)

    def start1(self):

        total = 0
        mymap = []
        file = self.inputfile()
        while True:
            line = file.readline()
            line = line.strip('\n')
            mymap.append(list(line))

            if not line:
                break

        for line in range(0, len(mymap)):
            for elem in range(0, len(mymap[line])):
                total += self.process(mymap, line, elem)

        #print(mymap)
        self.answer(1, total)

    def process(self, mymap, line, elem):
        char = mymap[line][elem]

        if char == ".":
            return 0

        if char.isnumeric():
            return 0

        #print("{} l: {} e: {}".format(char, line, elem))
        total = 0
        for x in range(elem-1, elem+2):
            for y in range(line-1, line+2):
                total += self.findnumber(mymap, x, y)

        return total

    def findnumber(self, mymap, x, y):
        if not mymap[y][x].isnumeric():
            return 0

        low = x
        high = x

        while True:
            if low == 0:
                break
            if not mymap[y][low-1].isnumeric():
                break
            low -= 1

        while True:
            if high == len(mymap[y])-1:
                break
            if not mymap[y][high+1].isnumeric():
                break
            high += 1

        nr = ''
        for i in range(low, high+1):
            nr += mymap[y][i]
            mymap[y][i] = '.'

        #print("nr:{}".format(nr))
        return int(nr)

    def start2(self):

        total = 0
        mymap = []
        file = self.inputfile()
        while True:
            line = file.readline()
            line = line.strip('\n')
            mymap.append(list(line))

            if not line:
                break

        for line in range(0, len(mymap)):
            for elem in range(0, len(mymap[line])):
                total += self.process2(mymap, line, elem)

        # print(mymap)
        self.answer(2, total)

    def process2(self, mymap, line, elem):
        char = mymap[line][elem]

        if not char == "*":
            return 0

        #print("{} l: {} e: {}".format(char, line, elem))
        total = 1
        amount = 0
        for x in range(elem - 1, elem + 2):
            for y in range(line - 1, line + 2):
                found = self.findnumber2(mymap, x, y)
                if found > 0:
                    total *= found
                    amount += 1
                    if amount > 2:
                        return 0

        if amount < 2:
            return 0

        return total

    def findnumber2(self, mymap, x, y):
        if not mymap[y][x].isnumeric():
            return 0

        low = x
        high = x

        while True:
            if low == 0:
                break
            if not mymap[y][low - 1].isnumeric():
                break
            low -= 1

        while True:
            if high == len(mymap[y]) - 1:
                break
            if not mymap[y][high + 1].isnumeric():
                break
            high += 1

        nr = ''
        for i in range(low, high + 1):
            nr += mymap[y][i]
            mymap[y][i] = '.'

        # print("nr:{}".format(nr))
        return int(nr)
