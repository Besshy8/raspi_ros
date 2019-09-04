#!/usr/bin/env python
#encoding: utf8

import rospy 
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("KeyBoardController")
    pub = rospy.Publisher("motorCmdvel",Twist,queue_size=10)
    print("----Enter key------")
    while True:
        val = raw_input("Enter key : ")
        print("keyboard input is : %s" % val)
        if val == "d":
            print("keyboard input is shutdown")
            break
    rospy.spin()