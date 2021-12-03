#Пульт охраны банка

Это - внутренний репозиторий банка "Сияние", вы не сможете его запустить, если не обладаете нужными ключами доступа к базе данных, но код проекта может быть использован в учебных целях.

##Как установать?

Вам понадобится установленный Python 3.6-3.9 и git.

Склонируйте репозиторий или скачайте код в виде архива:
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

```python
SECRET_KEY - секретный ключ для запуска сайте
DEBUG - режим отладки: True/False
```
Для получения всех остальных параметров переменной окружения обратитесь, пожалуйста, к руководству Вашего филиала

Простейший способ запустить сервер
```bash
$ python manage.py runserver
```
Эта команда автоматически запустит сервер на вашем компьютере. Перейдите сюда [ http://127.0.0.1:8000/
](http://127.0.0.1:8000) для того, чтобы оценить результат

## Возможности

На сайте отображается список всех пользователей с активными картами доступа. Имена кликабельны.
![Картинка](https://3.downloader.disk.yandex.ru/preview/307461a8a48bd47386a40807d96cbbc3da22f802e4d6a7fc747ef9dd80b1cdea/inf/NiqRg-YShT_Ms2sUe4_MNsxonG9V2PXx5clO5wFmd-PW03oWiHlQsuCK30fBgc_ivWK0geqTUvf_KWvGXiNzFw%3D%3D?uid=917569359&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-04%20%D0%B2%2008.18.48.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=917569359&tknv=v2&size=616x592)  

Если нажать на имя, вы сможете увидеть список всех посещений пользователя.
![Картинка](https://1.downloader.disk.yandex.ru/preview/21ebacf05301fbf7866eafe6b08aa3a748d1a1c631c268067b95f78228f83437/inf/1v8GwBKydeESoZzRwgFJbTbpLDCMA4ugeEM7TZcP8f55n5DLkwyTxJ92TTPNzTNopdxQgNoT2gJUCAUgBTgefA%3D%3D?uid=917569359&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-04%20%D0%B2%2008.09.03.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=917569359&tknv=v2&size=616x592)

Если визит длился дольше часа, то он считается подозрительным (True), а если менее часа - то не подозрительным (False).

Есть возможность узнать, кто в данный момент находится в хранилище
![Картинка](https://2.downloader.disk.yandex.ru/preview/204606f017a8e9049162cb67f9458709224a3a408779111cca5adb16d711c3d7/inf/1LhluN7EQIyNZiyERQ8Y-lq6MLDJD8GchacC7YJ1fGn728OqJX_w2-e90Tv5QkHmGbT2W8dpswnk4BIT--9VaQ%3D%3D?uid=917569359&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-04%20%D0%B2%2008.08.07.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=917569359&tknv=v2&size=615x592)