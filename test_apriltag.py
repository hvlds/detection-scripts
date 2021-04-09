import os
import time
import sys
from camera import start_camera, start_bridge
from utils import *

def echo_apriltag(exec_dir):
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_foxy.sh;"
        "ros2 topic echo /tag_detections;"
        "exec bash' &"
    )

def start_bag(exec_dir):
    pass


if __name__ == "__main__":
    exec_list = [start_camera, start_bridge, echo_apriltag]

    script_path = os.path.realpath(sys.argv[0])
    temp_dir = script_path.split("/")
    script_dir = "/".join(temp_dir[0:-1]) + "/bash_scripts"

    for step in exec_list:
        step(script_dir)
        time.sleep(4)