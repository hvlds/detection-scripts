import os
import time
import sys
from camera import start_camera, start_bridge, start_image_viewer, only_irmarker
from utils import *


def echo_apriltag(exec_dir):
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_foxy.sh;"
        "ros2 topic echo /tag_detections;"
        "exec bash' &"
    )


def start_ros1_image_viewer(exec_dir):
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_noetic.sh;"
        "rosrun rqt_image_view rqt_image_view;"
        "exec bash' &"
    )

def start_apriltag_bag(exec_dir, output_file):
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_foxy.sh;"
        f"ros2 bag record /tag_detections -o bag_{output_file};"
        "exec bash' &"
    )

def start_irmarker_bag(exec_dir, output_file):
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_foxy.sh;"
        f"ros2 bag record /irtracking/tag_detections -o bag_{output_file};"
        "exec bash' &"
    )

def start_csv_export(exec_dir, marker):
    os.system(
        f"gnome-terminal -- /bin/bash -c '. {exec_dir}/start_foxy.sh;"
        f"ros2 run plotter {marker};"
        "exec bash' &"
    )

def test_apriltag(output):
    exec_list = [start_camera, start_bridge, start_ros1_image_viewer, 
        echo_apriltag]

    script_path = os.path.realpath(sys.argv[0])
    temp_dir = script_path.split("/")
    script_dir = "/".join(temp_dir[0:-1]) + "/bash_scripts"

    for step in exec_list:
        step(script_dir)
        time.sleep(4)
    
    start_csv_export(script_dir, "apriltag")
    start_apriltag_bag(script_dir, output)


def test_irmarker(output):
    only_irmarker()

    script_path = os.path.realpath(sys.argv[0])
    temp_dir = script_path.split("/")
    script_dir = "/".join(temp_dir[0:-1]) + "/bash_scripts"

    start_csv_export(script_dir, "irmarker")
    start_irmarker_bag(script_dir, output)
