[![.github/workflows/main.yml](https://github.com/kopf8/foodgram/actions/workflows/main.yml/badge.svg)](https://github.com/kopf8/foodgram/actions/workflows/main.yml)

# 📝 [foodgram](https://github.com/kopf8/foodgram.git)
### <br>➜ https://yandex-foodgram.hopto.org/
<br><hr>

### Contents:

1. [Project tech stack](#project-tech-stack)
2. [Description](#project-description)
3. [Project deployment](#project-deployment)
4. [Project documentation](#project-documentation)
5. [Project created by](#project-created-by)
<br><hr>

## Project tech stack:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![React](https://img.shields.io/badge/-ReactJs-61DAFB?logo=react&logoColor=white&style=for-the-badge)](https://react.dev/)

<br><hr>
## Project description:

"Foodgram" project is a website where users will publish their recipes, add other people's recipes to favorites and subscribe to publications by other authors.
The Shopping List service will also be available to registered users. It will allow you to create a list of products that you need to buy to prepare selected dishes.

<br>Project website: https://yandex-foodgram.hopto.org/

<hr>

## Project deployment:

First of all you need to fork this repository into your GitHub account.
<br>Then setup all the necessary secrets in your newly created fork-repository:

```bash
# GitHub repository -> Settings -> Secrets and variables -> Actions:
# create all secrets which are needed for CI/CD to access your host server, DockerHub and GitHub
DOCKER_PASSWORD
DOCKER_USERNAME
HOST
SSH_KEY
SSH_PASSPHRASE
USER
TELEGRAM_TO
TELEGRAM_TOKEN
```

Then login to your host server and install all necessary components:
```bash
# username - your username to access Virtual Machine (VM) on host server, ip - ip-address of your VM working under Linux.
ssh username@ip
```

```bash
sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
```

```bash
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh
```

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

```bash
sudo systemctl start docker.service && sudo systemctl enable docker.service
```

When all components are successfully installed, you need to create directory **/foodgram** in your home directory **/home/username/** on your VM:

```bash
cd ~
```

```bash
mkdir foodgram
```

The next step is to create file **.env** in directory **/foodgram/**:

```bash
touch .env
```

This .env file needs to be filled with your variables needed for backend and database containers:

```python
POSTGRES_USER=foodgram_user # username for PostgreSQL database
POSTGRES_PASSWORD=foodgram_password # password for PostgreSQL database
POSTGRES_DB=foodgram # name for PostgreSQL database
DB_HOST=db # hostname for PostgreSQL database
DB_PORT=5432 # port PostgreSQL database
SECRET_KEY='your_secret_key' # Django secret key
ALLOWED_HOSTS=11.111.111.11,some.domain.org,127.0.0.1,localhost # Your VM host URL and IP address
DEBUG=True # Django debug setting flag
```
Example .env file can be found in the project root directory: [.env.example](https://github.com/kopf8/foodgram/blob/main/.env.example)

Initial setup is done.
After that you can clone your repository to your local machine via SSH link using the following command in your terminal: 

```bash
git clone git@github.com:username/foodgram.git # <username> is your GitHub username 
```

After you finished working with the code, commit & push all changes to your GitHub repository.
Project CI/CD procedure will automatically deploy all changes to your remote VM using GitHub Actions workflow.
You will receive a message in Telegram once deployment is successfully finished.

## Project documentation
Documentation can be accessed via the following link after deployment:

```url
http://<your.server.address>/api/docs/
```

## Project created by:
### [Maria Kirsanova](https://github.com/kopf8)