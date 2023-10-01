# MyChat

## Description 
A Group video calling application using the Agora Web SDK with a Django backend.

##  How to use this source code

#### 1 - Clone repo
```
git clone https://github.com/pythonmentor/mychat-example
```

#### 2 - Install requirements
```
cd mychat
pipenv install --dev
```

#### 3 - Create .env with Agora credentals
Create an account at agora.io and create an `app`. Once you create your app, you will want to rename the .env-example file to .env and fill in the values for AGORA_APP_ID and AGORA_APP_CERTIFICATE. 


#### 4 - Start server
```
python manage.py runserver
```


