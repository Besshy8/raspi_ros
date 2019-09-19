#!/usr/bin/env python
#encoding: utf8
import rospy
from geometry_msgs.msg import Twist
from raspi_ros.msg import GoTwist 

def transformMSG(msg):
    mes = GoTwist()
    mes.linear_x = msg.linear.x
    mes.angular_z = msg.angular.z
    pub.publish(mes)

if __name__ == "__main__":
    rospy.init_node("TransformMSG")
    sub = rospy.Subscriber("motorCmdvel",Twist,transformMSG)
    pub = rospy.Publisher("GoCmdvel",GoTwist,queue_size=10)
    rospy.spin()