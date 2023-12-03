from days import day


class Day1(day.Day):

    def __init__(self):
        super(Day1, self).__init__(1)

    def start1(self):
        file1 = self.inputfile()
        count = 0
        result = 0
        while True:
            count += 1
            line = file1.readline()

            if not line:
                break

            line = line.strip()
            max = len(line)
            first = -1
            last = -1

            for index in range(0, max):
                first = self.findnum1(line, index)
                if first > -1:
                    break

            for index in range(max-1, -1, -1):
                last = self.findnum1(line, index)
                if last > -1:
                    break

            result = result + int("{}{}".format(first,last))
            #print("{} {}".format(first, last))
            #print("Line{}: {}".format(count, line))
        self.answer(1, result)

    def findnum1(self, line, pos):
        #print(line[pos])
        try:
            return int(line[pos])
        except ValueError:
            return -1
            #print("not an int")

    def start2(self):
        file1 = self.inputfile()
        count = 0
        result = 0
        while True:
            count += 1
            line = file1.readline()

            if not line:
                break

            line = line.strip()
            max = len(line)
            first = -1
            last = -1

            for index in range(0, max):
                first = self.findnum2(line,index)
                if first > -1:
                    break

            for index in range(max-1, -1, -1):
                last = self.findnum2(line, index)
                if last > -1:
                    break

            result = result + int("{}{}".format(first,last))
            #print("{} {}".format(first, last))
            #print("Line{}: {}".format(count, line))
        self.answer(2,result)

    def findnum2(self, line, pos):
        #print(line[pos])
        try:
            return int(line[pos])
        except ValueError:
            max = len(line)
            if max-pos > 2:
                word = line[pos:pos+3]
                if word == "one": return 1;
                if word == "two": return 2;
                if word == "six": return 6;
            if max-pos > 3:
                word = line[pos:pos+4]
                if word == "four": return 4;
                if word == "five": return 5;
                if word == "nine": return 9;
            if max-pos > 4:
                word = line[pos:pos+5]
                if word == "three": return 3;
                if word == "seven": return 7;
                if word == "eight": return 8;

        return -1
