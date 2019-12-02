# Just for fun :)
class Dragon:
    def __init__(self):
        self.size = 50
        self.anger = 0

    def eat(self, herd):
        herd -= self.size
        self.size += -1 if herd < 0 else 1
        self.anger = self.anger + 1 if herd < 0 else 0
        return herd if herd > 0 else 0

    def isEnraged(self):
        return self.anger >= 5

class Town:
    def __init__(self, path):
        self.growth = self.load(path)
        self.herd = 0

    def load(self, path):
        with open(path) as list_file:
            growth_list = list_file.readlines()[0].split(', ')
        return growth_list
    
    def breed(self, day):
        if day >= len(self.growth):
            return False
        self.herd += int(self.growth[day])
        return True

if __name__ == '__main__':
    town = Town('sau.txt')
    dragon = Dragon()
    day = 0

    while(town.breed(day)):
        town.herd = dragon.eat(town.herd)
        if (dragon.isEnraged()):
            break
        day += 1
    print day
