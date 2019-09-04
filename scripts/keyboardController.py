#!/usr/bin/env python
#encoding: utf8

import rospy 
from geometry_msgs.msg import Twist
import math
from std_srvs.srv import Trigger

if __name__ == "__main__":
    rospy.init_node("KeyBoardController")
    pub = rospy.Publisher("motorCmdvel",Twist,queue_size=10)
    ##m = Twist()    ##ここにかくとwhileの中のmが更新されず累積する
    ##rate = rospy.Rate(10)
    '''
    print("----Enter key------")
    while True:
        val = raw_input("Enter key : ")
        print("keyboard input is : %s" % val)
        if val == "d":
            print("keyboard input is shutdown")
            break
        rospy.spin()    
    '''
    while not rospy.is_shutdown():
        m = Twist()
        val = raw_input("Enter key : ")
        ##print("keyboard input is : %s" % val)
        if val == "exit":
            print("KeyBoard input exit")
            break
        if val == "on":
            rospy.wait_for_service("motor_on")
            try:
                srv = rospy.ServiceProxy("motor_on",Trigger)
                on = srv()  ##ここで実際にサービス要請
                print(on.success)    ##ここの書式をどうにかする
                print("[message] : %s" % on.message)
                print("-----MotorON------")
            except rospy.ServiceException as e:
                print("Service call failed :%s" % e)
        if val == "off":
            rospy.wait_for_service("motor_off")
            try:
                srv = rospy.ServiceProxy("motor_off",Trigger)
                on = srv()  ##ここで実際にサービス要請
                print(on.success)
                print("[message] : %s" % on.message)
                print("-----MotorOFF------")
            except rospy.ServiceException as e:
                print("Service call failed :%s" % e)
        if val == "w":
            m.linear.x = 0.125  ##デバイスファイルには一度書き込まれると上書きするまで残るので動き続ける
            pub.publish(m)
        if val == "s":
            m.linear.x = -0.125
            pub.publish(m)
        if val == "d":
            m.angular.z = math.pi / 2
            pub.publish(m)
        if val == "a":
            m.angular.z = - math.pi / 2
            pub.publish(m)
        if val == "q":
            m.linear.x = 0.0
            m.angular.z = 0.0
            pub.publish(m)

    