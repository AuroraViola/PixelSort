from PIL import Image
import png

def load(fname):
    temp = Image.open(fname)
    temp.convert("RGB")
    temp.save("temp/temp.png")
    with open("temp/temp.png", mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l += [(line[i], line[i+1], line[i+2])]
            img += [l]
        return img

def save(img, filename):
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)