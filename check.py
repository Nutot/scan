import os

def ch():
    cfg = open("config.txt", 'a+')
    cfg.seek(0)
    OCR_path = cfg.read()
    print(OCR_path)
    if os.stat("config.txt").st_size == 0:
        print('Введите путь до файла tesseract.exe')
        print('Обычно он C:\Program Files\Tesseract-OCR\... ')
        OCR_path = str(input())
        if OCR_path[-13:] == "tesseract.exe":
            cfg.write(OCR_path)
            print('ok')
        else:
            while OCR_path[-13:] != "tesseract.exe":
                print('Ошибка!')
                OCR_path = str(input())
            cfg.write(OCR_path)
    else:

        if OCR_path[-13:] == "tesseract.exe":
            print('ok')
        else:
            while OCR_path[-13:] != "tesseract.exe":
                print('Путь поврежден!')
                cfg.truncate(0)
                OCR_path = str(input())
            cfg.write(OCR_path)

