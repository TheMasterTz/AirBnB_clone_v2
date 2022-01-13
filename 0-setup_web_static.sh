#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create folders
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create fake html
echo "
<html>
<head>
</head>
<body>
	Holberton School
</body>
</html>" | sudo tee -a /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Create owner and permissions
sudo chown -hR ubuntu:ubuntu /data/

# Update nginx configuration content
new_conf="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "47i $new_conf" /etc/nginx/sites-available/default

sudo service nginx reload
sudo service nginx start
