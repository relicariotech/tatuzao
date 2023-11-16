
## Obtaining the tatuzao's codebase
git clone https://github.com/relicariotech/tatuzao.git

`cd tatuzao`

Open on your Editor. We recommend using Visual Studio Code.

## Conteiners services
On your terminal, execute the command to run the docker-compose locally:

`docker-compose -f docker-compose.yml up --build`


Two conteiners will be up and running. These conteiners are described on docker-compose.yml.
- web
- db

## Other Commands

After setting up the conteiners, execute the following commands:

`docker-compose -f docker-compose.yml exec web python manage.py makemigrations` 

`docker-compose -f docker-compose.yml exec web python manage.py migrate`

`docker-compose -f docker-compose.yml exec web python manage.py createsuperuser`

At this point, tatuzao application will be running and with your superuser.

## Creating basic elements
Login on /admin interface based on your environment.