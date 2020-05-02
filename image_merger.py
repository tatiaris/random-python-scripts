from PIL import Image

img = Image.open('assets/apple.jpg').convert('RGBA')
img2 = Image.open('assets/line.jpg').convert('RGBA')

pixdata = img.load()
pixdata2 = img2.load()

for x in range(img.width):
    for y in range(img.height):
        coordinate = x, y
        pixel_rgb = img.getpixel(coordinate)
        pixel_rgb2 = img2.getpixel(coordinate)
        r = pixel_rgb[0]
        g = pixel_rgb[1]
        b = pixel_rgb[2]
        r2 = pixel_rgb2[0]
        g2 = pixel_rgb2[1]
        b2 = pixel_rgb2[2]
        ravg = int((r+r2)/2)
        gavg = int((g+g2)/2)
        bavg = int((b+b2)/2)
        pixdata[x, y] = (ravg,gavg,bavg)
img.show()
