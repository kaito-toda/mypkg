#!/usr/bin/env python3
#SPDX-License-Identifier: GPL-3.0
#
# Copyright (C) 2020 KaitoToda + RyuichiUeda.  All rights reserved.
#
import rospy
from std_msgs.msg import Int32

val = 1 
val_t = 1000
n = 1
c = 0
def cb(message):
    global n
    n = message.data

if __name__ == '__main__':
    rospy.init_node('conver')
    sub = rospy.Subscriber('count_up',Int32,cb)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        if c > 100:
            rate = rospy.Rate(10)
            if c > 200:
                rate = rospy.Rate(20)
        if val < val_t:
            print(val ,'+', n , end='=')
            val = val + n
            print(val,end='   ')
            c += 1
        elif val > val_t:
            print(val ,'-', n , end='=')
            val = val - n
            print(val,end='   ')
            c += 1
        elif val == val_t:
            c += 1
            print(c,"回目で成功")
            break
        print(c ,"回目")
        rate.sleep()
