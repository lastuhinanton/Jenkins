#!/bin/bash"

add_user()
{
  USER=$1
  PASSWORD=$2
  useradd -m -s /bin/bash $USER
  echo "$USER:$PASSWORD" | chpasswd
}

add_user user 123456789
service ssh start
service ssh enable
/bin/bash
