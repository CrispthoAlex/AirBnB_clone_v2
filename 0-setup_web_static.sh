#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static. It:

# Install Nginx if it not already installed
# Create the folder below, if it doesnt already exist:
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
# Give ownership of the /data/ folder to the ubuntu user AND group. This should be recursive; everything inside should be created/owned by this user/group.
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static).
# Restart Nginx after updating the configuration

# Script to set ups web server
echo -e "\n##### INSTALL NGINX #####\n"
sudo apt-get update
sudo apt-get -y install nginx
# Enable port 80
sudo ufw allow 'Nginx HTTP'

DIR1=data # /data
DIR2=web_static # /data/web_static/
DIR3=releases # /data/web_static/releases/
DIR3_1=test # /data/web_static/releases/test/
# DIR4=shared # /data/web_static/shared/

echo -e "\n##### CREATE FOLDERS ######\n"
# Create folders (-v to print it does it)
sudo mkdir -vp /$DIR1/$DIR2/{$DIR3/$DIR3_1,shared}

echo -e "\n##### CREATE FAKE HTML #####\n"
# fake HTML
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /$DIR1/$DIR2/$DIR3/$DIR3_1/index.html

echo -e "\n##### SYMBOLIC LINK ######\n"
# Symbolic link "current"
sudo ln -sfv /$DIR1/$DIR2/$DIR3/$DIR3_1/ /$DIR1/$DIR2/current

echo -e "\n##### OWNERSHIP #####\n"
# Give ownership to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /$DIR1/

echo -e "\n##### Update Nginx Configuration #####\n"
# Update Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Apply changes to nginx#
sudo service nginx restart
