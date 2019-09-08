#!/usr/bin/env python
#encoding: utf8

##URL https://wiki.ros.org/navigation/Tutorials/RobotSetup/Odom

import rospy,tf,math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def cmdvel_to_tf(v_x,v_th,dt):
    odm_Quaternion = tf.transformations.quaternion_from_euler(0,0,theta)
    return 0

## wiki.ros.org
##The nav_msgs/Odometry message stores an estimate of the position and velocity of a robot in free space
def cmdvel_to_Odm(v_x,v_th,dt,now_time):
    global x
    global y
    global theta
    #-------------------------
    x += v_x * math.cos(theta) * dt
    y += v_x * math.sin(theta) * dt
    theta += v_th * dt
    #------------------------- 
    odm_Quaternion = tf.transformations.quaternion_from_euler(0,0,theta)
    ##print(odm_Quaternion)
    odm = Odometry()
    ##set the header
    odm.header.stamp = now_time
    odm.header.frame_id = "odom"

    ##set the position
    odm.pose.pose.position.x = x
    odm.pose.pose.position.y = y
    odm.pose.pose.position.z = 0.0

    ## set the orientation
    odm.pose.pose.orientation.x = odm_Quaternion[0]
    odm.pose.pose.orientation.y = odm_Quaternion[1]
    odm.pose.pose.orientation.z = odm_Quaternion[2]
    odm.pose.pose.orientation.w = odm_Quaternion[3]

    ##set the velocity
    odm.child_frame_id = "base_link"
    odm.twist.twist.linear.x = v_x
    odm.twist.twist.angular.z = v_th

    pubOdm.publish(odm)

    print("+++++++++ Odmetry ++++++++++")
    print("x :     %f" % x)
    print("theta : %f" % theta)
    return 0

def timeCounter(last_time):
    global now_time
    last_time = now_time
    now_time = rospy.Time.now()
    dt = (now_time - last_time).to_sec()
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
        cmdvel_to_Odm(v_x,v_th,dt,now_time) ## 止まっている時はtf,Odmを送らないような実装になっている
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
    now_time = rospy.Time.now()
    v_x = 0
    v_th = 0
    x = 0.0
    y = 0.0
    theta = 0.0
    sub = rospy.Subscriber("motorCmdvel",Twist,call_tfOdmtransformer)
    pubOdm = rospy.Publisher("odom",Odometry,queue_size=50)
    rospy.spin()
    