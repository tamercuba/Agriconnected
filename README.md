# Agriconnected Aliens
> Catalogando todas aparições alienígenas do Brasil.

Parágrafo apresentando o projeto

GIF DO FRONT-END

## Instalação
Esse guia funciona apenas para sistemas operacionais com kernel Linux, se você quiser executá-lo
em outro sistema operacional e compartilhar a experiência aqui fiquei a vontade.

Primeiro você precisa baixar os arquivos para o seu computador, para isso execute o seguinte comando
no diretório desejado
> git clone https://github.com/tamercuba/Agriconnected.git

Caso não tenha em sua maquina, instale o virtualenv (lembrando que estamos utilizando a versão 3.7 do Python, então
    talvez você precise executar `pip3` ao inves de `pip`)
> pip install virtualenv

Crie seu ambiente virtual na pasta que desejar (recomendamos que utilize uma pasta `.venv` dentro da pasta do projeto)
> virtualenv -p /diretorio/do/python3.7/na/sua/maquina ENV_NAME

Após isso navegue até a pasta do projeto (onde está o arquivo `requirements.txt`) e execute
>pip install -r requirements.txt

Instale o PostgreSQL na sua maquina, crie um banco de dados com o nome que desejar e no arquivo `settings.py` faça
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'NOME_DO_SEU_DB',
        'USER': 'USUARIO_QUE_O_DJANGO_IRA_UTILIZAR',
        'PASSWORD': 'SUA_SENHA',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}`

Execute os seguintes comandos para migrar o banco de dados
>./manage.py makemigrations
./manage.py migrate

Agora você precisará criar um super user para fazer o cadastro dos estados e ter acesso ao sistema
>./manage.py createsuperuser

Pronto, você ja pode rodar o site na sua maquina, faça
>./manage.py runserver --insecure

Para acessar o site basta digitar `localhost:8000` no seu navegador.

## Sobre o Autor
