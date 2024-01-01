from funcscl import CheckBaseData, DelAllImg, DelImg, DelImgFrom

checkDel = 1
while checkDel > 0:
    print("Все строки с картинками: ")
    CheckBaseData()
    checkDel = int(input("\nУдалить все картинки - 1 \n"
                         "Удалить по вопросу/ответу/ID - 2 \n"
                         "Удалить все записи после - 3 \n"
                         "Выход - 0 \n"
                         "Ввод: "))
    if checkDel == 1:
        DelAllImg()
    if checkDel == 2:
        anser = input("Введите вопрос\ответ либо ID вопроса: ")
        DelImg(anser)
    if checkDel == 3:
        anser = input("Введите вопрос или ID: ")
        DelImgFrom(anser)