import os
from utils import *
from create_catkin_ws import build_catkin_ws
from create_colcon_ws import build_colcon_ws
from create_bridge_ws import build_bridge_ws
import click

def make_subdirs(base_dir):
    os.mkdir(base_dir + "/bridge_ws")
    os.mkdir(base_dir + "/colcon_ws")
    os.mkdir(base_dir + "/catkin_ws")

if __name__ == "__main__":
    check_directory(detection_ws)
    make_subdirs(detection_ws)