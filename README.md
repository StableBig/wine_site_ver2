# Новое русское вино

**Новое русское вино** — это сайт винного магазина и веб-приложение для отображения информации о винах и других напитках в продаже, основанное на простом HTTP-сервере.

Приложение позволяет пользователям загрузить свой файл Excel (формата `.xlsx`) с информацией о винах и напитках и просмотреть его содержимое на веб-странице.

## Как это работает?

Вы создаете свой файл `.xlsx` с данными о винах и напитках в виде таблицы (категория, цена и так далее), а скрипт загружает эти данные и формирует веб-страницу магазина с ними.

## Используемые технологии

* **Python** для серверной части и обработки данных.
* **Pandas** для чтения и обработки данных из файлов `.xlsx`.
* **Jinja2** для шаблонизации и генерации HTML-страницы на основе данных.
* Встроенный **HTTP-сервер** для отображения данных на веб-странице.

## Предварительные требования

Прежде чем начать, убедитесь, что у вас установлено следующее:

* **[Python 3.7](https://www.python.org/downloads/)** или выше.
* **pip** - установщик пакетов Python.
* **Virtualenv** - инструмент для создания изолированных сред Python.
* **Git** - система контроля версий.

## Установка и запуск

1. Скачайте [репозиторий](https://github.com/StableBig/wine_site_ver2) или клонируйте его, выполнив команды:

```bash
git clone https://github.com/StableBig/wine_site_ver2.git
cd wine_site_ver2
```

_**Примечание:** Команда  `cd` (change directory) используется в Unix/Linux системах. Если вы используете Windows, вы можете использовать эту же команду в PowerShell или использовать команду `chdir` в командной строке (cmd)._

2. Создайте новое виртуальное окружение и активируйте его:

```bash
python3 -m venv venv
source venv/bin/activate  # для Unix систем
.\venv\Scripts\activate  # для Windows
```

3. Установите необходимые зависимости.

Убедитесь, что у вас установлены **Python** и **pip**. Затем установите необходимые библиотеки:

```bash
pip install -r requirements.txt
```

_**Примечание:** Если вы используете `pip3` вместо `pip`, замените `pip` на `pip3` в команде выше._

4. Вам нужно предварительно настроить некоторые переменные окружения.

Создайте файл `.env`.

Укажите значения переменных `FOUNDING_YEAR` (год основания винодельни) и `WINE_TABLE_PATH` (путь к вашему файлу с таблицей в формате `.xlsx`).

Например, если год основания винодельни - `1920`, а файл называется `wine.xlsx` и он находится в корневой директории проекта, ваш файл `.env` будет выглядеть так:

```
FOUNDING_YEAR=1920
WINE_TABLE_PATH=wine.xlsx
```

* Если значение переменной `FOUNDING_YEAR` не указано в файле `.env`, то значение по умолчанию - `1920`.

* Если значение переменной `WINE_TABLE_PATH` не указано в файле `.env`, то значение по умолчанию - `wine.xlsx`.

* Переменная `FOUNDING_YEAR` необходима для правильного подсчета возраста винодельни.

5. Структура таблицы файла `.xlsx`.

Таблица должна иметь следующие названия колонок: `Категория`, `Название`, `Сорт`, `Цена`, `Картинка`, `Акция`.

Пример таблицы:

| Категория    | Название      | Сорт      | Цена | Картинка       | Акция      |
|--------------|---------------|-----------|------|----------------|------------|
| Белые вина   | Ркацители     | Ркацители | 499  | rkaciteli.png  | Акция      |
| Красные вина | Черный лекарь | Качич     | 399  | chernyi_lekar.png  |         |

* Если ваше вино или напиток участвует в акции "Выгодное предложение", заполните колонку `Акция` напротив нужного нужного вам (не имеет значения, что там будет написано, главное заполнить это поле). На изображениях этих вин и напитков появится плашка "Выгодное предложение". Например, если вино "Белая леди" и "Чача" участвуют в акции, то ваша таблица будет выглядеть так:

| Категория  | Название   | Сорт            | Цена | Картинка        | Акция               |
|------------|------------|-----------------|------|-----------------|---------------------|
| Белые вина | Белая леди | Дамский пальчик | 399  | belaya_ledi.png | Скидка              |
| Напитки    | Чача       |                 | 299  | сhacha.png      | Выгодно |

* Изображения товаров поместите в директорию `images`, и в колонке `Картинка` укажите название файлов напротив вин и напитков, к которым они относятся.

6. Запуск веб-сервера.

Будет запущен веб-сервер и загружен файл `.xlsx`. По умолчанию это файл `wine.xlsx`, который находится в корневой директории проекта. Если вы указали путь к нему в файле `.env`, то будет загружаться он.

Для запуска выполните команду:

```bash
python3 main.py
```

Если вы хотите использовать другой файл, можете указать путь к нему прямо во время выполнения команды:

```bash
python3 main.py --file путь_к_вашему_файлу/название_вашего_файла.xlsx
```

Перейдите в вашем браузере по адресу: http://127.0.0.1:8000. Вы должны увидеть сайт с вашим списком вин и напитков.

## Для разработчиков

Основные файлы проекта:

* `main.py`: Главный скрипт приложения. Запускает сервер, читает данные из файла `.xlsx`, генерирует веб-страницу на основе шаблона `template.html`.

* `template.html`: HTML-шаблон для генерации веб-страницы.

## Цели проекта

Код написан в учебных целях.
