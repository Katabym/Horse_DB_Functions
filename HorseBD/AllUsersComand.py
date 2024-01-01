from funcscl import inBase, lastRow, allData
from funcscl import getGifnum, getKeyword, getLink
from funcscl import CheckBaseData, CheckNum

#   Вставка данных в таблицу
#   inBase(аргумент с номером анимации, аргумент с ключем)
#inBase(3, 'представься')


#   Выводит данные таблицы запросов текстом
#lastRow()


#   Кидает все данные из базы в переменную
#data = allData()
#print(f'Номер анимации = {data[0]}')
#print(f'Ключ = {data[1]}')
#print(f'Ссылка на картинку = {data[2]}')


#   Возвращает номер анимации в переменную
#num = getGifnum()
#print('num =', num)


#   Возвращает ключ в переменную
#word = getKeyword()
#print('word =', word)


#   Возвращает ссылку на картинку в переменную
#img_link = getLink()
#print('img_link =', img_link)


#   Функция которая возвращает номер последней добавленной в базу картинки
#   Из записи D\images\img15.jpg
#   i = 15
#   Баг:  Из числа 153
#   i = 15
#i = CheckNum()


#   Выводит все записи базы данных с непустыми картинками
#CheckBaseData()