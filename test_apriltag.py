import os
import time
import sys
from camera import start_camera, start_bridge
from utils import *


if __name__ == "__main__":
    exec_list = [start_camera, start_bridge]

    script_path = os.path.realpath(sys.argv[0])
    temp_dir = script_path.split("/")
    script_dir = "/".join(temp_dir[0:-1]) + "/bash_scripts"

    for step in exec_list:
        step(script_dir)
        time.sleep(2)