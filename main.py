import check
import sort
import tess
check.ch()
print('created by Nutot. @Nutot on tg')
print('Сортировать скриншоты?')
print('Д/Н')

while True:
    a = input()
    if a == 'Д' or a == 'Y' or a == 'YES'or a == 'Yes' or a == 'Да':
        sort.rand()
        sort.so()
        tess.ts()
        print('Готово!')
        break
    elif a == 'Н' or a == 'N' or a == 'No' or a == 'Нет':
        tess.ts()
        print('Готово!')
        break