#crontab moi gio 1 lan
import glob
import datetime
from datetime import date
import os
import subprocess as sp
import signal

cmd = 'mkdir -p /data1/camera/$(date +"%d-%m") '
os.system(cmd)

pid  = sp.getoutput(" pgrep -l avconv | awk '{print $1}'")
print(pid)

while True:
    if pid == "":
        print ("Khong co process !!! ")
        break
    else:
        cmd = "kill -HUP " + pid
        print(cmd)
        os.system(cmd)
        print("Da kill process thanh cong")
        pid  = sp.getoutput(" pgrep -l avconv | awk '{print $1}'")

print("Dang quay video")
cmd = 'sudo avconv -i rtsp://admin:P@ssword0958@192.168.100.2:554/onvif1 -c copy -map 0 -f segment -segment_time 3650 -segment_format mkv "/data1/camera/$(date +"%d-%m")/cam-truoc-%03d-$(date +"%Y_%m_%d_%I_%M_%p").mkv" '

os.system(cmd)
