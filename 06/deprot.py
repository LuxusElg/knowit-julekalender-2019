from PIL import Image

class Deprotector:
    def __init__(self, path):
        self.originalImage = Image.open(path)

    def xorImage(self):
        img = self.originalImage
        pixels = list(img.getdata())
        img.putdata(self.processPixels(pixels))
        img.save('out2.png')

    def processPixels(self, pixels):
        xored = pixels
        for i in range(1, len(xored)):
            if i < len(xored):
                xored[-i] = tuple(self.xorPixel(xored[-i], xored[-i-1]))
        return xored

    def xorPixel(self, p1, p2):
        return [p1[0]^p2[0],p1[1]^p2[1],p1[2]^p2[2]]


if __name__ == '__main__':
    deprotector = Deprotector("mush.png")
    deprotector.xorImage()