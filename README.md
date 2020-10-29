# A simple webapp using Flask and Vue

App based on https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

# Server

## Project setup

```
cd server
pip3 install -r requirements.txt
```

## Run the server

In debug:

```
python app.py
```

## Gunicorn

GUnicorn is  the Web Server Gateway Interface (WSGI).

Installation:
```
sudo pip3 install gunicorn
```

To start gunicorn:
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

To start as a service:
```
cp flask-wsgi.service /etc/systemd/system/
sudo systemctl start flask-wsgi
sudo systemctl enable flask-wsgi
```

Check the status
```
sudo systemctl status flask-wsgi
```

## Nginx

Nginx is the Web Server.

To install it:
```
sudo apt install nginx
```

Copy the config files
```
cp flask-backend-nginx /etc/nginx/sites-available/
cp vue-frontend-nginx /etc/nginx/sites-available/

# create simLinks
ln -s /etc/nginx/sites-available/flask-backend-nginx /etc/nginx/sites-enabled
ln -s /etc/nginx/sites-available/vue-frontend-nginx /etc/nginx/sites-enabled
```
Restart nginx
```
sudo systemctl restart nginx
```

# Client

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
