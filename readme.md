
## Obtaining the riacho's codebase
git clone https://github.com/relicariotech/riacho.git

`cd riacho`

Open on your Editor. We recommend using Visual Studio Code.

## Conteiners services
On your terminal, execute the command to run the docker-compose locally:

`docker-compose -f docker-compose-local.yml up --build`


Two conteiners will be up and running. These conteiners are descibed on docker-compose.yml.
- web
- db

## Other Commands

After setting up the conteiners, execute the following commands:

`docker-compose -f docker-compose-local.yml exec web python manage.py makemigrations` 

`docker-compose -f docker-compose-local.yml exec web python manage.py migrate`

`docker-compose -f docker-compose-local.yml exec web python manage.py createsuperuser`

At this point, riacho application will be running and with your superuser.

## Creating basic elements
Login on /admin interface based on your environment.


### Dev environment
api.riacho-dev.relicario.tech/admin


### Homolog environmnet
api.riacho-homolog.relicario.tech/admin


### Production environmnet
api.riacho.relicario.tech/admin


Create a Cliente. It will generate the client id = 1 that we'll use on fixture loaddata.

Create a Dispositivo for this Cliente. It will generate the dispositivo id = 1 that we'll use on fixture loaddata.

## Seeding a set of Leituras

On your terminal, execute the command:

`docker-compose -f docker-compose-local.yml exec web python manage.py loaddata leitura.yaml`

It'll create 13 Leituras for the underlying Dispositivo (id=1).


## Seeding a set of data related to Licenças

On your terminal, execute the command:

`docker-compose -f docker-compose-local.yml exec web python manage.py loaddata licenca.yaml`

It'll create feed data for these models:

- OrgaoExpeditor
- TipoLicenca
- Licenca
- TipoRecorrencia
- Condicionante
- StatusProtocolo
- Protocolo