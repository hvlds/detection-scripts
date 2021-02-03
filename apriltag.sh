gnome-terminal -- /bin/bash -c "source ~/start_noetic.sh; roslaunch detection detection.launch; exec bash" &
sleep 5
gnome-terminal -- /bin/bash -c "source ~/start_bridge.sh; ros2 run ros1_bridge static_bridge_apriltag; exec bash" &
sleep 5
gnome-terminal -- /bin/bash -c "source ~/start_foxy.sh; ros2 topic list; exec bash" &
