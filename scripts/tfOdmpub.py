#!/usr/bin/env python
#encoding: utf8
import rospy
from geometry_msgs.msg import Twist

def transform_tfOdm(msg):
    v_x = msg.linear.x
    v_th = msg.angular.z
    print("-----------")
    print(v_x)
    print(v_th)
    return 0

if __name__ == "__main__":
    rospy.init_node("Cmd_to_tfOdm")
    sub = rospy.Subscriber("motorCmdvel",Twist,transform_tfOdm)
    rospy.spin()