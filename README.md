<p align="center">
  <img src="/img/Telegram_bot_logo.png" alt="Logo" style="border-radius: 50%;" width="200" height="200" />
  <br>
  <h1 align="center">EduCloud</h1>
</p>

A Python-based Telegram bot leveraging GCP to organize and share academic resources like PDFs and videos, tailored for university students by faculty and degree.

# List of tools we used
* <a href="https://www.python.org"><img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" alt="Python" width="25" height="30"/> Python</a>
* <a href="https://www.postgresql.org"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/540px-Postgresql_elephant.svg.png" alt="PostgreSQL" width="30" height="30"/> PostgreSQL</a>
* <a href="https://core.telegram.org/bots/api"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/512px-Telegram_logo.svg.png?20220101141644" alt="Telegram" width="30" height="30"/> Telegram Bot API</a>
* <a href="https://cloud.google.com"><img src="https://seeklogo.com/images/G/google-cloud-logo-6B950E8ADB-seeklogo.com.png" alt="Google Cloud Platform (GCP)" width="30" height="25"/> Google Cloud Platform (GCP)</a>
* <a href="https://www.docker.com"><img src="https://cdn.worldvectorlogo.com/logos/docker-4.svg" alt="Docker" width="30" height="30"/> Docker</a>

## Setup
1. Create a copy of .env_example and rename it to .env.
2. Fill in all the necessary variables in the .env file.

## Running the Application
To build the Docker image and start the application, run the following commands:
```py
docker build -t telegram_bot .
docker run -it --name Telegram_bot telegram_bot
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>
