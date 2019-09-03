#!/usr/bin/env python
#encoding: utf8
import rospy
from raspi_ros.msg import LightSensors

def getLightsensor(msg):
    print("--------LightSensorsVal---------")
    print("Right_side : %d" % msg.r_side)
    print("Right_front: %d" % msg.r_front)
    print("Left_front : %d" % msg.l_front)
    print("Left_side  : %d" % msg.l_side)
    
if __name__ == "__main__":
    rospy.init_node("LightSensorController")
    sub = rospy.Subscriber("lightsensor_val",LightSensors,getLightsensor)
    rospy.spin()