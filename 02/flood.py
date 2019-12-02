class Solver:
    def __init__(self, list):
        self.list = self.load_list(list)

    def solve(self):
        flooded = 0
        for line in self.list:
            first_mtn = -1
            last_mtn = -1
            mtn_count = 0
            for pos, val in enumerate(line):
                if first_mtn == -1 and val == '#':
                    first_mtn = pos
                if val == '#':
                    last_mtn = pos
                    mtn_count += 1
            if first_mtn != last_mtn:
                flooded += (last_mtn - first_mtn - (mtn_count-1))
        return flooded

    def load_list(self, list):
        with open(list) as list_file:
            lines = list_file.readlines()
        return lines

if __name__ == '__main__':
    solver = Solver("world.txt")
    print solver.solve()
