import os
import time

SCRIPTS_DIR = "~/scripts"


def start_camera():
    os.system(
        f"gnome-terminal -- /bin/bash -c 'source {SCRIPTS_DIR}/start_noetic.sh;"
        "roslaunch detection only_camera.launch;"
        "exec bash' &")


def start_bridge():
    os.system(
        f"gnome-terminal -- /bin/bash -c 'source {SCRIPTS_DIR}/start_bridge.sh;"
        "ros2 run ros1_bridge static_bridge_filtered_camera;"
        "exec bash' &")


def start_static_tf():
    os.system(
        f"gnome-terminal -- /bin/bash -c 'source {SCRIPTS_DIR}/start_foxy.sh;"
        "ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 1 map base_link' &")


def start_irtracking():
    os.system(
        f"gnome-terminal -- /bin/bash -c 'source {SCRIPTS_DIR}/start_foxy.sh;"
        "ros2 launch irtracking infrared_tracking_launch.py;"
        "exec bash' &")


def start_image_viewer():
    os.system(
        f"gnome-terminal -- /bin/bash -c 'source {SCRIPTS_DIR}/start_foxy.sh;"
        "ros2 run rqt_image_view rqt_image_view;"
        "exec bash' &")


if __name__ == "__main__":
    exec_list = [start_camera, start_bridge, start_static_tf,
                    start_irtracking, start_image_viewer]

    for step in exec_list:
        step()
        time.sleep(2)
