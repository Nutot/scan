# scan
 Photo parser using tesseract
# Установка:
1. Скачать и установить Tesseract-OCR по ссылке https://github.com/UB-Mannheim/tesseract/wiki

![Снимок экрана 2024-04-17 195230](https://github.com/Nutot/scan/assets/39900113/43298c3e-e8a7-4e33-be5f-394f714ab90d)

2. Обязательно выбирете компонент установки Russian в Additional language data
![Снимок экрана 2024-04-17 195705](https://github.com/Nutot/scan/assets/39900113/1d8f177a-5313-42a4-b999-b7c3fe5d3488)
![Снимок экрана 2024-04-17 195545](https://github.com/Nutot/scan/assets/39900113/dec96821-bc9a-4d44-918b-30bd4f0e0a6b)
3. Запомните папку установки!!!    
![Снимок экрана 2024-04-17 200024](https://github.com/Nutot/scan/assets/39900113/84fd74d8-0955-405d-a6fc-d84b0c3f2ae1)
4. Скачайте приложение по инструкции
![Снимок экрана 2024-04-17 200721](https://github.com/Nutot/scan/assets/39900113/267f47cc-5459-4b26-89c6-7f05f0d9f823)
![Снимок экрана 2024-04-17 200814](https://github.com/Nutot/scan/assets/39900113/f5c47676-850a-4d46-b043-368eea80360a)
5. Создайте отдельную папку(название значения не имеет), скопируйте в нее приложение Scan.exe. Дополнительно создайте подпапку img. Она предназначена для фотографий.
 ![изображение](https://github.com/Nutot/scan/assets/39900113/d44268cb-a77b-4304-bc4a-5ffd751859ce)
![изображение](https://github.com/Nutot/scan/assets/39900113/31bd15ab-2858-44b6-8db8-371f93df5aa2)
6. После запуска программы Smart Screen может выдать предупреждениие. Обойдите его по инструкции!
![Без имени](https://github.com/Nutot/scan/assets/39900113/7f91a713-c1c7-40b5-81c5-7cd5bea92151)
![Без имени](https://github.com/Nutot/scan/assets/39900113/e51acecc-eef4-4a6c-8573-2e98f6c844cd)
7. В открывшееся окно консоли необходимо ввести путь до файла tesseract.exe, установленного на шагу номер 3. Обычно папка установки это: C:\Program Files\Tesseract-OCR\tesseract.exe (Это единоразовый процесс)
![изображение](https://github.com/Nutot/scan/assets/39900113/dfcecc95-e60e-4952-ac16-e383aa3112ff)
8. После ввода пути к файлу сортировщик выдаст количество найденых фотографий, и предложит отсортировать их. При первом запуске или при добовлении новых фотографий рекомендуется написать ДА.
9. Результат работы программы будет в текстовом файле test.txt в одной папке с приложением.
![изображение](https://github.com/Nutot/scan/assets/39900113/659fc353-9a70-4295-83f5-b99ec499c3ad)
![изображение](https://github.com/Nutot/scan/assets/39900113/500951df-bdab-4352-95fc-b2de4fd18121)

# FaQ
Почему не работает программа?
1. У вас установленна 32х битная версия Windows. Узнать разрядность вашей системы можно в панели управления в пункте СИСТЕМА![Снимок экрана 2024-04-17 215356](https://github.com/Nutot/scan/assets/39900113/ae136d3e-d373-4e07-8d61-1201fbb091cb)
![Снимок экрана 2024-04-17 215506](https://github.com/Nutot/scan/assets/39900113/4ba70b4a-845d-4de2-bb88-4d3fd126ce42)
2. Вы не установили Tesseract-OCR или не установили дополнительный русский язык. Обратитесь к пунктам 1-3.
3. Вы вывели неправильный путь установки Tesseract-OCR. Обратитесь к пунктам 3 и 7.
4. 
