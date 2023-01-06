FROM centos:7

RUN yum -y install openssh-server

RUN useradd any_user && \
    echo "1234" | passwd any_user  --stdin && \
    mkdir /home/any_user/.ssh && \
    chmod 700 /home/any_user/.ssh

COPY id_rsa.pub /home/any_user/.ssh/authorized_keys

RUN chown any_user:any_user   -R /home/any_user && \
    chmod 600 /home/any_user/.ssh/authorized_keys

RUN /usr/sbin/sshd-keygen > /dev/null 2>&1

RUN yum -y install mysql

RUN yum -y install wget && \
    yum -y install epel-release && \
    yum -y install python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install awscli


CMD /usr/sbin/sshd -D

