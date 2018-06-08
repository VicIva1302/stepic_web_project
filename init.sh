sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello
#sudo ln -sf /home/box/web/etc/gunicorn_dj.conf /etc/gunicorn.d/test_dj
#sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:wsgi_application
#sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ hello:app &
gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application &