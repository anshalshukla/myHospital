# myHospital

To start the project on localserver make sure you have virtualenv installed in your system, if not then run the following command.

```
pip3 install virtualenv
```

Now make a Virtual Environment using it, install dependencies and run server

```
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
