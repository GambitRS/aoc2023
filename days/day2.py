from days import day


class Day2(day.Day):

    def __init__(self):
        super(Day2, self).__init__(2)

    def start1(self):
        reds = 12
        greens = 13
        blues = 14

        file = self.inputfile()
        total = 0
        while True:
            line = file.readline()

            if not line:
                break

            parts = line.split(":")
            games = parts[1].split(";")
            ok = True

            for i in range(0, len(games)):
                game = games[i]
                colors = game.split(",")

                for j in range(0, len(colors)):
                    balls = (colors[j].strip().split(' '))
                    amount = int(balls[0])
                    color = balls[1]
                    if (color == "red") & (amount > reds):
                        ok = False
                        break
                    if (color == "blue") & (amount > blues):
                        ok = False
                        break
                    if (color == "green") & (amount > greens):
                        ok = False
                        break

                if not ok:
                    break

            if ok:
                nr = int(parts[0].split(" ")[1])
                total += nr



        #file = self.inputfile()
        self.answer(1,total)

    def start2(self):

        file = self.inputfile()
        total = 0
        while True:
            reds = 0
            greens = 0
            blues = 0

            line = file.readline()

            if not line:
                break

            parts = line.split(":")
            games = parts[1].split(";")

            for i in range(0, len(games)):
                game = games[i]
                colors = game.split(",")

                for j in range(0, len(colors)):
                    balls = (colors[j].strip().split(' '))
                    amount = int(balls[0])
                    color = balls[1]
                    if (color == "red") & (amount > reds):
                        reds = amount
                    elif (color == "blue") & (amount > blues):
                        blues = amount
                    elif (color == "green") & (amount > greens):
                        greens = amount

            total += reds * greens * blues


        # file = self.inputfile()
        self.answer(2, total)
