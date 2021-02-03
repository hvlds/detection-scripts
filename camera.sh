# gnome-terminal -- /bin/bash -c "source ~/start_noetic.sh; roslaunch detection only_infrared.launch; exec bash" &
gnome-terminal -- /bin/bash -c "source ~/scripts/start_noetic.sh; roslaunch detection only_camera.launch; exec bash" &
sleep 2
gnome-terminal -- /bin/bash -c "source ~/scripts/start_bridge.sh; ros2 run ros1_bridge static_bridge_filtered_camera; exec bash" &
sleep 2
gnome-terminal -- /bin/bash -c "source ~/scripts/start_foxy.sh; ros2 launch irtracking infrared_tracking_launch.py; exec bash" &
sleep 2
gnome-terminal -- /bin/bash -c "source ~/scripts/start_foxy.sh; ros2 run rqt_image_view rqt_image_view; exec bash" &
sleep 2
gnome-terminal -- /bin/bash -c "source ~/scripts/start_foxy.sh; ros2 interface list; exec bash" &
