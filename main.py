import pytesseract
import os
from PIL import Image
import sort
from tqdm import trange
from tqdm import  tqdm
cfg = open("config.txt", "a+")
cfg.seek(0)

def scan():


    file = open("test.txt", "w+")
    for c in trange(1,len(filtered_files)):
        file_path = str(c)
        image = Image.open(f'{"img"}/{file_path}' + '.jpg')
        pytesseract.pytesseract.tesseract_cmd = OCR_path
        a = pytesseract.image_to_string(image, lang="rus")

        b = a.find("Всего проголосовало")
        d = (a[b + 21:b + 26])
        u = (a[b + 21:b + 25])

        if d.isdigit() == True:
            file.write(d + '\n')


        elif u.isdigit() == True:
            file.write(u + '\n')




if os.stat("config.txt").st_size ==0 :
    print('Введите путь до файла tesseract.exe.')
    print('Обычно он C:\Program Files\Tesseract-OCR\ ')
    OCR_path=str(input())
    cfg.write(OCR_path)
    cfg.close()
else:
    cfg.seek(0)
    OCR_path = cfg.read()
    cfg.close()
    print(OCR_path)
s = []
f = 0
filtered_files=os.listdir('img')
g = os.listdir('img')
print(len(g))
print('Сортировать? ')
print('Y/n')
ask = input()
if ask == 'Y':
    sort.rand()
    sort.so()
    scan()

elif ask == 'n':
    scan()


tqdm.write('done')
print('Created by Nutot')
while s != '':
    s = input()

