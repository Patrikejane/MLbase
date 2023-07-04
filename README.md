# MLbase
Simple Api for upload Sound Files to the ML model

project structure


### project Stucture

    .
    ├── mlbasetsx-app      # client app
    ├── soundFiles         # Folder where files will be uploaded
    ├── templates          # flask templates (only Hello api)
    ├── venv               # virtual environment Py
    ├── main.py            # main Py
    ├── Router.py          # routes api Py
    ├── requirements.txt   # python packages
    └── README.md          # project Read me


### Server 

run 

> source venv/bin/activate

> pip install -r requirements.txt

> flask --app main run


* will Run on http://127.0.0.1:5000

* http://127.0.0.1:5000/upload
 ---> fill upload end point


### Client

> cd mlbasetsx-app

In the Client project directory, you can run:

### `npm install`

to install available packages

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.


[http://localhost:3000/Home](http://localhost:3000/Home]) is the Mlbase Client Home page
