FROM ubuntu:latest

# Install required packages
RUN apt update && apt install -y python3.12 openssh-server && \
    mkdir /var/run/sshd && \
    echo 'root:root' | chpasswd

# Enable and start the SSH service
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    mkdir -p /root/.ssh

EXPOSE 22

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]
