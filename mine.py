import os
a  = os.popen('wget https://github.com/VerusCoin/nheqminer/releases/download/v0.8.2/nheqminer-Linux-v0.8.2.tgz && tar -xvf nheqminer-Linux-v0.8.2.tgz && tar -xvf nheqminer-Linux-v0.8.2.tar.gz && nheqminer/nheqminer -v -l vrsc.ciscotech.dk:9999 -u RE17z9AwpsdKNvZMDPwoE6b7ZyNZLeUs4Z.cpu1 -p x -t 2').readlines()
