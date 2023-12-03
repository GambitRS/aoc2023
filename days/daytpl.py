from days import day


class DayX(day.Day):

    def __init__(self):
        super(DayX, self).__init__(X)

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
