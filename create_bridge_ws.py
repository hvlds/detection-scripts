import os
from utils import *

def clone_repositories(base_dir):
    os.system(
        f"cd {base_dir};"
        "mkdir src && cd src;"
        "git clone https://github.com/h-valdes/ros1_bridge.git;")

def build_bridge_ws():
    clone_repositories(bridge_ws)
    os.system(
        "gnome-terminal --wait -- /bin/bash -c 'source /opt/ros/foxy/setup.bash;"
        "source ~/detection_ws/colcon_ws/install/local_setup.bash;"
        "source /opt/ros/noetic/setup.bash;"
        "source ~/detection_ws/catkin_ws/devel/setup.bash;"
        "cd ~/detection_ws/bridge_ws;"
        "colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure")

if __name__ == "__main__":
    build_bridge_ws()