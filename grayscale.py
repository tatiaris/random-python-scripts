from PIL import Image

img = Image.open(input('enter img path: ')[:-1])
img = img.convert("RGBA")

pixdata = img.load()

for x in range(img.width):
    for y in range(img.height):
        coordinate = x, y
        pixel_rgb = img.getpixel(coordinate)
        r = pixel_rgb[0]
        g = pixel_rgb[1]
        b = pixel_rgb[2]
        a = pixel_rgb[3]
        avg = int((r+g+b)/3)
        # if not (r == 0):
            # pixdata[x, y] = (avg,avg,avg)
        # pixdata[x, y] = (b, g, r, a)
        # if (r + g + b)/3 > 200:
        #     pixdata[x, y] = (20, 20, 20)
        # else:
        #     pixdata[x, y] = (0, 240, 240)
        if (avg < 200 and a > 100):
            pixdata[x, y] = (0, 255, 0)

img.show()
img.save('g_pawn.png')
