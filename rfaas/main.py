#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '...'
__author__ = '...'
"""
import os
import time
import logging

# 使用logging打印出结果
logging.basicConfig(format='%(asctime)s--%(filename)s[line:%(lineno)d]--%(levelname)s: %(message)s',
                    level=logging.DEBUG, filename='parserTopMetric.log', filemode='a')


def parseTop(pid_name):
    cpu_index = 0
    mem_index = 0
    while True:
        text = os.popen('top -bi -n 2 -d 0.02').read().split('\n\n')
        mem_text = text[0].split('\n')[
            3]  # 获取KiB Mem 的值 ---->KiB Mem :6384865+total, 12354860+free, 18582268 used, 12171778+buff/cache
        swap_text = text[0].split('\n')[4]  # 获取交换内存的值
        pid_text = text[1].split('\n')
        logging.info("当前内存使用情况为：%s" % mem_text)
        logging.info("当前交换内存使用情况为：%s" % swap_text)
        for i in range(len(pid_text)):  # type(pid_text[i])--str
            pid_text[i] = [p for p in pid_text[i].split(' ') if p]
            if pid_text[i][-1] == pid_name:  # 被监控的进程名
                target_pid = pid_text[i]
                cpu_index = target_pid[-4]  # 获取被监控进程的cpu使用率
                mem_index = target_pid[-3]  # 获取被监控进程的内存使用率
        return float(cpu_index), float(mem_index)


# 获取150s内的cpu及内存使用率的最大值
def max_index(top):
    cpu_data = []
    mem_data = []
    for i in range(30):
        cpu_index, mem_index = parseTop(top)
        cpu_data.append(cpu_index)
        mem_data.append(mem_index)
        # time.sleep(5)
    print(cpu_data, mem_data)
    return max(cpu_data), max(mem_data)


# 获取150s内的cpu及内存使用率的平均值
def average_index(top):
    cpu_data = []
    mem_data = []
    for i in range(30):
        cpu_index, mem_index = parseTop(top)
        cpu_data.append(cpu_index)
        mem_data.append(mem_index)
        # time.sleep(5)
    print(cpu_data, mem_data)
    ave_cpu = sum(cpu_data) / len(cpu_data)
    ave_mem = sum(mem_data) / len(mem_data)
    return ave_cpu, ave_mem


if __name__ == '__main__':
    process = "kube-apiserver"
    max_cpu, max_mem = max_index(process)
    ave_cpu, ave_mem = average_index(process)
    logging.info("监控进程%s的cpu使用率的最大值为: %.2f" % process)
    logging.info("监控进程%s的内存使用率的最大值为: %.2f" % process)
    logging.info("监控进程%s的cpu使用率的平均值为: %.2f" % process)
    logging.info("监控进程%s的cpu使用率的最大值为: %.2f" % process)
