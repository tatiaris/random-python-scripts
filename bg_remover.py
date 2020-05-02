from PIL import Image

img = Image.open('/Users/rishabhtatia/Desktop/misc/wps/personalWPs/line_loop/m2.png')
img = img.convert("RGBA")
copy = img

pixdata = img.load()
coordinate = 25, 25
r0 = copy.getpixel(coordinate)[0]
g0 = copy.getpixel(coordinate)[1]
b0 = copy.getpixel(coordinate)[2]

for x in range(img.width):
    for y in range(img.height):
        coordinate = x, y
        pixel_rgb = img.getpixel(coordinate)
        r = pixel_rgb[0]
        g = pixel_rgb[1]
        b = pixel_rgb[2]
        comp = 70
        # if abs(r0-r) < comp and abs(g0-g) < comp and abs(b0-b) < comp:
        #     for i in range(-1, 2):
        #         for j in range(-1, 2):
        #             if x+i > -1 and x+i < img.width and y+j > -1 and y+j < img.height:
        #                 # pixdata[x, y] = (255,255,255,0)
        #                 pixdata[x, y] = (15, 17, 26)
        if r == 23 and g == 24 and b == 28:
            pixdata[x, y] = (15, 17, 26)
        # elif abs(r - 23) < 20 and abs(g - 24) < 20 and abs(b - 28) < 20:
        #     pixdata[x, y] == (0,0,0)
img.show()
# img.save('/Users/rishabhtatia/Desktop/coding/py/projects/assets/wefwf.png')
img.save('/Users/rishabhtatia/Desktop/test.png')