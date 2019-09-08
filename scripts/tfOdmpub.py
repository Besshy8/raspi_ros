#!/usr/bin/env python
#encoding: utf8
import rospy,tf,math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def cmdvel_to_tf(v_x,v_th):

    return 0

def cmdvel_to_Odm(v_x,v_th):
    return 0

def timeCounter(last_time):
    global now_time
    last_time = now_time
    now_time = rospy.Time.now().to_sec()
    dt = now_time - last_time
    ##print(now_time)
    print("-------------")
    print("now_time  : %f" % now_time)
    print("last_time : %f" % last_time)
    print("dt        : %f" % dt)
    return dt, now_time

def call_tfOdmtransformer(msg):
    global now_time
    dt, now_time = timeCounter(now_time)
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
    now_time = rospy.Time.now().to_sec()
    sub = rospy.Subscriber("motorCmdvel",Twist,call_tfOdmtransformer)
    rospy.spin()