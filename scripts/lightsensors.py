#!/usr/bin/env python
#encoding: utf8
import rospy


if __name__ == "__main__":
    rospy.init_node("lightsensors")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        with open("/dev/rtlightsensor0","r") as r:
            l = [s.rstrip() for s in r.readlines()] ##改行が含まれてしまうので取り除いた
            
            rate.sleep()