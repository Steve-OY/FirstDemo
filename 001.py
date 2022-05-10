import subprocess
import os

obj=[]
for i in range(10):
    aaa = subprocess.Popen("echo 'hello'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    obj.append(aaa)
# print(obj[0].poll())
for i in range(10):
    obj[i].wait()

