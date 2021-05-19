# PicoZense (Ubuntu18 and ROS Melodic)

## Install


```bash
cd ~/catkin_ws/src
git clone https://github.com/Funderburger/pico_zense_camera.git
cd ..
catkin make 
source devel/setup.bash
```


## Usage 

```bash
roslaunch pico_zense_camera pz_camera.launch
```

### Some configurations in order to use depthimage_to_laserscan while not wasting too much time

With this camera, we had some troubles when using this package (segmentation fault, without any other warning) and that was because our camera_info didn't contained the R matrix, and without it couldn't make the conversion from depth to laser, so first make sure you have this matrix. (but of course, if you have this repo it should be ok)

Follow these steps if you want to use depthimage_to_laserscan package:

1. Start the camera: 

`roslaunch pico_zense_camera pz_camera.launch`

2. Start the pointcloud node (maybe, you might need to install this: `sudo apt install ros-melodic-depth-image-proc`):

`roslaunch pico_zense_camera camera_node_depth_image_proc.launch`

3. Start the laser scan: 

`roslaunch pico_zense_camera depth_laser_scan.launch`

4. Run "The Savior": 

`roslaunch pico_zense_camera tf_important_for_laser.launch`

5. And... that's it, you can open `rviz` to visualise this beauty.
