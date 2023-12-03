from days import day


class Day5(day.Day):

    def __init__(self):
        super(Day5, self).__init__(5)

    def start1(self):

        file = self.ex1()
        while True:
            line = file.readline()

            if not line:
                break
        self.answer(1, "nothing yet")

    def start2(self):

        file = self.ex1()
        while True:
            line = file.readline()

            if not line:
                break

        self.answer(2, "nothing yet")
