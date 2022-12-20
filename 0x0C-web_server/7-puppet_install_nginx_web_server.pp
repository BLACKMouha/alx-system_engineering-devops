# Configuration of Nginx web server
exec {'/usr/bin/env apt-get -y update':}

exec {'/usr/bin/env apt-get -y install nginx':}

exec {'/usr/bin/env echo "Hello Wordl!" > var/www/html/index.nginx-debian.html':}

exec {'/usr/bin/env sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.holbertonschool.com permanent;" /etc/nginx/sites-available/default':}

exec {'/usr/bin/env sed -i "/server_name _;/ a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-available/default':}

exec {'/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html':}

exec {'/usr/sbin/env nginx -t':}

exec {'/usr/bin/env service nginx restart':}
