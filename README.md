This app is same in functionality as ERMS_Django_Web. But this app uses
multiple databases. I created this app because the django documentation on
using multiple databases is not clear. In addition to django's default
database, it uses 'admindb' to store admin credentials, and 'empdb' to store
employee data. Go through the 'settings.py' for details about db configuration.
This app uses 'dbrouter' to direct the db actions to appropriate databases. It
is possible to not use 'dbrouter' and explicitly specify database for db
actions. See the django docmentation for that. 

As usual, the project requirements are given in 'ERMS.pdf'. Before running the
app, initialise and migrate the databases with the following commands:

    ./manage.py makemigrations app_django
    ./manage.py migrate --database=default
    ./manage.py migrate --database=admindata
    ./manage.py migrate --database=empdata
    ./manage.py migrate

'admindata' and 'empdata' are the names used in 'settings.py'

Run the app with:

    ./manage.py runserver
