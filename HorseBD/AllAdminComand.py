from funcscl import CreateIMGTable, CreateRequestsTable, Fill_keyword_ids
from funcscl import Cheka, FullRename, CheckBaseData
from funcscl import GlobalUpKeyWords, GlobalUpKeyAns, WordRename
from funcscl import DelAllImg, DelImg, DelImgFrom
#from words1 import data_set
#from words import data_set


#================================================================================================
#   Первичное создание базы данных

#   Создание таблицы images
#CreateIMGTable()

#   Создание таблицы запросов
#CreateRequestsTable()

#   Вызываем функцию для заполнения столбцов keyword, keyAns
#Fill_keyword_ids(data_set)

#================================================================================================

#================================================================================================
#   Функции проверки данных в базе

#   Cheka возвращает:
#   True - Если img_id совпадает с ID И есть картинки
#   False - Если img_id НЕ совпадает с ID И есть картинки
# --------------------------------------
#   FullRename обновляет имена картинок по введенному ID = img_id
#   от NUM до последней записи подходящей под условие:
#   NUM = 5
#   img42, img43, img44, img45 -> img5, img6, img7, img8
#   ...
#   img86, img87, img88, img89 -> img9, img10, img11, img12
#   ...
#   end
# --------------------------------------
#Cheka(ID)
#FullRename(ID, NUM)

#   Выводит все записи базы данных с непустыми картинками
#CheckBaseData()

#================================================================================================

#================================================================================================
#   Функции обновления данных в базе

#   Обновляем картинки в строке по ответу (keyWord)
#i=1
#for values in data_set.values():
#    GlobalUpKeyWords(values, f'D\images\img{i}.jpg',
 #              f'D\images\img{i+1}.jpg',
 #              f'D\images\img{i+2}.jpg',
 #              f'D\images\img{i+3}.jpg',)
 #   i += 4

#   Обновляем картинки в строке по вопросу (keyAns)
#i=1
#for key in data_set.values():
#    GlobalUpKeyAns(key, f'D\images\img{i}.jpg',
 #              f'D\images\img{i+1}.jpg',
 #              f'D\images\img{i+2}.jpg',
 #              f'D\images\img{i+3}.jpg',)
 #   i += 4

#   Обновляем картинки в строке по ID записи (img_id)
#i=1
#for key in data_set.values():
#    WordRename(217, f'D\images\img{i}.jpg',
 #              f'D\images\img{i+1}.jpg',
 #              f'D\images\img{i+2}.jpg',
 #              f'D\images\img{i+3}.jpg',)
 #   i += 4

#================================================================================================

#================================================================================================
#   Функции удаления данных в базе

#   Удаляет все картинки
#DelAllImg()

#   Удалить по вопросу/ответу/ID
#anser = input("Введите вопрос\ответ либо ID вопроса: ")
#DelImg(anser)

#   Удалить все записи после номера
#anser = input("Введите вопрос или ID: ")
#DelImgFrom(anser)

#================================================================================================