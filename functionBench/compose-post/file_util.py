import os
import re

FILE_PATH_PREFIX = "D:\\Workdir\\pycharm\\sn\\functionBench\\compose-post\\data"


def get_file_path():
    riscv_file_name_b = ""
    riscv_file_name_u = ""
    x86_file_name_b = ""
    x86_file_name_u = ""
    riscv_files = os.listdir(FILE_PATH_PREFIX + "\\riscv")
    x86_files = os.listdir(FILE_PATH_PREFIX + "\\x86")

    for str in riscv_files:
        tmp = str.split("-")
        if "b.txt" == tmp[3]:
            riscv_file_name_b = FILE_PATH_PREFIX + "\\riscv" + "\\" + str

        if "u.txt" == tmp[3]:
            riscv_file_name_u = FILE_PATH_PREFIX + "\\riscv" + "\\" + str

    for str in x86_files:
        tmp = str.split("-")
        if "b.txt" == tmp[3]:
            x86_file_name_b = FILE_PATH_PREFIX + "\\x86" + "\\" + str

        if "u.txt" == tmp[3]:
            x86_file_name_u = FILE_PATH_PREFIX + "\\x86" + "\\" + str

    return riscv_file_name_b, riscv_file_name_u, x86_file_name_b, x86_file_name_u


def read_file(type, arch):
    riscv_file_name_b, riscv_file_name_u, x86_file_name_b, x86_file_name_u = get_file_path()

    if type == "cpu" and arch == "riscv":
        f = open(riscv_file_name_u)
    if type == "io" and arch == "riscv":
        f = open(riscv_file_name_b)
    if type == "cpu" and arch == "x86":
        f = open(x86_file_name_u)
    if type == "io" and arch == "x86":
        f = open(x86_file_name_b)

    lines = f.readlines()

    user_result = []
    iowait_result = []
    idle_result = []
    bread_result = []
    bwrite_result = []
    for line in lines:
        tmp = line.split()
        if type == "cpu" and arch == "x86":
            if len(tmp) >= 9 and is_float_regex(tmp[3]):
                user_result.append(float(tmp[3]))
                idle_result.append(float(tmp[8]))
                iowait_result.append(float(tmp[5]))
        if type == "cpu" and arch == "riscv":
            if len(tmp) >= 8 and is_float_regex(tmp[2]):
                user_result.append(float(tmp[2]))
                idle_result.append(float(tmp[7]))
                iowait_result.append(float(tmp[5]))
        if type == "io" and arch == "x86":
            if len(tmp) >= 7 and is_float_regex(tmp[5]):
                bread_result.append(float(tmp[5]))
                bwrite_result.append(float(tmp[6]))
        if type == "io" and arch == "riscv":
            if len(tmp) >= 8 and is_float_regex(tmp[6]):
                bread_result.append(float(tmp[6]))
                bwrite_result.append(float(tmp[7]))

    if type == "cpu":
        return user_result, idle_result, iowait_result
    else:
        return bread_result, bwrite_result


def is_float_regex(s):
    return bool(re.match(r'^[-+]?[0-9]*\.?[0-9]+$', s))


if __name__ == '__main__':
    user_result, idle_result, iowait_result = read_file("cpu", "riscv")
    print(user_result)
    print(idle_result)
