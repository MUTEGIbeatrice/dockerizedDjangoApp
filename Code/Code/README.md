

## Project Description


### How To run the code

- Download python 3.10.7 form (https://www.python.org/downloads/) 

- Use any terminal available 

- Navigate to the folder using the command line interface 

- Install all requirements using the following command:
	Pip install -r req.txt
- The file will download all required python libraries and dependencies to function

- To start the server with SSL enabled:
  	python manage.py runsslserver --certificate cert.pem --key key.pem

- Run the development server using the following command without SSL enabled if required :
 	 Python manage.py runserver

- Navigate to the local host IP address: “Usually set to http://127.0.0.1:8000”

- If an account is locked, use the following command: 
  Python manage.py axes_reset

- to run in docker, 
	install docker version 4.13 (https://desktop.docker.com/win/main/amd64/89412/Docker%20Desktop%20Installer.exe)
	switch to windows containers (on the docker's icon on the taskbar)

on the terminal run     docker compose up --build

run docker-compose build 

returned this Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them......will do later
docker login
docker scan --login
you'll need to authenticate your snyk account
docker scan python:3.11
docker scan app:django

docker-compose up

Credentials: Beatrice