# study_mq_python

* Python: 3.8

```
# set virtual environment
$ python3 -m venv .venv

# install requirements
(.venv) $ pip install -r requirements.txt

# migrate
(.venv) $ python manage.py migrate

# start server as DEBUG mode

# run docker-compose for the worker and broker in the root directory of the project
## for mac
$ docker-compose -f local.yml build && docker-compose -f local.yml up

## for windows
$ docker-compose -f local.yaml -f local.yaml up
```
