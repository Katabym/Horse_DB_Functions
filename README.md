# Функционал настройки Базы данных для "Голосового помощника коня"

## Для выставки ВДНХ "Россия" 4 ноября был разработан голосовой помощник "Тидон"

В данном репозитории находится функционал для создания и настройки базы данных.

#### Язык: `Python, SQL`.

#### СУБД: `SQLite`.

#### Используемая библиотека: `sqlite3`.

#### В файле `config.py` требуется указать путь для создания базы данных.

#### В файлах `words.py` и `words1.py` находятся словари диалогов коня и списки нецензурных слов.

#### В файле `AllAdminComand.py` находятся примеры функций

`-создания таблиц`

`-обновления таблиц`

`-удаления данных в таблицах`

`-просмотра таблиц` 

с описанием того что они выполняют

#### Пример:

```shell
   Создание таблицы images
CreateIMGTable()

   Создание таблицы запросов
CreateRequestsTable()

   Удаляет все картинки
DelAllImg()

   Удалить по вопросу/ответу/ID
anser = input("Введите вопрос\ответ либо ID вопроса: ")
DelImg(anser)
```

### В файле `AllUsersComand.py` находятся примеры функций

`-создания новой записи`

`-вызова данных`

`-просмотра данных` 

с описанием того что они выполняют.

### Пример:

```shell
   Вставка данных в таблицу
   inBase(аргумент с номером анимации, аргумент с ключем)
inBase(3, 'представься')

   Выводит все записи базы данных с непустыми картинками
CheckBaseData()
```

### Файл `In&Del.py` это готовый скрипт для обновления записей по картинкам и их удаления.

### Файл `Deleter.py` это готовый скрипт для удаления картинок у записей в базе.

### В файле `funcsql.py` находятся ВСЕ функции.