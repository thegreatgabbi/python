# GDipSA Python
Python section for GDipSA Enrichment Week.
`05_05` and `05_06` are Python snippets from http://172.27.242.189/ (NUS VPN required)

## Django
### Installation
```
$ cd python/django/mysite

# to migrate models over to MySQL database
$ python3 manage.py makemigrations
$ python3 manage.py makemigrations inventory
$ python3 manage.py migrate

# Add a superuser account for administration authentication
$ python3 manage.py createsuperuser

# Start the server
$ python3 manage.py runserver
```
The server will automatically refresh when there are changes to any project files.
