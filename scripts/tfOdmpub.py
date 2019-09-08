#!/usr/bin/env python
#encoding: utf8
import rospy,tf,math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def cmdvel_to_tf():
    return 0

def cmdvel_to_Odm():
    return 0


def call_tfOdmtransformer(msg):
    v_x = msg.linear.x
    v_th = msg.angular.z
    print("==============")
    print("velocity_x    : %f" % v_x)
    print("velocity_theta: %f" % v_th)
    cmdvel_to_tf(v_x,v_th)
    cmdvel_to_Odm(v_x,v_th)
    return 0

if __name__ == "__main__":
    rospy.init_node("Cmd_to_tfOdm")
    sub = rospy.Subscriber("motorCmdvel",Twist,transform_tfOdm)
    rospy.spin()