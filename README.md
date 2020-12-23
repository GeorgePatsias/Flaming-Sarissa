<p align="center">
  <a href="" rel="noopener">
 <img src="https://turningpointsoftheancientworld.com/wp-content/uploads/2018/07/Phalanx1-672x372.png" alt="Project logo"></a>
</p>

<h3 align="center">Flaming Sarissa</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
</div>

---

<p align="center">Dynamic deployment of temporary Infrastructure for Software Execution.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

The purpose of this project is to scale the use of your scripts on the Cloud.
Dynamicaly create a temporary infrastracture to accomodate your Shellcodes, Scans, Docker images, Nmap scans collecting the results to a centralized platform. The platform distributes the command execution to servers every region, not raising flags about targeted attacks and requests that cannot be backtracked, after that destroys the infrastructure and presenting the report to the platform.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

### Create a Virtual Environment
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv -p python3 venv 
```

### Activating the Virtual Environment
```
. venv/bin/activate
```

### Install Requirements
```
pip install -r requirements.txt
```

### Run the Server
```
python3 server.py
```

## 🚀 Deployment <a name = "deployment"></a>

For production deployment use the Compose.

```
docker-compose up -d
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/download/releases/3.0/) - Language
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Server Framework
- [MongoDB](https://www.mongodb.com/) - Database
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - UI Structure
- [Docker](https://www.docker.com/) - Docker image
- [Docker Compose](https://docs.docker.com/compose/) - Docker Compose YAML
- [Terraform](https://www.terraform.io/) - Infrastructure Deployment
- [Ansible](https://www.ansible.com/) - Infrastructure Automation
## ✍️ Author <a name = "authors"></a>

- [Me](https://github.com/GeorgePatsias) - Development
- [byt3bl33d3r](https://github.com/byt3bl33d3r/Red-Baron) - Idea

