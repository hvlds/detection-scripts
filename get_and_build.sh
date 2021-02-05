cd $HOME

# Create detection workspace in home directory (delete if already exists)
DIRECTORY="./detection_ws"
if [ -d "$DIRECTORY" ]; then
    rm -rf detection_ws
fi
mkdir detection_ws

# Create sub-workspace for the project
cd detection_ws
mkdir bridge_ws
mkdir colcon_ws
mkdir catkin_ws

# Create catkin_ws (ROS1)
printf "\n---- Create catkin_ws ----\n" 
cd $HOME/detection_ws/catkin_ws
mkdir src && cd src
git clone https://github.com/h-valdes/detection.git
git clone https://github.com/h-valdes/apriltag_ros
git clone https://github.com/ros-drivers/openni2_camera
cd .. # go to catkin_ws
gnome-terminal --wait -- /bin/bash -c "source /opt/ros/noetic/setup.bash; \
cd ~/detection_ws/catkin_ws; \
catkin build"

. $HOME/scripts/create_colcon_ws.sh

# Create bridge_ws (ros1_bridge)
printf "\n---- Create bridge_ws ----\n" 
cd $HOME/detection_ws/bridge_ws
mkdir src && cd src
git clone https://github.com/h-valdes/ros1_bridge.git
gnome-terminal --wait -- /bin/bash -c "source /opt/ros/foxy/setup.bash; \
source ~/detection_ws/colcon_ws/install/local_setup.bash; \
source /opt/ros/noetic/setup.bash; \
source ~/detection_ws/catkin_ws/devel/setup.bash; \
cd ~/detection_ws/bridge_ws;\
colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure"

# go back to detection_ws
cd $HOME/detection_ws 
