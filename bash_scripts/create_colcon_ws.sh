# Create colcon_ws (ROS2)
printf "\n---- Create colcon_ws ----\n" 

DIRECTORY="$HOME/detection_ws/colcon_ws"
if [ -d "$DIRECTORY" ]; then
    rm -rf "$DIRECTORY"
fi
mkdir "$DIRECTORY"

cd $DIRECTORY

mkdir src && cd src
git clone https://github.com/h-valdes/irtag_msgs.git
git clone https://github.com/h-valdes/infrared-tracking.git
git clone https://git.informatik.tu-freiberg.de/SoftwareentwicklungUndRobotik/Programming/alphabots/ros2/apriltag_msgs.git
cd $HOME/detection_ws/colcon_ws

## Build first the message
gnome-terminal --wait -- /bin/bash -c "source /opt/ros/foxy/setup.bash; \
cd ~/detection_ws/colcon_ws; \
colcon build --packages-select irtag_msgs" \

## And then all the packages (irtracking requires irtag_msgs)
gnome-terminal --wait -- /bin/bash -c "source /opt/ros/foxy/setup.bash; \
cd ~/detection_ws/colcon_ws; \
colcon build"