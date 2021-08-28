# Clean Architecture Example

A simple example of clean architecture.

## RUN SERVER

```
python manage.py runserver
```

## SWAGGER

```
http://localhost:8000/swagger/
```

## SEED

```
python manage.py migrate
python manage.py shell < seeds/seed_company.py
```

## TEST

```
python manage.py test
```