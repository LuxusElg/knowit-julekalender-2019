
class SnailTimer:
	def __init__(self, list):
		self.list = self.load_list(list)
		self.grid = self.generateSquare(1000)

	def generateSquare(self, size):
		grid = [[0] * size for i in range(size)]
		return grid

	def run(self):
		#print(len(self.list))
		#print(self.list)
		#print(self.grid)

		snailpos = [0,0]
		elapsed = 0
		largest = 0
		# naive step by step
		for coords in self.list:
			# x move
			while snailpos[0] != int(coords[0]):
				if snailpos[0] < int(coords[0]):
					snailpos[0] += 1
				else:
					snailpos[0] -= 1
				#print(snailpos)
				#print(self.grid[snailpos[0]][snailpos[1]])
				elapsed += 1 + self.grid[snailpos[0]][snailpos[1]]
				self.grid[snailpos[0]][snailpos[1]] += 1
				if self.grid[snailpos[0]][snailpos[1]] > largest:
					largest = self.grid[snailpos[0]][snailpos[1]]

			while snailpos[1] != int(coords[1]):
				if snailpos[1] < int(coords[1]):
					snailpos[1] += 1
				else:
					snailpos[1] -= 1
				#print(snailpos)
				#print(self.grid[snailpos[0]][snailpos[1]])
				elapsed += 1 + self.grid[snailpos[0]][snailpos[1]]
				self.grid[snailpos[0]][snailpos[1]] += 1
				if self.grid[snailpos[0]][snailpos[1]] > largest:
					largest = self.grid[snailpos[0]][snailpos[1]]

			#print(self.grid)
		print(elapsed)
		print(largest)

	def load_list(self, list):
		lines = []
		with open(list) as list_file:
			raw = list_file.readlines()
			for line in raw:
				if line[0] == '#':
					continue
				line = line.rstrip().split(',')
				lines.append(line)
		return lines

if __name__ == '__main__':
	snailtimer = SnailTimer("coords.csv")
	snailtimer.run()