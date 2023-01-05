FROM centos:7

RUN yum -y install openssh-server

RUN useradd any_user && \
    echo "any_password" | passwd any_user  --stdin && \
    mkdir /home/any_user/.ssh && \
    chmod 700 /home/any_user/.ssh

COPY id_rsa.pub /home/any_user/.ssh/authorized_keys

RUN chown any_user:any_user   -R /home/any_user && \
    chmod 600 /home/any_user/.ssh/authorized_keys

RUN /usr/sbin/sshd-keygen

CMD /usr/sbin/sshd -D
