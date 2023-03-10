# backenderp : [backenderp.com](https://backenderp.com)

# Backend generic for ERP or Ecommerce
This is a project in development, is not ready for production.

# How install
```
git clone https://github.com/falconsoft3d/backenderp.git
cd backenderp
git checkout dev
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
python manage.py runserver --settings app.settings.dev
```

# How use
```
http://localhost:8000
```

# Django
```
python manage.py startapp myapp apps/<myapp>
python manage.py startapp <www>
python manage.py makemigrations
python manage.py migrate
```

# Update the libraries requirements
```
pip freeze > requirements.txt
```

# How install with docker local
```
docker run -d -p 8000:8000 mfalconsoft/caprover-django
```

# How update if you have docker local
```
docker build -t mfalconsoft/backenderp .
docker push mfalconsoft/backenderp
docker images
docker run -d -p 8000:8000 mfalconsoft/caprover-django
```

# My contact data
```
Marlon Falcón Hernández | Valencia | Spain
* ERP, CRM y Software: https://www.marlonfalcon.com
» Email: mfalconsoft@gmail.com
» Github: https://github.com/falconsoft3d
» linkedin: https://linkedin.com/in/marlon-falcón-3a2aa9a4
```