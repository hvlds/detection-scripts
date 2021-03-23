import os

def check_directory(base_dir):
    if os.path.exists(base_dir):
        os.rmdir(base_dir)
    else:
        os.mkdir(base_dir)

home_dir = os.path.expanduser("~")
detection_ws = f"{home_dir}/detection_ws"

catkin_ws = f"{detection_ws}/catkin_ws"
bridge_ws = f"{detection_ws}/bridge_ws"
colcon_ws = f"{detection_ws}/colcon_ws"