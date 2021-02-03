cd $HOME

# Create detection workspace in home directory
mkdir detection_ws

# Create sub-workspace for the project
cd detection_ws
mkdir bridge_ws
mkdir colcon_ws
mkdir catkin_ws

# Clone bridge_ws (ros1_bridge) requirements
cd bridge_ws
mkdir src && cd src
git clone https://github.com/h-valdes/ros1_bridge.git
cd ../.. # go back to detection_ws

# Clone catkin_ws (ROS1) requirements
cd catkin_ws
mkdir src && cd src
git clone https://github.com/h-valdes/detection.git
git clone https://github.com/h-valdes/apriltag_ros
cd ..
gnome-terminal -- /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin build; exec bash" &
cd .. # go back to detection_ws

# Clone colcon_ws (ROS2)
## TODO: Project infrared-tracking is in gitlab