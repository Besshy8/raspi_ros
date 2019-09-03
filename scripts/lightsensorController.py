#!/usr/bin/env python
#encoding: utf8
import rospy
from raspi_ros.msg import LightSensors
from geometry_msgs.msg import Twist

def getLightsensor(msg):
    print("--------LightSensorsVal---------")
    print("Right_side : %d" % msg.r_side)
    print("Right_front: %d" % msg.r_front)
    print("Left_front : %d" % msg.l_front)
    print("Left_side  : %d" % msg.l_side)
    print("Sum        : %d" % msg.sum)
    print("Sum_forward: %d" % msg.sum_forward)

    m = Twist()
    if msg.sum_forward >= 100:
        m.linear.x = 0
        m.angular.z = 0
        pub.publish(m)     ## エラーは起こらないがコードの補完はない
    else:
        m.linear.x = 0.125
        pub.publish(m)

if __name__ == "__main__":
    rospy.init_node("LightSensorController")
    pub = rospy.Publisher("motorCmdvel",Twist,queue_size=10)
    sub = rospy.Subscriber("lightsensor_val",LightSensors,getLightsensor)
    rospy.spin()