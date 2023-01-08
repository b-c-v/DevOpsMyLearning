**_Description:_**
Select values from DB and show them on WebPage (Jenkins==>Ansible==>MySQL==>PHP project with Docker container).

## 1. Create an SSH-key

- in the folder "docker_centos7" run:

```bash
ssh-keygen -f id_rsa
```

- copy private key to the folder docker_jenkins:

```bash
cp id_rsa ../jenkins_data/ansible/id_rsa
```

## 2. If needed change owner of the folder "jenkins_data" to current user:

2.1 Find out the ID number of the current user

```bash
id
```

2.2 Change owner

```bash
chown id:id jenkins_data
```

## 3. Building Docker images and containers

- install Docker and Docker Compose - run [script](install_docker.sh)
- run building images

```bash
docker-compose up -d
```

## 4. Copy private SSH-key to container with Jenkins (public key was downloaded to Centos during creating Docker image)

- From local server copy created in p.1 private SSH-key

```bash
docker container cp docker_centos7/id_rsa jenkins_container:/tmp/id_rsa
```

- Connect from Jenkins using copied SSH-key

```bash
docker container exec -it jenkins_container bash
ssh -i /tmp/id_rsa centos_user@centos_container
```

## 5. In Jenkins

- In log find password to Jenkins GUI:

```
docker logs -f jenkins_container
```

- Install plugin SSH
- Add credentials to connect to remote host Centos (Manage Jenkins ==> Manage Credentials ==> global). Username: centos_user; Private Key: copy value of public key from p.1
- Add remote host (Manage Jenkins ==> Configure System ==> SSH remote hosts). Hostname: centos_container; Port: 22; Credentials: look p.4

## 6. Connect to MySQL database from local computer:

- connect to container with MySQL:
  ```
  docker container exec -it mysql_container bash
  ```
- connect to DB

  ```
  mysql -u root -h db -p1234
  ```
