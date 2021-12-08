
# Пульт охраны банка

Это - внутренний репозиторий банка "Сияние", вы не сможете его запустить, если не обладаете нужными ключами доступа к базе данных, но код проекта может быть использован в учебных целях.

## Установка, зависимости и виртуальное окружение?

Вам понадобится установленный Python 3.6-3.9 и git.

Склонируйте репозиторий или скачайте код в виде архива:
```bash
$ git clone https://github.com/IlyaG96/django-opm-store.git
```

Создайте в этой папке виртуальное окружение:
```bash
$ python3 -m venv [полный путь до папки django-opm-store] env
```
### Необходимые пакеты
Активируйте виртуальное окружение и установите все необходимые пакеты:
```bash
$ cd django-opm-store
$ source env/bin/activate
$ pip install -r requirements.txt
```
Список необходимых пакетов (можно установить вручную, используя команду `pip install`)

```text
pytz==2017.2
django==1.11.*
psycopg2-binary==2.8.*
python-dotenv==0.19.2
```


## Переменные окружения
Заполните прилагающийся .env.example файл и переименуйте его в .env или иным образом задайте переменные среды:

```bash
SECRET_KEY=''
DEBUG=''
DATABASE_URL=''
```

```python
SECRET_KEY - секретный ключ для запуска сайте
DEBUG - режим отладки: True/False
DATABASE_URL='postgres://USER:PASSWORD@HOST:PORT/NAME'
```

### Как получить переменные окружения?
Для получения значений `USER`, `PASSWORD`, `HOST`, `PORT` и `NAME` обратитесь к руководству филиала Вашего банка
## Запуск
```bash
$ python manage.py runserver
```
Эта команда автоматически запустит сервер на вашем компьютере. Перейдите сюда [ http://127.0.0.1:8000/
](http://127.0.0.1:8000) для того, чтобы оценить результат

## Пример работы приложения

На сайте отображается список всех пользователей с активными картами доступа. Имена кликабельны.  

![Картинка](https://downloader.disk.yandex.ru/preview/5687a842727cb12cba2251f9c3088fc075df67eb46e90ad9a546b7b3e2b892b8/61aac461/NiqRg-YShT_Ms2sUe4_MNsxonG9V2PXx5clO5wFmd-PW03oWiHlQsuCK30fBgc_ivWK0geqTUvf_KWvGXiNzFw%3D%3D?uid=0&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-04%20%D0%B2%2008.18.48.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=512x512)  

Если нажать на имя, вы сможете увидеть список всех посещений пользователя.  

![Картинка](https://downloader.disk.yandex.ru/preview/6da04e0741a00c60d7eda1cc688ffb3f4c784fdad6d9d8ddda9f4ec441375826/61aac433/1v8GwBKydeESoZzRwgFJbTbpLDCMA4ugeEM7TZcP8f55n5DLkwyTxJ92TTPNzTNopdxQgNoT2gJUCAUgBTgefA%3D%3D?uid=0&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-04%20%D0%B2%2008.09.03.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=512x512)

Если визит длился дольше часа, то он считается подозрительным (True), а если менее часа - то не подозрительным (False).

Есть возможность узнать, кто в данный момент находится в хранилище  

![Картинка](https://downloader.disk.yandex.ru/preview/fcf2f1fec253d98c1249c8db4e9037ce43658fdc7b95cb434aedd1cdb6683983/61aac418/1LhluN7EQIyNZiyERQ8Y-lq6MLDJD8GchacC7YJ1fGn728OqJX_w2-e90Tv5QkHmGbT2W8dpswnk4BIT--9VaQ%3D%3D?uid=0&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-04%20%D0%B2%2008.08.07.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=512x512)  


## Примечания

Проект написан в учебных целях devman.org