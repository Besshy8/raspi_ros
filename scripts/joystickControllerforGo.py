#!/usr/bin/env python
#encoding: utf8
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist 
import math
from std_srvs.srv import Trigger
from std_msgs.msg import Empty

def joyToCmdvel(msg):
    m = Twist()
    emp = Empty()
    if msg.buttons[4] == 1:
        motor_on.publish(emp)
    elif msg.buttons[5] == 1:
        motor_off.publish(emp)
    elif msg.buttons[0] == 1:
        m.angular.z = math.pi / 2
        pub.publish(m)
    elif msg.buttons[1] == 1:
        m.linear.x = -0.125
        pub.publish(m)
    elif msg.buttons[2] == 1:
        m.angular.z = -math.pi / 2
        pub.publish(m)
    elif msg.buttons[3] == 1: ##elifにしないと最後のif-elseしか見てくれない
        m.linear.x = 0.125
        pub.publish(m)
    else:
        m.linear.x = 0.0     #この部分でmotor_onoffの時にtopicも送信してしまうためオドメトリが計算されてしまう
        m.angular.z = 0.0
        pub.publish(m)
           
        
if __name__ == "__main__":
    rospy.init_node("JoyStickController")
    pub = rospy.Publisher("motorCmdvel",Twist,queue_size=10)
    motor_on = rospy.Publisher("motor_on_ByMSG",Empty,queue_size=10)
    motor_off = rospy.Publisher("motor_off_ByMSG",Empty,queue_size=10)
    sub = rospy.Subscriber("joy",Joy,joyToCmdvel)
    rospy.spin()