import os 
import time
import signal
import subprocess

def photo(filename):
     print("Taking photo")
     proc = subprocess.Popen("sudo fswebcam -r /dev/video0 "+filename,
     shell=True, 
     preexec_fn=os.setsid) 
     time.sleep(5)
     os.killpg(os.getpgid(proc.pid), signal.SIGTERM)