import os, time
import shutil

path = "/data1/camera"
now = time.time()
so_ngay = 62

for filename in os.listdir(path):
    filestamp = os.stat(os.path.join(path, filename)).st_mtime
    filecompare = now - so_ngay * 86400
    if  filestamp < filecompare:
        print(filename)
        shutil.rmtree(path + "/" + filename)
    else:
        print("Khong xoa gi")
        pass
