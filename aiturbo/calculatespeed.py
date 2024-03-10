import os
import sys


def one_speed(filepath):
    temp = []
    step = []
    with open(filepath, "r", encoding='utf-8') as file:
        b = -1
        c = b
        for line in file:
            line = line.strip('\n')
            a = line.split(" ")
            c = b
            b = a[1]
            if b != c:
                step.append(a[1])
                temp.append(a[0])

    speed_lists = []
    # print(temp)
    del temp[0]
    del step[0]
    del temp[0]
    del step[0]
    for i in range(len(step)):
        step1 = step[len(step) - 1 - i]
        step2 = step[len(step) - 2 - i]
        temp1 = temp[len(step) - 1 - i]
        temp2 = temp[len(step) - 2 - i]
        speed_lists.append((float(step2) - float(step1)) / (float(temp2) - float(temp1)))
    # print(speed_lists)
    average_speed = sum(speed_lists) / len(speed_lists)
    return average_speed


if __name__ == '__main__':
    # one_speed()
    dir_path = 'D:\\Workdir\\pycharm\\Draw\\ll\\'
    file_list = os.listdir(dir_path)
    speed_list = []
    for i in range(len(file_list)):
        file_path = dir_path + file_list[i]
        print(file_path)
        speed_list.append(one_speed(file_path))

    print(speed_list)
