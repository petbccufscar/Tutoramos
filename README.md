
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
## Requirements.txt

Manter as dependências é importante!!

Para salvar:
```bash
pip freeze > requirements.txt
```

Para instalar a partir do arquivo:
```bash
pip install -r requirements.txt
```

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

## Model Fields
[Referência](https://docs.djangoproject.com/en/4.0/ref/models/fields/)
- IntegerField
- BooleanField
- CharField
- DateField
- DateTimeField
- DurationField
- EmailField

## Relações
```py
models.TIPODERELACAO( MODELOASSOCIADO, on_delete=E_SE_DELETAR, related_name=FUNCAO_INVERSA)
```

### Tipos de campos de relações
[Documentação](https://docs.djangoproject.com/en/4.0/topics/db/examples/)
- ForeignKey - Usado para 1 - N
- OneToOneField - Usado para 1 - 1
- ManyToManyField - Usado para M - N

### Tipos de deleções principais
[Referência](https://ilovedjango.com/django/models-and-databases/foreign-keys-on_delete-option-in-django-models/)

- CASCADE
- PROTECT
- RESTRICT
- SET_NULL
- SET_DEFAULT

### Relação inversa
```py
a.reunioes_do_perfil.all()
```

## Modelando as entidades
Exemplo:
```py
class Reuniao(models.Model):
    # Campos
    nome = models.CharField(blank=False, null=False, max_length=255)
    descricao = models.CharField(blank=False, null=False, max_length=400)
    dataHora = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Relações
    participantes = models.ManyToManyField(Perfil,related_name="reunioes_do_perfil") 
    POT = models.ForeignKey(POT, models.CASCADE, related_name="reunioes_do_pot")
```
## Serializadores
[Documentação](https://www.django-rest-framework.org/api-guide/serializers/)

"Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data."

## Model Serializer (CRUD pronto)
Exemplo: 
```py
class ReuniaoSerializer(ModelSerializer):
    class Meta:
        model = Reuniao
        fields = '__all__'
```

## SerializerMethodField
[Documentação](https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield)

## Criando os serializers
Crie arquivos serializers.py nos apps.
Faça seus serializers, para esse tutorial ModelSerializer é suficiente.
Para mais informações, consulte a documentação.

### Serializers compostos

É possivel inserir um serializer como campo de outro.
Exemplo:
```py
user: User = UserSerializer(write_only=True)
```

### to_representation
[Documentação](https://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields)
Você customiza o que quer ver pelo Serializer!!


## @transaction.atomic

Lembram que em algum momento a gente ficou preocupado com as
condições de corrida que podiam acontecer ao fazer alguma
leitura do banco de dados, manipular esse dado e escrever novamente
no banco? Aparentemente os bancos de dados tem operadores
pra garantir que isso não aconteça. São chamados "transactions".
Basicamente, vc coloca um "begin-transaction" antes de começar
a fazer leituras e escritas no banco de dados e "commita" as
alterações quando todas as operações forem feitas. Se alguma falhar,
todas são desfeitas. Esse comando garante também a atomicidade,
não tem a chance de vc ler uma propriedade A e outra pessoa escrever
em cima desse propriedade antes de você terminar sua operação (se vc
tiver usado o begin-transaction").


## Rotas
- CRUD Reunião
- CRUD POT
- CRUD Perfil+Usuário
- Login
- Refresh

## APIView


