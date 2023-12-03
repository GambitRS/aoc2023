from days import day


class Day4(day.Day):

    def __init__(self):
        super(Day4, self).__init__(4)

    def start1(self):

        file = self.ex1()
        while True:
            line = file.readline()

            if not line:
                break
        self.answer(1,"nothing yet")

    def start2(self):

        file = self.ex1()
        while True:
            line = file.readline()

            if not line:
                break

        self.answer(2,"nothing yet")
