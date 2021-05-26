Hello world

## info
this is a hello world app

## High level design

Use http://asciiflow.com/ to show your diagrams

# Developing
1. Create a virtualenv to hold the project (`python3.9 -m venv venv`)
2. Active the virtual environment just created by: `source venv/bin/activate `
3. Install the project library: `pip install -r requirements.txt`

#  To run the app in docker, run:
`
docker-compose up -d
`

# To take down the app, run:
`
docker-compose down -v
`

# To check the services, run:
`
docker ps
`

# default username and password for grafana:
`
username: admin
pass: admin
`

# url for prometheus:
`
http://[your ip address]:9090
`

# to kill a service, e.g. app
`
docker rm -f app
`