#!/usr/bin/env bash
# Install Nginx
sudo apt update
sudo apt install -y nginx

# Create dir if not exists
data='data'
if [[ ! -e $data ]];then
	mkdir $data

elif [[ -d $data ]];then
	echo "$data already exists but is not a directory" 1>&2
fi

static='/data/web_static/'
if [[ ! -e $static ]];then
        mkdir "$static"


elif [[ -d $static ]];then
        echo "$static already exists but is not a directory" 1>&2
fi

releases='/data/web_static/releases/'
if [[ ! -e $releases ]];then
        mkdir $releases


elif [[ -d $releases ]];then
        echo "$releases already exists but is not a directory" 1>&2
fi

shared='/data/web_static/shared/'
if [[ ! -e $shared ]];then
        mkdir $shared


elif [[ -d $shared ]];then
        echo "$shared already exists but is not a directory" 1>&2
fi

test_dir='/data/web_static/shared/test/'
if [[ ! -e $test_dir ]];then
        mkdir $test_dir


elif [[ -d $test_dir ]];then
        echo "$test_dir already exists but is not a directory" 1>&2
fi

cat << EOF > "$test_dir/index.html"
<!DOCTYPE html>
<html>
<head>
</head>
<body>
	Hello school
</body>
</html>
EOF

current='/data/web_static/current'
if [[ -L $current ]];then
	rm  $current
fi
ln -s $test_dir $current

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
