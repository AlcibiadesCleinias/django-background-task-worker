# django-background-task-worker
Want to merely run a simple thread worker in a Django background? I will show you, but:

this repo is not about "ready-to-use" package, it is only about how to natively run tasks in background Django thread.

## Pros & Cons
### Cons
- The [Celery](https://docs.celeryproject.org/en/stable/) wheel already exists
- This threaded job behavior initiates jobs in `app_ready()` method of a Django app. So, you can not silence the job for example for testing because `app_ready()` is executed on each start of a Django project (e.g. with help of `./manage.py runserver`)
- By adding your special job timetable with your additional code you can not be sure that your job runs only one according to your timetable. To be sure you should use a flag, e.g. database flag which you ought to select and update with atomic request, because you each booted thread of your Django app executes `app_ready()`, so several thread jobs go to work.
- ...

### Pros
- you can start a simple Django thread worker that executes your task each interval, logs heart-beat, has access to Django ORM

## Real World Example
Python Api on a Windows Server:
- python coz its 'built in' Ml instruments
- Django coz it is easy to implement rest api
- Windows Server coz feature you work with runs only on WS (e.g. PI Server) and coz you can not procreate several services for a task :(

## Script
- check `src/utils/job.py` for general ABC job worker class
- check `src/app_with_background_thread_worker/jobs` for simple implementation of the ABC class in the Django app
- check `src/app_with_background_thread_worker/test` for example of faking the simple worker class

## Start
You can create a venv and so, and so... I prefer the Docker way:
1. Create an image
```
docker build -t django-background-worker .
```
2. Start a container
```
docker run --rm --name test-django-background-worker -v $(pwd)/src:/opt -t django-background-worker 
```

## Сompetitor
- [django-background-tasks](https://github.com/arteria/django-background-tasks/blob/master/docs/index.rst) Django package that uses your database to register task and etc.
- [RQ](https://github.com/rq/rq) package that uses Redis
- [django-workers](https://github.com/geekforbrains/django-workers) Django package that adds posibility to run separate manage.py command for worker process, tasks synchronizing via django db

## Discussion
- I hope on discussions: do not hesitate to open issues relate to the behaviour and suggest the wheel improvements (or merely this readme file).
- https://stackoverflow.com/questions/17601698/can-you-perform-multi-threaded-tasks-within-django
- ...

## Acknowledgment
- [@nlevashov](https://github.com/nlevashov)

