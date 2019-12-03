from PIL import Image
import math

class Drawer:
    def __init__(self, list):
        self.list = self.load_list(list)[0]

    def makeImage(self):
        print(len(self.list))
        #root = int(math.sqrt(len(self.list)))
        #print(root)
        #728 * 990
        #770 * 936
        #780 * 924
        #792 * 910
        #819 * 880
        #840 * 858
        #1001 * 720
        #1008 * 715
        #1040 * 693
        #1092 * 660
        #1144 * 630
        #1155 * 624
        #1170 * 616
        #1232 * 585
        #1260 * 572
        #1287 * 560
        #1320 * 546
        #1365 * 528
        #1386 * 520
        #1430 * 504
        #1456 * 495
        #1540 * 468
        #1560 * 462
        #1584 * 455
        #1638 * 440
        #1680 * 429
        #1716 * 420
        #1820 * 396
        #1848 * 390
        #1872 * 385
        #1980 * 364
        #2002 * 360
        #2145 * 336
        #2184 * 330
        #2288 * 315
        #2310 * 312
        xlen = 1287
        ylen = int(len(self.list) / xlen)
        print(xlen, ylen)
        image = Image.new('1', (xlen,ylen), 1)

        chunks, chunk_size = len(self.list), xlen
        lines = [ self.list[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        #print(lines)
        
        for y, line in enumerate(lines):
            for x, value in enumerate(line):
                #print(x,y,value)
                image.putpixel((x,y), int(value))

        image.save('img.bmp')

    def load_list(self, list):
        with open(list) as list_file:
            lines = list_file.readlines()
        return lines

if __name__ == '__main__':
    drawer = Drawer("img.txt")
    drawer.makeImage()