FROM centos:7

RUN yum -y install openssh-server

RUN useradd centos_user && \
    echo "1234" | passwd centos_user  --stdin && \
    mkdir /home/centos_user/.ssh && \
    chmod 700 /home/centos_user/.ssh

COPY id_rsa.pub /home/centos_user/.ssh/authorized_keys

RUN chown centos_user:centos_user   -R /home/centos_user && \
    chmod 600 /home/centos_user/.ssh/authorized_keys

RUN /usr/sbin/sshd-keygen > /dev/null 2>&1

CMD /usr/sbin/sshd -D

