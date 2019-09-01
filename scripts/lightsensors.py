#!/usr/bin/env python
import rospy


if __name__ == "__main__":
    rospy.init_node("lightsensors")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        with open("/dev/rtlightsensor0","r") as r:
            l = r.readlines()
            rospy.loginfo(l)
            rate.sleep()
            