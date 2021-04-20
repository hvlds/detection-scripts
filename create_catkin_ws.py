import os
from utils import *


def clone_repositories(base_dir):
    os.system(
        f"cd {base_dir};"
        "mkdir src && cd src;"
        "git clone https://github.com/h-valdes/detection.git;"
        "git clone https://github.com/h-valdes/apriltag_ros;"
        "git clone https://github.com/ros-drivers/openni2_camera")


def build_catkin_ws():
    # clone_repositories(catkin_ws)
    os.system(
        f"cd {catkin_ws};"
        "gnome-terminal --wait -- /bin/bash -c 'source /opt/ros/noetic/setup.bash;"
        "cd ~/detection_ws/catkin_ws;"
        "catkin build'")

if __name__ == "__main__":
    build_catkin_ws()