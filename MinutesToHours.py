#!/usr/bin/env python3

import sys

def Hours(minute):
    if minute < 0:
        raise ValueError('Input number cannot be negative')  # 抛出异常
    else:
        print('{} H, {} M'.format(int(minute / 60), minute % 60))

try:
    Hours(int(sys.argv[1]))  # sys.argv用于提取命令行参数，sys.argv[0]表示脚本名，参数从1开始
except:
    print('Parameter Error')  # 捕获异常，打印异常提示信息
