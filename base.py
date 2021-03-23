import os
from utils import *

def make_subdirs(base_dir):
    os.mkdir(base_dir + "/bridge_ws")
    os.mkdir(base_dir + "/colcon_ws")
    os.mkdir(base_dir + "/catkin_ws")

if __name__ == "__main__":
    check_directory(detection_ws)