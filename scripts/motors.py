#!/usr/bin/env python
#encoding: utf8
import rospy 
from std_srvs.srv import Trigger,TriggerResponse
from raspi_ros.msg import MotorFreq

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

if __name__ == "__main__":
    rospy.init_node("Motors")
    srvs_on = rospy.Service("motor_on",Trigger,srvCallbackOn)
    srv_off = rospy.Service("motor_off",Trigger,srvCallbackOff)   ##srv_offが無くても動く
    sub = rospy.Subscriber("motorFreq",MotorFreq,callBackFreq)
    print("Service Server start!")
    rospy.spin()