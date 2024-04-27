import pytesseract
import os
from tqdm import trange
from PIL import Image


def ts():
    file = open("config.txt", 'r')
    path = file.read()
    file1 = open("votes.txt", "w+")
    filtered_files = os.listdir('img')
    pytesseract.pytesseract.tesseract_cmd = path
    for c in trange(1, len(filtered_files)):
        file_path = str(c)
        image = Image.open(f'{"img"}/{file_path}' + '.jpg')
        a = pytesseract.image_to_string(image, lang="rus")
        b = a.find("Всего проголосовало")
        d = (a[b + 21:b + 26])
        u = (a[b + 21:b + 25])

        if d.isdigit() == True:
            file1.write(d + '\n')


        elif u.isdigit() == True:
            file1.write(u + '\n')

