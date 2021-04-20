import os
from utils import *


def clone_repositories(base_dir):
    os.system(
        f"cd {base_dir};"
        "mkdir src && cd src;"
        "git clone https://github.com/h-valdes/irtag_msgs.git;"
        "git clone https://github.com/h-valdes/infrared-tracking.git;"
        "git clone https://git.informatik.tu-freiberg.de/SoftwareentwicklungUndRobotik/Programming/alphabots/ros2/apriltag_msgs.git;")


def build_msg(base_dir):
    os.system(
        "gnome-terminal --wait -- /bin/bash -c 'source /opt/ros/foxy/setup.bash;"
        f"cd {base_dir};"
        "colcon build --packages-select irtag_msgs")


def build_pkgs(base_dir):
    build_msg(base_dir)
    os.system(
        "gnome-terminal --wait -- /bin/bash -c 'source /opt/ros/foxy/setup.bash;"
        f"cd {base_dir};"
        "colcon build")

def build_colcon_ws():
    # check_directory(colcon_ws)
    build_pkgs(colcon_ws)


if __name__ == "__main__":
    build_colcon_ws()
