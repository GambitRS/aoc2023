from days import day


class Day2(day.Day):

    def __init__(self):
        super(Day2, self).__init__(2)

    def start1(self):
        file = self.ex1()
        #file = self.inputfile()
        self.answer(1,"nothing")

    def start2(self):
        file = self.ex2()
        #file = self.inputfile()
        self.answer(2,"nothing")
