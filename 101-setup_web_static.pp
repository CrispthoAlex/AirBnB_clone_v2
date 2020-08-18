# Bash script that sets up your web servers for the deployment of
# web_static using Puppet

exec { '/usr/bin/env apt-get -y update':}
exec { '/usr/bin/env apt-get -y install nginx':}
exec { '/usr/bin/env mkdir -p /data/web_static/releases/test/':}
exec { '/usr/bin/env mkdir -p /data/web_static/shared/':}
exec { '/usr/bin/env echo "Hello Holberton School. No more Tiwetter" > /data/web_static/releases/test/index.html':}
exec { '/usr/bin/env ln -sfv /data/web_static/releases/test/ /data/web_static/current':}
exec { '/usr/bin/env sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n}" \
     /etc/nginx/sites-available/default':}
exec { '/usr/bin/env chown -hR ubuntu:ubuntu /data/':}
exec { '/usr/bin/env service nginx restart':}
