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
                spl = i.split(" ")  ##spaceで要素を区切った
            ##print(spl)
            d = [int(i) for i in spl]  ##文字列を整数にキャスト
            print("d[0]:%d,d[1]:%d,d[2]:%d,d[3]:%d" % (d[0],d[1],d[2],d[3]))
            rate.sleep()