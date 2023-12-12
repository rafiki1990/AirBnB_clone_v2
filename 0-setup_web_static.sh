#!/usr/bin/env bash
# sets up web servers for the deployment of web_static.

# Update package list
sudo apt update -y

# Install Nginx
sudo apt install nginx -y

# Allow Nginx through the firewall
sudo ufw allow 'Nginx HTTP'

# Create directory structure for web deployment
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a sample index.html file
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link to the latest release
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data directory
sudo chown -R ubuntu:ubuntu /data

# Configure Nginx to serve the static content
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply changes
sudo service nginx restart
