import message_filters
from sensor_msgs.msg import Image, CameraInfo, TimeReference
import numpy as np

import rospy
from cv_bridge import CvBridge 


bridge = CvBridge()

frame = bridge.imgmsg_to_cv2()
image_time_ref_msg = TimeReference()
image_time_ref_msg.source = "image"
image_time_ref_msg.header.stamp = 

image_sub = message_filters.Subscriber('image', Image)
ts = message_filters.ApproximateTimeSynchronizer()

pub = rospy.Publisher('ceva', CameraInfo,queue_size=10)

pub.publish()