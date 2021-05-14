#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
# from sensor_msgs.msg import RegionOfInterest
from cv_bridge import CvBridge
import cv2
# from tracker.centroidtracker import CentroidTracker
# from tracker.trackableobject import TrackableObject
# from imutils.video import VideoStream
# from imutils.video import FPS
import numpy as np
# import argparse
# import imutils
import time
# import dlib
# import jetson.utils
# import jetson.inference
import sys

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

    # equ = cv2.equalizeHist()
    alpha = 0.15 # Contrast control (1.0-3.0)
    beta = 1 # Brightness control (0-100)
    frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    pub.publish(bridge.cv2_to_imgmsg(frame,"mono8"))

    # showImage(frame)

def start_node():
    global pub
    rospy.init_node('detect_person')
    rospy.loginfo('detect node started')
    pub = rospy.Publisher('pico_img_rect', Image, queue_size=1)
    rospy.Subscriber(
    "/pico_zense/ir/image_raw", Image, process_image)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
