import os 
import time
import signal
import subprocess

def photo(filename):
     # Takes a photo using the webcam
     print("Taking photo")

     # Execute a command line to schedule a photo to be taken and save it
     proc = subprocess.Popen("sudo fswebcam -r /dev/video0 "+filename,
     shell=True, 
     preexec_fn=os.setsid) 
     
     # Give the camera time to take and save the picture
     time.sleep(5)
     os.killpg(os.getpgid(proc.pid), signal.SIGTERM)