# The demo web app
### Features
 - Create entry with name, email, phone [for all users]
 - Register an account
 - Login with an account
 - View created entries [only for authenticated users]
 - logout
 - view admin dashboard [only for superusers, staff users]
### Technology stack
 - server side rendering of web page built with html and bootstrap
 - backend logic written in django framework of python
 - packeged with docker
 - sqlite database used

### Installation
step 1 : clone github repository

    $ git clone https://github.com/shojibMahabub/kludio-assignments.git

step 2 : create a virtualenv

    $ virtualenv -p python3 env
    $ source ./env/bin/activate

step 3 : install packages

    $ pip install -r requirements.txt

step 3 : migrate database

    $ python manage.py makemigrations accounts
    $ python manage.py migrate

step 4 :  run django server

    $python manage.py runserver

### Architecture
The requirement was simple enough to go with server side rendering.
If any client side technology was required then it would be great to have an api.

It is a simple monolith software with a central database. It is fast because of server side rendering. It is secured because of strong backend framework.

If I want to convert it to micro service I would like to separate user and auth service with their own DB and wrap them with an api. There is no need but other services like massage queue, load balancer, api gateway etc can be integrated with this
