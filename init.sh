sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello
sudo ln -sf /home/box/web/etc/gunicorn_dj.conf /etc/gunicorn.d/test_dj
sudo /etc/init.d/gunicorn restart