import sqlite3
import config

conn = sqlite3.connect(config.path)
c = conn.cursor()

def CreateIMGTable():
    # Создаем таблицу картинок
    c.execute('''CREATE TABLE IF NOT EXISTS images (
                    img_id INTEGER PRIMARY KEY,
                    keyWord TEXT,
                    keyAns TEXT,
                    imgLink TEXT,
                    img2Link TEXT,
                    img3Link TEXT,
                    img4Link TEXT
                )''')

def CreateRequestsTable():
    # Создаем таблицу с внешним ключом
    c.execute('''CREATE TABLE IF NOT EXISTS requests
                 (req_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 gifNum INTEGER,
                 keyWord TEXT,
                 FOREIGN KEY (keyWord) REFERENCES images(keyWord))''')

def Fill_keyword_ids(data_set):
    for key, val in data_set.items():
        # Вставляем ключевое слово в таблицу keyword
        c.execute('INSERT INTO images (keyWord, keyAns) VALUES (?, ?)', (val, key,))
    conn.commit()

def inBase(num, keyword):
    c.execute("INSERT INTO requests (gifNum, keyWord) VALUES (?, ?)", (num, keyword,))
    conn.commit()

def lastRow():
    #ID последней добавленной строки
    last_row_id = c.lastrowid
    c.execute("SELECT gifNum, keyWord FROM requests WHERE req_id=?", (last_row_id,))
    # Получаем последнюю добавленную строку
    last_row = c.fetchone()
    print('Последний добавленный запрос:', last_row)

def getGifnum():
    # Получаем ID последней строки в таблице
    c.execute("SELECT MAX(req_id) FROM requests")
    last_row_id = c.fetchone()[0]
    # Выполняем запрос SELECT для получения значения столбца "gifNum" из последней строки
    c.execute("SELECT gifNum FROM requests WHERE req_id = ?", (last_row_id,))
    gifNum_value = c.fetchone()[0]
    # Выводим значение столбца "gifNum" в последней строке
    return int(gifNum_value)

def getKeyword():
    # Получаем ID последней строки в таблице
    c.execute("SELECT MAX(req_id) FROM requests")
    last_row_id = c.fetchone()[0]
    # Выполняем запрос SELECT для получения значения столбца "keyWord" из последней строки
    c.execute("SELECT keyWord FROM requests WHERE req_id = ?", (last_row_id,))
    gifNum_value = c.fetchone()[0]
    # Выводим значение столбца "keyWord" в последней строке
    return gifNum_value

def getLink():
    c.execute("SELECT MAX(req_id) FROM requests")
    last_row_id = c.fetchone()[0]
    c.execute("SELECT imgLink FROM images, requests "
              "WHERE requests.keyWord=images.keyWord AND req_id = ?", (last_row_id,))
    # Извлекаем результат запроса
    link_value = c.fetchone()
    if link_value is None:
        return 'Неизвестно'
    else:
        return link_value[0]

def allData():
    key = getKeyword()
    link = getLink()
    if link == 'Неизвестно':
        num = 10
    else:
        num = getGifnum()
    return num, key, link

def GlobalUpKeyWords(key, link1, link2, link3, link4):
    # Обновляем столбец imgLink в таблице images, если значение keyword_id совпадает с arg1
    c.execute('''UPDATE images
                     SET imgLink = ?,
                     img2Link = ?,
                     img3Link = ?,
                     img4Link = ?
                     WHERE keyword = ?''', (link1, link2, link3, link4, key))
    conn.commit()

def GlobalUpKeyAns(key, link1=None, link2=None, link3=None, link4=None):
    # Обновляем столбцы картинок в таблице images, если значение keyAns совпадает с arg1
    c.execute('''UPDATE images
                     SET imgLink = ?,
                     img2Link = ?,
                     img3Link = ?,
                     img4Link = ?
                     WHERE keyAns = ?''', (link1, link2, link3, link4, key))
    conn.commit()

def Cheka(n):
    c.execute(f'SELECT keyAns FROM images WHERE imgLink IS NOT NULL AND img_id = ?', (n,))
    row = c.fetchone()
    if row and row[0]:
        return True
    else:
        return False

def FullRename(n, num):
    i = num
    while (n <= 345):

        if (Cheka(n)):
            link1 = f'./img/img.{i}.jpg'
            link2 = f'./img/img.{i+1}.jpg'
            link3 = f'./img/img.{i+2}.jpg'
            link4 = f'./img/img.{i+3}.jpg'

            print(f"Картинки для этого вопроса будут иметь имена:\n"
                    f" 1) ./img/img.{i}.jpg \n"
                    f" 2) ./img/img.{i + 1}.jpg \n"
                    f" 3) ./img/img.{i + 2}.jpg \n"
                    f" 4) ./img/img.{i + 3}.jpg \n")

            c.execute('''UPDATE images
                                     SET imgLink = ?,
                                     img2Link = ?,
                                     img3Link = ?,
                                     img4Link = ?
                                     WHERE imgLink IS NOT NULL AND img_id = ?''', (link1, link2, link3, link4, n))
            conn.commit()
            i += 4
        n += 1

def WordRename(imId, link1, link2, link3, link4):
    c.execute('''UPDATE images
                         SET imgLink = ?,
                         img2Link = ?,
                         img3Link = ?,
                         img4Link = ?
                         WHERE img_id = ?''', (link1, link2, link3, link4, imId))
    conn.commit()

def CheckBaseData():
    c.execute('''SELECT *
    FROM images
    WHERE imgLink IS NOT NULL''')
    # Получаем результаты запроса
    results = c.fetchall()
    # Выводим строки с ненулевыми значениями столбца imgLink
    for row in results:
        print(row)
    conn.commit()

def CheckNum():
    imgnum = None
    c.execute('''SELECT CAST(substr(img4Link, 13, 2) AS INTEGER)
                          FROM images
                          WHERE img_id = (SELECT MAX(img_id) FROM images WHERE imgLink IS NOT NULL)''')
    result = c.fetchone()
    if result is not None:
        imgnum = result[0] + 1
    else:
        imgnum = 1
    conn.commit()
    return imgnum

def DelAllImg():
    c.execute('''UPDATE images
                         SET imgLink = NULL,
                         img2Link = NULL,
                         img3Link = NULL,
                         img4Link = NULL
                         ''')
    conn.commit()

def DelImg(keyword):
    c.execute('''UPDATE images
                         SET imgLink = NULL,
                         img2Link = NULL,
                         img3Link = NULL,
                         img4Link = NULL
                         WHERE keyAns = ? OR keyWord = ? OR img_id = ?''', (keyword, keyword, keyword))
    conn.commit()

def DelImgFrom(keyword):
    c.execute('''UPDATE images
                         SET imgLink = NULL,
                         img2Link = NULL,
                         img3Link = NULL,
                         img4Link = NULL
                         WHERE img_id >= ? OR img_id >= (SELECT img_id
                                                        FROM images
                                                        WHERE keyAns = ?)''', (keyword, keyword))
    conn.commit()