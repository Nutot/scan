import pytesseract
import os
from PIL import Image
import sort
from tqdm import trange
from tqdm import  tqdm
cfg = open("config.txt", "a+")

cfg.seek(0)


def check():
    OCR_path = str(input())

    if OCR_path[-13:] != "tesseract.exe" and os.path.isfile(OCR_path) == True:
        cfg.write(OCR_path)
    else:
        while OCR_path[-13:] != "tesseract.exe" and os.path.isfile(OCR_path) == False:
            print("Недействительный путь!")
            OCR_path = str(input())
        cfg.write((OCR_path))
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
    print('Введите путь до файла tesseract.exe')
    print('Обычно он C:\Program Files\Tesseract-OCR\... ')

    check()

    cfg.close()
else:
    cfg.seek(0)

    if cfg.read()[-13:] == 'tesseract.exe':
        cfg.close()
    else:
        open("config.txt", 'w')
        print('Файл config.txt поврежден.')
        print('Введите путь к файлу tesseract.exe')
        check()

s = []
f = 0
filtered_files=os.listdir('img')
g = os.listdir('img')
print(len(g))
print('Сортировать? ')
print('ДА/НЕТ')
ask = input()
if ask == 'ДА':
    sort.rand()
    sort.so()
    scan()

elif ask == 'НЕТ':
    scan()


tqdm.write('done')
print('Created by Nutot')
while s != '':
    s = input()