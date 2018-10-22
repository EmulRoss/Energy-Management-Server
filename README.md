# Energy-Management-Server
Energy monitoring, analysis and visualization
> This repository works in conjunction with [Energy-Management-Website](https://github.com/EmulRoss/Energy-Management-Website)

## Required technologies

The pip package manager is required to install the Flask framework.

Flask and Flask-CORS are included via the pip package manager.

- [Flask](http://flask.pocoo.org/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

## Build Setup

For a development environment, run the following commands:

```bash
# export the application
export FLASK_APP=Server.py

# export the development environment
export FLASK_ENV=development

# run the flask application at localhost:5000
flask run
```

By going to 'localhost:5000/' in a browser, the message "Server Test" should appear.

Proceed to [Energy-Management-Website](https://github.com/EmulRoss/Energy-Management-Website) and follow the steps to display the website.
