# stepic_web_project
Создание проекта в рамках курса на stepic.org

1.Разверните репозиторий со своим проектом в директориию /home/box/web

2. Создайте WSGI приложение в файле /home/box/web/hello.py

WSGI приложение должно возвращать документ с MIME-типом text/plain, содержащий все GET параметры, по одному на каждую строку.

Например при запросе  /?a=1&a=2&b=3 приложение должно вернуть такой текст

a=1
a=2
b=3
3. Настройте Gunicorn таким образом, что бы он запускал приложение  /home/box/web/hello.py , и принимал соединения на IP адресе 0.0.0.0 на порту 8080 .  (Использования IP = 0.0.0.0 необходимо для тестирования). Конфиг разместить в файле /home/box/etc/hello.py и подключите его с помощью символической ссылки /etc/gunicorn.d/hello.py

4. Настройте nginx так что бы location /hello/ проксировался на cервер Guincorn

Таким образом, WSGI приложение должно быть доступно по URL

http://127.0.0.1/hello/
http://127.0.0.1:8080/

5. Не забудьте закомитить и сохранить на github полученную структуру директорий и конфиги.
==================================================
###### Задание 2.3 Работа с СУБД
```git clone https://github.com/...  #--последние изменения в ветке home, переходим туда и фетчим
sudo pip install pymysql # Нужно для работы MySQL
sudo pip install --upgrade django #  ﻿﻿Апргейдим Джангу до последней версии.
sudo /etc/init.d/mysql start
--Создаем пользователя и базу, выдаем права
mysql -uroot -e "CREATE USER 'admin'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('pass111')"
mysql -uroot -e "CREATE DATABASE mybase"
mysql -uroot -e "GRANT ALL ON mybase.* TO 'admin'@'localhost'"
-- Создаем таблицы для моделей
python manage.py makemigrations qa
python manage.py migrate
--запускаем приложение для проверки:
./init.sh
