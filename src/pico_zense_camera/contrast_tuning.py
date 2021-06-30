#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image

from cv_bridge import CvBridge
import cv2

import numpy as np


net = None
args = None
pub = None


def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(1)


def process_image(msg):
    global net
    global args
    global pub
    global output
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
    try:
        pass
    except Exception as err:
        print(err)

    alpha = 0.15 # Contrast control (1.0-3.0)
    beta = 1 # Brightness control (0-100)
    frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    
    new_ir_msg = bridge.cv2_to_imgmsg(frame,"mono8")
    
    new_ir_msg.header = msg.header
    # new_ir_msg.header.stamp = rospy.Time().now()
    # new_ir_msg.header.frame_id = "contrast"
    pub.publish(new_ir_msg)

def start_node():
    global pub
    rospy.init_node('detect_person')
    rospy.loginfo('detect node started')
    pub = rospy.Publisher('pico_ir_rect', Image, queue_size=1)
    rospy.Subscriber("/pico_zense/ir/image_raw", Image, process_image)

if __name__ == '__main__':
    try:
        start_node()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
