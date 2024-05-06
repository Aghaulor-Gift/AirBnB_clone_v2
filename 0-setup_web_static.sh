#!/usr/bin/env bash
# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get install -y nginx
fi

sudo service nginx start
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html><head></head><body> Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
config_file="/etc/nginx/sites-available/default"
sudo sed -i "/^\s*server_name\s/ a \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" "$config_file"
sudo service nginx restart
