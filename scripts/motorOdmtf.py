#!/usr/bin/env python
#encoding: utf8
import rospy 
from std_srvs.srv import Trigger,TriggerResponse
from raspi_ros.msg import MotorFreq
from geometry_msgs.msg import Twist
import math

def srvCallbackOn(srv):    ##srvがないとerror processing request: srvCallback() takes no arguments (1 given)
    print("----------------------")
    print("Called srvCallbackOn() func")
    res = TriggerResponse()

    ## ------- 例外処理で書き直す--------
    with open("/dev/rtmotoren0","w") as w:
        w.write("1\n")  ##1でも可
    res.success = True
    res.message = "motor_on"
    ## --------------------
    return res    ##returnでTriggerresponseを返さないとservice cannot process request: service handler returned None

def srvCallbackOff(srv):
    print("----------------------")
    print("Called srvCallbackOff() func")
    res = TriggerResponse()
    with open("/dev/rtmotoren0","w") as w:
        w.write("0\n")  ##1でも可

    # ----------try expectを用いて検証---------------
    ##with open("/dev/rtmotor0","w") as w:
        ##w.write("%d %d" % (0,0))   ##うまく行かない（ここで処理がとまる）
    # ---------------------------------------------
    with open("/dev/rtmotor_raw_l0","w") as w:
        w.write("0\n")
    with open("/dev/rtmotor_raw_r0","w") as w:
        w.write("0\n")
    res.success = True
    res.message = "motor_off"
    return res

def callBackFreq(msg):
    left_Freq = msg.wheelLeft
    right_Freq = msg.wheelRight
    ##with open("/dev/rtmotor0","w") as w:
        ##w.write("%d %d" % (left_Freq,right_Freq)) ## 2回目に呼び出されたときにうまく動かなかった
    with open("/dev/rtmotor_raw_l0","w") as w:
        w.write("%d" % left_Freq) 
    with open("/dev/rtmotor_raw_r0","w") as w:
        w.write("%d" % right_Freq)  
    return 0

def callBackCmdvel(msg):
    vel_x = msg.linear.x
    rot_z = msg.angular.z
    r = 0.0225
    left_Freq = (400 / (2*math.pi*r))*vel_x - (400 / math.pi)*rot_z 
    right_Freq = (400 / (2*math.pi*r))*vel_x + (400 / math.pi)*rot_z
    with open("/dev/rtmotor_raw_l0","w") as w:
        w.write("%d" % left_Freq) 
    with open("/dev/rtmotor_raw_r0","w") as w:
        w.write("%d" % right_Freq)  
    return 0

if __name__ == "__main__":
    rospy.init_node("Motors")
    srvs_on = rospy.Service("motor_on",Trigger,srvCallbackOn)
    srv_off = rospy.Service("motor_off",Trigger,srvCallbackOff)   ##srv_offが無くても動く
    sub_ferq = rospy.Subscriber("motorFreq",MotorFreq,callBackFreq)
    sub_vel = rospy.Subscriber("motorCmdvel",Twist,callBackCmdvel)
    print("Service Server start!")
    rospy.spin()