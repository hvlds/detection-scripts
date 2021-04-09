import os
import time
import sys


def start_camera(exec_dir):
    """Start the launch script for the camera Asus Xtion running in ROS(1)
    Noetic.

    Args:
        exec_dir (str): Directory with the launch scripts for the project
    """
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_noetic.sh;"
        "roslaunch detection only_camera.launch;"
        "exec bash' &")


def start_bridge(exec_dir):
    """Start ros1_bridge to enable communication between ROS1 and ROS2

    Args:
        exec_dir (str): Directory with the launch scripts for the project
    """
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_bridge.sh;"
        "ros2 run ros1_bridge static_bridge_filtered_camera;"
        "exec bash' &")


def start_static_tf(exec_dir):
    """Publish basic static tf broadcaster for the map->base_link relationship 

    Args:
        exec_dir (str): Directory with the launch scripts for the project
    """
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_foxy.sh;"
        "ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 1 map base_link' &")


def start_irtracking(exec_dir):
    """Start the irtracking project (ROS2)

    Args:
        exec_dir (str): Directory with the launch scripts for the project
    """
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_foxy.sh;"
        "ros2 launch irtracking infrared_tracking_launch.py;"
        "exec bash' &")


def start_image_viewer(exec_dir):
    """Start the image viewer (ROS2)

    Args:
        exec_dir (str): Directory with the launch scripts for the project
    """
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_foxy.sh;"
        "ros2 run rqt_image_view rqt_image_view;"
        "exec bash' &")

def only_irmarker():
    exec_list = [start_camera, start_bridge, start_static_tf, 
        start_irtracking, start_image_viewer]
    script_path = os.path.realpath(sys.argv[0])
    temp_dir = script_path.split("/")
    script_dir = "/".join(temp_dir[0:-1]) + "/bash_scripts"

    for step in exec_list:
        step(script_dir)
        time.sleep(2)

if __name__ == "__main__":
    only_irmarker()
