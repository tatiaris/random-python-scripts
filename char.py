from PIL import Image

img = Image.open('assets/paper.png')
img.show()
img = img.convert("RGBA")

def convert_bw(img):
    pixdata = img.load()
    for x in range(img.width):
        for y in range(img.height):
            coordinate = x, y
            pixel_rgb = img.getpixel(coordinate)
            r = pixel_rgb[0]
            g = pixel_rgb[1]
            b = pixel_rgb[2]
            avg = int((r+g+b)/3)
            if avg > 170:
                pixdata[x, y] = (255,255,255,0)
            else:
                pixdata[x, y] = (0, 0, 0)
def remove_singles(img):
    w, h = img.height, img.width;
    neighbors = [[0 for x in range(w)] for y in range(h)] 
convert_bw(img)
img.show()
