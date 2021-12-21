#! /usr/bin/env python

import rospy


def main():
    rospy.init_node('move')
    
    rospy.spin()

if __name__ == '__main__':
    main()
