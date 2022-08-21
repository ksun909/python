
import os

import subprocess
import sys
import io
import urllib.request as dw
import pytube

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

yt = pytube.YouTube("https://www.youtube.com/watch?v=RnEqUblyO2I") #�ٿ����� ������ URL ����

vids= yt.streams.filter(file_extension='mp4', progressive=True)
# vids= yt.streams.all()

#���� ���� ����Ʈ Ȯ��
for i in range(len(vids)):
    print(i,',',vids[i])

vnum = int(input("선택? "))

print(vnum)

parent_dir = "C:/Users/ksun9/OneDrive/바탕 화면/!!!Python/section2"
vids[vnum].download(parent_dir) #�ٿ��ε� ����


# new_filename = input("선2?")
#
# default_filename = vids[vnum].default_filename
# subprocess.call(['ffmpeg', '-i',                 #cmd ���ɾ� ����
#     os.path.join(parent_dir, default_filename),
#     os.path.join(parent_dir, new_filename)
# ])

print('호호2!')
