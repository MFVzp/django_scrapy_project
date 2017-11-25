# django_scrapy_project


### install redis-server

    ~/$ sudo apt-get install redis-server

### install requirements

    ~/$ pip install -r requirements.txt

### in new console run spider

    ~/django_scrapy_project/parser_project/scrapy_project$ scrapy crawl mytheresa

### in new console run celery

    ~/django_scrapy_project/parser_project$ celery -A parser_project worker -l info

### in new console run django

    ~/django_scrapy_project/parser_project$ python3 manage.py runserver
