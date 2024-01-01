#from words1 import data_set
from words import data_set
from funcscl import GlobalUpKeyAns, CheckNum, CheckBaseData
from funcscl import DelAllImg, DelImg, DelImgFrom


#===========================================================
#   Часть добавления новых картинок к записям

#   Функция которая возвращает номер последней добавленной в базу картинки
#   Из записи D\images\img15.jpg
#   i = 15
#   Баг:  Из числа 153
#   i = 15
i = CheckNum()

lastimg = 0
for key, value in data_set.items():

    print(f"На вопрос: \"{key}\" \n"
          f"C ответом: \"{value}\" \n"
          f"Нужны картинки?")
    print("Да - 1")
    print("Нет - 0")
    print("Выход - 5")
    check = int(input("Ответ: "))
    if check == 5:
        break
    if check == 1:

        GlobalUpKeyAns(key, f'D\images\img{i}.jpg',
                       f'D\images\img{i+1}.jpg',
                       f'D\images\img{i+2}.jpg',
                       f'D\images\img{i+3}.jpg',)

        print(f"Картинки для этого вопроса будут иметь имена:\n"
              f" 1) D\images\img{i}.jpg \n"
              f" 2) D\images\img{i+1}.jpg \n"
              f" 3) D\images\img{i+2}.jpg \n"
              f" 4) D\images\img{i+3}.jpg \n")
        i += 4
        lastimg = i-1
    else: print("Картинок нет \n")
if lastimg == 0:
    print("Новых картинок не добавлено")

print("Всего картинок добавлено: ", lastimg)


#===========================================================
#   Часть удаления не нужных записей

checkDel = 1
while checkDel > 0:
    print("Все строки с картинками: ")
    #   Выводит все записи базы данных с непустыми картинками
    CheckBaseData()
    checkDel = int(input("\nУдалить все картинки - 1 \n"
                         "Удалить по вопросу/ответу/ID - 2 \n"
                         "Удалить все записи после - 3 \n"
                         "Выход - 0 \n"
                         "Ввод: "))
    if checkDel == 1:
        #   Удаляет все картинки
        DelAllImg()
    if checkDel == 2:
        anser = input("Введите вопрос\ответ либо ID вопроса: ")
        #   Удалить по вопросу/ответу/ID
        DelImg(anser)
    if checkDel == 3:
        anser = input("Введите вопрос или ID: ")
        #   Удалить все записи после номера
        DelImgFrom(anser)