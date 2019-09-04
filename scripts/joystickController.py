#!/usr/bin/env python
#encoding: utf8
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist 
import math
from std_srvs.srv import Trigger

def joyToCmdvel(msg):
    m = Twist()
    if msg.buttons[4] == 1:
        rospy.wait_for_service("motor_on")
        try:
            srv = rospy.ServiceProxy("motor_on",Trigger)
            on = srv()
            print("---------------------")
            print(on.success)
            print("[message]: %s" % on.message)
        except rospy.ServiceException as e:
            print("can't get service : %s" % e)
    elif msg.buttons[5] == 1:
        rospy.wait_for_service("motor_off")
        try:
            srv = rospy.ServiceProxy("motor_off",Trigger)
            off = srv()
            print("---------------------")
            print(off.success)
            print("[message]: %s" % off.message)
        except rospy.ServiceException as e:
            print("can't get service : %s" % e)
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
        m.linear.x = 0.0   
        m.angular.z = 0.0
        pub.publish(m)
           
        
if __name__ == "__main__":
    rospy.init_node("JoyStickController")
    pub = rospy.Publisher("motorCmdvel",Twist,queue_size=10)
    sub = rospy.Subscriber("joy",Joy,joyToCmdvel)
    rospy.spin()

    