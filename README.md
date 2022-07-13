
## Instalação e criação do virtualenv
```bash
pip install virtualenv
virtualenv .venv
```
## Ativando o ambiente virtual
### Windows
```bash
source .venv/Scripts/activate
```
### Linux
```bash
source .venv/bin/activate
```
## Instalando o django rest
[Documentação](https://www.django-rest-framework.org)
```bash
pip install django djangorestframework
```

## Criando o Projeto
```bash
django-admin startproject tutoramos .
```

## Instalando o Simple JWT

[Documentação](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
```
pip install djangorestframework-simplejwt
```

## Adicionando os Pacotes instalados
Em settings.py adicione os apps:

```py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
]
```
Também se faz necessário adicionar o seguinte código no settings.py:
```

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}

```
## Criando Apps
Vamos criar nossos próprios apps!!
```bash
django-admin startapp Perfil
django-admin startapp POT
django-admin startapp Reuniao

```
Lembre-se de adicioná-los nos INSTALLED_APPS.

```py
INSTALLED_APPS = [
    ...
    'Perfil',
    'POT',
    'Reuniao'
]
```


## Modelando as entidades

## Adicionando no painel de adm
[Documentação](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
Para aparecer no painel de adm basta registrar o modelo no arquivo admin.py
Exemplo:
```py
from .models import Reuniao
admin.site.register(Reuniao)
```

## Migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

## Criando super usuário
```bash
python manage.py createsuperuser 
```

## Rodando o servidor
```
python manage.py runserver
```

## Relações
