SCRIPTS_DIR="~/scripts"

gnome-terminal -- /bin/bash -c "source ${SCRIPTS_DIR}/start_noetic.sh; \
roslaunch detection only_camera.launch; \
exec bash" &

sleep 2

gnome-terminal -- /bin/bash -c "source ${SCRIPTS_DIR}/start_bridge.sh; \
ros2 run ros1_bridge static_bridge_filtered_camera; \
exec bash" &

sleep 2

gnome-terminal -- /bin/bash -c "source ${SCRIPTS_DIR}/start_foxy.sh; \
ros2 launch irtracking infrared_tracking_launch.py; \
exec bash" &

sleep 2

gnome-terminal -- /bin/bash -c "source ${SCRIPTS_DIR}/start_foxy.sh; \
ros2 run rqt_image_view rqt_image_view; \
exec bash" &

sleep 2

gnome-terminal -- /bin/bash -c "source ${SCRIPTS_DIR}/start_foxy.sh; \
ros2 topic echo /raw_tag_detections; \
exec bash" &