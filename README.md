
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
    #participantes = models.ManyToManyField(Perfil,related_name="reunioes_do_perfil") 
    #POT = models.ForeignKey(POT, models.CASCADE, related_name="reunioes_do_pot")
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

## PrimaryKeyRelatedField
[Documentação](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)

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
[Documentação](https://www.django-rest-framework.org/api-guide/views/)
Exemplo: 
```py
class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

### Generic views
[Documentação](https://www.django-rest-framework.org/api-guide/generic-views/)

- CreateAPIView
- RetrieveAPIView
- UpdateAPIView
- DestroyAPIView
- ListAPIView


## Como testar as rotas???
- DJANGO DEBUG
- [Insomnia](https://insomnia.rest/download) Free
- [Postman](https://www.postman.com/) Pago
- [...](https://www.google.com/search?channel=fs&client=ubuntu&q=postman+alternatives)

## CRUD POT, REUNIÃO, PERFIL

Os Cruds, em sua maioria serão feitos desse modo:
Considerando um modelo NOME:
```py
class ListCreateNOME(generics.ListCreateAPIView):
    queryset = NOME.objects.all()
    permission_classes = []
    serializer_class = NOMESerializer

class RetrieveUpdateDeleteNOME(generics.RetrieveUpdateDestroyAPIView):
    queryset = NOME.objects.all()
    permission_classes = []
    serializer_class = NOMESerializer
```
Esse é um CRUD bem simples que se aproveita dos generics para funcionar.
Sempre é possível fazer modificações.
Necessário dizer que é preciso linkar essas views no urls:
```py
path('NOME/', ListCreateNOME.as_view()),
path('NOME/<pk>/', RetrieveUpdateDeleteNOME.as_view()),
# <pk> é um kwarg que é necessário em views que são relativas a um unico objeto.
# ele vai representar a chave primária desse objeto.
# se acessar NOME/1/, você estará fazendo a operação no objeto nome de chave primária 1.
```

Em relação ao CRUD do Perfil + User é um pouco mais complicado,
pois, como eles são integrados, temos os seguintes serializers:

```py
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField()
    name = serializers.CharField()

    def create(self, validated_data):
        user = User()

        user.username = validated_data['username']
        user.email = validated_data['email']
        user.first_name = validated_data['first_name']
        validated_data.pop('name')
        user.set_password(validated_data['password'])

        return user

    def update(self, user: User, validated_data):
        l = ['username', 'email', 'first_name']
        for i in l:
            if i in validated_data:
                setattr(user, i, validated_data[i])

        if 'name' in validated_data:
            validated_data.pop('name')

        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        
        return user

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'username']


class PerfilSerializer(serializers.ModelSerializer):

    user: User = UserSerializer(write_only=True)
    
    class Meta:
        model = Perfil
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.create_user(
            first_name=user_data['name'],
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )

        return Perfil.objects.create(**validated_data, user=user)


    @transaction.atomic
    def update(self, instance, validated_data):
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            d = {}

            if 'name' in user_data:
                d['first_name'] = user_data['name']

            l = ['email', 'password', 'username']
            for i in l:
                if i in user_data:
                    d[i] = user_data[i]
            
            serializer = UserSerializer()
            user = serializer.update(user = instance.user,validated_data=d)
            user.save()
            instance.user = user
        return super().update(instance,validated_data=validated_data)

    


    def to_representation(self, instance: Perfil):
        representation = {'id': instance.user.id,
                          'username': instance.user.username,
                          'email': instance.user.email,
                          'nome': instance.user.get_full_name()
                          }

        # Adiciona os dados da própria instância.
        representation.update(super().to_representation(instance))
        return representation
```

Note que há uma preocupação se os parâmetros foram passados no update, pois o verbo PATCH passa apenas os que serão atualizados.
Também é importante notar o uso do ".save()", você pode recuperar um objeto e modificar, mas para a aplicação refletir no banco de dados é necessário fazer o save.


## Autenticação
- Rotas de login 

Adicione o seguinte no urls
```py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]

```

[É possivel modificar as configurações do simple jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html)

[É possível modificar as rotas de login e refresh também!](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html)


### Permissões
[Com as Permissões podemos controlar o acesso as views!!](https://www.django-rest-framework.org/api-guide/permissions/#allowany)

As principais são:
- AllowAny
- IsAuthenticated 
- IsAdminUser

Para ativa-las basta usar o campo permission_classes das views, as passando na lista.

exemplo:

```py
class ListCreateReuniao(generics.ListCreateAPIView):
    queryset = Reuniao.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReuniaoSerializer
```

Além de permitir o acesso, também podemos pegar o objeto do usuário logado nas views.

exemplo:

```py
class ListCreateReuniao(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReuniaoSerializer

    def get_queryset(self):
        qs = Reuniao.objects.all()
        return qs.filter(POT=self.request.user.perfil.POT)
```


Limitando o queryset pelo método:
```py
class RetrieveUpdatePerfil(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PerfilSerializer

    def get_queryset(self):
        qs = Perfil.objects.all()
        if self.request.method == 'GET':
            return qs
        return qs.filter(id=self.request.user.perfil.id)
```