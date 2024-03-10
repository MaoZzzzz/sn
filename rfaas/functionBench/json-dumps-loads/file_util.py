import os
import re

FILE_PATH_PREFIX = "/rfaas/functionBench/json-dumps-loads/data"


def get_file_path():
    riscv_file_name_n = ""
    x86_file_name_n = ""
    riscv_files = os.listdir(FILE_PATH_PREFIX + "\\riscv")
    x86_files = os.listdir(FILE_PATH_PREFIX + "\\x86")

    for str in riscv_files:
        tmp = str.split("-")
        if "n.txt" == tmp[4]:
            riscv_file_name_n = FILE_PATH_PREFIX + "\\riscv" + "\\" + str

    for str in x86_files:
        tmp = str.split("-")
        if "n.txt" == tmp[4]:
            x86_file_name_n = FILE_PATH_PREFIX + "\\x86" + "\\" + str

    return riscv_file_name_n, x86_file_name_n


def read_file(type, arch):
    riscv_file_name_n, x86_file_name_n = get_file_path()

    if type == "net" and arch == "riscv":
        f = open(riscv_file_name_n)
    if type == "net" and arch == "x86":
        f = open(x86_file_name_n)

    lines = f.readlines()

    iseg_result = []
    oseg_result = []
    for line in lines:
        tmp = line.split()
        if type == "net" and arch == "riscv":
            if len(tmp) >= 5 and is_float_regex(tmp[4]):
                iseg_result.append(float(tmp[3]))
                oseg_result.append(float(tmp[4]))
        if type == "net" and arch == "x86":
            if len(tmp) >= 5 and is_float_regex(tmp[4]):
                iseg_result.append(float(tmp[3]))
                oseg_result.append(float(tmp[4]))

    return iseg_result, oseg_result


def is_float_regex(s):
    return bool(re.match(r'^[-+]?[0-9]*\.?[0-9]+$', s))


if __name__ == '__main__':
    iseg_result, oseg_result = read_file("net", "riscv")
    print(iseg_result)
    print(oseg_result)
