class Day:
    def __init__(self, nr):
        self.name = "Day {}".format(nr)
        self.inputfolder = "inputs/day{}".format(nr)
        self.start1()
        self.start2()

    def answer(self, nr, answer):
        print("{}.{}: {}".format(self.name, nr, answer))

    def start1(self):
        self.answer(1, "not yet")

    def start2(self):
        self.answer(2, "not yet")

    def inputfile(self):
        return open("{}/input.txt".format(self.inputfolder))

    def ex1(self):
        return open("{}/example1.txt".format(self.inputfolder))

    def ex2(self):
        return open("{}/example2.txt".format(self.inputfolder))