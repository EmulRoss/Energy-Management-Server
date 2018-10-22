# Energy-Management-Server
Energy monitoring, analysis and visualization
> This repository works in conjunction with [Energy-Management-Website](https://github.com/EmulRoss/Energy-Management-Website)
> A Vue.js project

## Required technologies

The pip package manager is required to install the Flask framework.

Flask and Flask-CORS are included via the pip package manager.

- Flask
  - found [here](http://flask.pocoo.org/)
- Flask-CORS
  - found [here](https://flask-cors.readthedocs.io/en/latest/)

## Build Setup

For a development environment, run the following commands:

1. export the application
   - export FLASK_APP=Server.py

2. export the development environment
   - export FLASK_ENV=development

3. run the flask application
   - flask run

Once the development environment is running the flask application is at localhost:5000

By going to localhost:5000/ in a browser, the message "Server Test" should appear.

Proceed to [Energy-Management-Website](https://github.com/EmulRoss/Energy-Management-Website) and follow the steps to display the website.