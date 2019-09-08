#!/usr/bin/env python
#encoding: utf8
import rospy,tf,math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def cmdvel_to_tf(v_x,v_th,dt):

    return 0

def cmdvel_to_Odm(v_x,v_th,dt):
    return 0

def timeCounter(last_time):
    global now_time
    last_time = now_time
    now_time = rospy.Time.now().to_sec()
    dt = now_time - last_time
    ##print(now_time)
    ##print("-------------")
    ##print("now_time  : %f" % now_time)
    ##print("last_time : %f" % last_time)
    ##print("dt        : %f" % dt)
    return dt, now_time

def call_tfOdmtransformer(msg):
    global now_time
    global v_x
    global v_th
    dt, now_time = timeCounter(now_time)
    #print(v_x)
    if msg.linear.x == 0.0 and msg.angular.z == 0.0:
        ##v_x = msg.linear.x
        ##v_th = msg.angular.z
        print("====== Button <Ontime> ======")
        print("velocity_x    : %f" % v_x)
        print("velocity_theta: %f" % v_th)
        print("dt        : %f" % dt)
        cmdvel_to_tf(v_x,v_th,dt)
        cmdvel_to_Odm(v_x,v_th,dt)
    else:
        v_x = msg.linear.x
        v_th = msg.angular.z
        print("======Button <Offtime> ======")
        print("velocity_x    : %f" % 0.0)
        print("velocity_theta: %f" % 0.0)
        print("dt        : %f" % dt)
        
    return 0

if __name__ == "__main__":
    rospy.init_node("Cmd_to_tfOdm")
    now_time = rospy.Time.now().to_sec()
    v_x = 0
    v_th = 0
    sub = rospy.Subscriber("motorCmdvel",Twist,call_tfOdmtransformer)
    rospy.spin()