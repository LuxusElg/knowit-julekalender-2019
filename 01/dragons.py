class Solver:
    def __init__(self, list):
        self.numberlist = self.load_numbers(list)
        self.dragon_size = 50
        self.days_gone = 0
        self.berserk = 0
        self.herd = 0

    def solve(self):
        for sheepcount in self.numberlist:
            self.herd += (int(sheepcount) - self.dragon_size)
            if self.herd < 0:
                self.herd = 0
                self.berserk += 1
                self.dragon_size -= 1
            else:
                self.berserk = 0
                self.dragon_size += 1
            if self.berserk == 5:
                break
            else:
                self.days_gone += 1

    def load_numbers(self, list):
        with open(list) as list_file:
            numberlist = list_file.readlines()[0].split(', ')
        return numberlist

if __name__ == '__main__':
    solver = Solver("sau.txt")
    solver.solve()
    print solver.days_gone
