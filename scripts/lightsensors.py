#!/usr/bin/env python
#encoding: utf8
import rospy


if __name__ == "__main__":
    rospy.init_node("lightsensors")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        with open("/dev/rtlightsensor0","r") as r:
            l = [s.rstrip() for s in r.readlines()] ##改行が含まれてしまうので取り除いた
            for i in l:
                spl = i.split(" ")
            print(spl)
            ##d = [int(i) for i in l]  ##文字列を整数にキャスト
            ##rospy.loginfo("d[0]:%d",d[0])
            #rospy.loginfo("l[0]:%s",l[0])
            rate.sleep()