
## Obtendo o código do tatuzao
git clone https://github.com/relicariotech/tatuzao.git

`cd tatuzao`

Abra o seu editor favorito. Nós recomendamos o utilizar Visual Studio Code.

## Conteiners services
No seu terminal, execute o comando abaixo para processar o docker-compose localmente:

`docker-compose -f docker-compose.yml up --build`


Dois conteineres serão `up and running`. Esses são os conteineres descritos no `docker-compose.yml`.
- web
- db

## Outros Commands - nativos do Django

Após configurar os conteiners, execute os comandos abaixo para criar as tabelas nativas do Django e criar o usuário `superuser`:

`docker-compose -f docker-compose.yml exec web python manage.py makemigrations` 

`docker-compose -f docker-compose.yml exec web python manage.py migrate`

`docker-compose -f docker-compose.yml exec web python manage.py createsuperuser`

Nesse ponto, a aplicação `tatuzao` estará com o seu usuário superuser.

##  Executando os comando a partir do container

Uma melhor abordagem é acessar diretamente o conteiner, e a partir dele, executar os comandos do Django.

Liste todos os conteineres em operação.
```
docker ps
````

Copie o Id do container `tatuzao-web`.

Execute o comando abaixo para acessar o conteiner.
```
docker exec -it <container-id> /bin/bash
````

Agora você está dentro do `bash` do conteiner, podendo executar os comando dessa forma:

`python manage.py makemigrations` 

`python manage.py migrate`

`python manage.py createsuperuser`

## Acessando o admin do Django
Realize o login através do /admin.