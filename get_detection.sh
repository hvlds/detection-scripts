cd $HOME

# Create detection workspace in home directory
mkdir detection_ws

# Create sub-workspace for the project
cd detection_ws
mkdir bridge_ws
mkdir colcon_ws
mkdir catkin_ws

# Create catkin_ws (ROS1) 
cd $HOME/detection_ws/catkin_ws
mkdir src && cd src
git clone https://github.com/h-valdes/detection.git
git clone https://github.com/h-valdes/apriltag_ros
git clone https://github.com/ros-drivers/openni2_camera
cd .. # go to catkin_ws
gnome-terminal --wait -- /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin build"

# Create colcon_ws (ROS2)
cd $HOME/detection_ws/colcon_ws
mkdir src && cd src
git clone https://git.informatik.tu-freiberg.de/SoftwareentwicklungUndRobotik/Programming/alphabots/infrared-tracking.git
git clone https://git.informatik.tu-freiberg.de/SoftwareentwicklungUndRobotik/Programming/alphabots/ros2/apriltag_msgs.git
cd infrared-tracking
git checkout ros2
cd .. # go to colcon_ws
gnome-terminal --wait -- /bin/bash -c "source /opt/ros/foxy/setup.bash; colcon build"

# Create bridge_ws (ros1_bridge)
cd $HOME/detection_ws/bridge_ws
mkdir src && cd src
git clone https://github.com/h-valdes/ros1_bridge.git

# go back to detection_ws
cd $HOME/detection_ws 
