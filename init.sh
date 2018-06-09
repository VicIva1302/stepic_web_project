#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello
#sudo ln -sf /home/box/web/etc/gunicorn_dj.conf /etc/gunicorn.d/test_dj
#sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:wsgi_application
#sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
#gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/hello &
#gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask &
#sudo rm -r /etc/gunicorn.d/*
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello
#sudo ln -sf /home/box/web/etc/gunicorn_dj.conf /etc/gunicorn.d/gunicorn_dj.conf
#sudo /etc/init.d/gunicorn restart
#sudo gunicorn -b 0.0.0.0:8000 wsgi &
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
#sudo gunicorn -b 0.0.0.0:8080 --workers=2 hello:app
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql restart
#source web/myvenv/bin/activate
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ hello:app &
gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application &