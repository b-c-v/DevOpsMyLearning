**_Description:_**
Create two Docker containers (Jenkins and Centos) and establish an SSH connection between them.

1. Create an SSH-key in the "dir_centos" folder by running the command:
   ```bash
   ssh-keygen -f id_rsa
   ```
2. Change owner of the folder "jenkins_home" to current user:

2.1 Find out the ID number of the current user

```bash
id
```

2.2 Change owner

```bash
chown id:id jenkins_home
```

3. Run building

```bash
docker-compose up -d
```

4. Check connection from Jenkins container to Centos container with password "any_password"

- connect to Jenkins container

```bash
docker container exec -it any_name_host bash
```

- connect from Jenkins to Centos container

```bash
ssh any_user@any_name_remote_host
```

6. Copy private SSH-key to container with Jenkins (public key was downloaded to Centos during creating Docker image)

- From local server copy created in p.1 private SSH-key

```bash
docker container cp dir_centos7/id_rsa any_name_host:/tmp/id_rsa
```

- Connect from Jenkins using copied SSH-key

```bash
ssh -i /tmp/id_rsa any_user@any_name_remote_host
```
