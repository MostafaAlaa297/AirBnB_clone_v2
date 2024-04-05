#!/usr/bin/env bash
# Install Nginx
sudo apt update
sudo apt install -y nginx

# Create dir if not exists
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/test

cat << EOF > /data/web_static/releases/test/index.html
<!DOCTYPE html>
<html>
<head>
</head>
<body>
	Hello school
</body>
</html>
EOF

# Create symbolic link
ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership of data dir to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
echo 'server {
	listen 80 default_server;
	listen [::]:80;
	
	location /data/web_static/current/ {
		alias hbnb_static;

	}
}' > /etc/nginx/sites-available/default

# Add custom HTTP response header to Nginx configuration
sudo service nginx restart
