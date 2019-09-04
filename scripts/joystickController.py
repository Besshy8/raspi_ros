#!/usr/bin/env python
#encoding: utf8
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist 
import math

def joyToCmdvel(msg):
    m = Twist()
    if msg.buttons[0] == 1:
        m.angular.z = -math.pi / 2
        pub.publish(m)
    if msg.buttons[1] == 1:
        m.linear.x = -0.125
        pub.publish(m)
    if msg.buttons[2] == 1:
        m.angular.z = math.pi / 2
        pub.publish(m)
    if msg.buttons[3] == 1:
        m.linear.x = 0.125
        pub.publish(m)

    
    '''
    else:
        m.linear.x = 0.0   ##最初におしたボタンしか反応しなかった
        m.angular.z = 0.0
        pub.publish(m)
    '''       
        
if __name__ == "__main__":
    rospy.init_node("JoyStickController")
    pub = rospy.Publisher("motorCmdvel",Twist,queue_size=10)
    sub = rospy.Subscriber("joy",Joy,joyToCmdvel)
    rospy.spin()

    