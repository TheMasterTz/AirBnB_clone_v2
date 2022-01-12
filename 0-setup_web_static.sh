#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "It is working" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
new_string="server_name _;\n\t\tlocation /hbnb_static/ {\n\t\t\talias /data/web_static/current/;\n\t\t}"
sudo sed -i "s|server_name\ _;|$new_string|" /etc/nginx/sites-available/default
sudo service nginx restart
