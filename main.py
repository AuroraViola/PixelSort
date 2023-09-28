import images
import random
import colorsys
import os

def partition(list, maxlen, seed):
    random.seed(seed)

    list_copy = list.copy()
    lists = []
    while len(list_copy) > maxlen:
        rnum = random.randint(1, maxlen)
        lists.append(list_copy[:rnum])
        list_copy = list_copy[rnum:]
    lists.append(list_copy)

    return lists

def rgbtohsv(rgbtuple):
    (h, s, v) = colorsys.rgb_to_hsv(rgbtuple[0], rgbtuple[1], rgbtuple[2])
    return (h, s, v)

def pixelsort(input, output, pxlenght, seed):
    img = images.load(input)
    img2 = []

    for row in img:
        sortedrow = []

        splited_row = partition(row, pxlenght, seed)

        for parts in splited_row:
            sortedrow.extend(sorted(parts, key=lambda x: (rgbtohsv(x)[0], rgbtohsv(x)[1], rgbtohsv(x)[2])))
        img2.append(sortedrow)

        seed += 1

    images.save(img2, output)

if __name__ == '__main__':
    seed = random.randint(0,10000)
    pxlenght = 50
    files = os.listdir("input")

    if not os.path.exists("temp"):
        os.mkdir("temp")
    if not os.path.exists("output"):
        os.mkdir("output")

    for i in range(len(files)):
        pixelsort(("input/" + files[i]), ("output/" + files[i]), pxlenght, seed)
        print("(" + str(i+1) + "/" + str(len(files)) + ") image saved in output/" + files[i])
