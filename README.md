Пульт охраны банка

Это - внутренний репозиторий банка "Сияние", вы не сможете его запустить, если не обладаете нужными ключами доступа к базе данных, но код проекта может быть использован в учебных целях.

Как установать?

Вам понадобится установленный Python 3.6-3.9 и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/IlyaG96/django-opm-store.git
```

Создайте в этой папке виртуальное окружение:
```bash
$ python3 -m venv [полный путь до папки django-opm-store] env
```

Активируйте виртуальное окружение и установите все необходимые пакеты:
```bash
$ cd django-opm-store
$ source env/bin/activate
$ pip install -r requirements.txt
```
## Использование
Заполните прилагающийся .env.example файл и переименуйте его в .env или иным образом задайте переменные среды:

```bash
ENGINE_DB=''
HOST_DB=''
PORT_DB=''
NAME_DB=''
USER_DB=''
PASSWORD_DB=''
SECRET_KEY=''
DEBUG=''
```
Переменная `LANGUAGES` содержит список языков, для которых будет найдена средняя зарплата. Запятые ставить не надо. Только пробелы

Простейший способ начать поиск средней зарплаты -
```bash
$ python main.py
```
Программа получит данные по вакансиям с сайтов [hh.ru](hh.ru) и [superjob.ru](superjob.ru) и представит их в виде таблицы:

![](https://downloader.disk.yandex.ru/preview/9d7cb2350e69a64ce5b5bd38653befebab22977d3497486ccdd7d42b41dffa0a/61a70313/aiK_p35wptpfeBleZFkIbcGTbmx8tm2WQyXkxReSpPUATwBE7osJB0J4Akycf2TJJHynJtbni52cRJjF8j4nzA%3D%3D?uid=0&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-01%20%D0%B2%2012.03.22.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=512x512)

### headhunter.py
Содержит логику для работы с API headhunter

### superjob.py
Содержит логику для работы с API superjob
