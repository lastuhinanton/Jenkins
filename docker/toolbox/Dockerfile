FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y && apt-get install sudo ssh -y
RUN echo 'root:123456789' | chpasswd
RUN sed -ri 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
COPY ./script.sh .
ENTRYPOINT ["bash", "script.sh"]
