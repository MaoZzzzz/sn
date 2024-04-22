from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

color = ["#760304", "#770433", "#662354", "#493764", "#314263", "#2F4858", "#774400", "#6A6E0A"]
# color = ["#FF4500", "#FF0056", "#F40096", "#B934CC", "#3D5DED", "#006FEE", "#86AEE1"]
function_name = ["upload-creator-X86", "upload-creator-RISCV", "upload-user-mentions-X86", "upload-user-mentions-RISCV",
                 "post-storage-X86", "post-storage-RISCV", "upload-home-timeline-X86", "upload-home-timeline-RISCV",
                 "upload-user-timeline-X86", "upload-user-timeline-X86"]


def process_file(file_path):
    data = defaultdict(float)

    with open(file_path, 'r') as file:
        for line in file:
            if "StartTime&&EndTime" in line:
                end_time = float(line.split()[2])
                start_time = float(line.split()[1])
                duration = end_time - start_time
                data["total_time"] += duration
            else:
                parts = line.split()
                call = parts[1]
                duration = float(parts[-1])
                data[call] += duration

    return data


def calculate_percentage(data, total_time):
    percentages = {call: (time / total_time) * 100 for call, time in data.items()}
    return percentages


def main():
    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\upload-creator-X86.txt"
    data1 = process_file(file_path)
    total_time = data1["total_time"]
    percentages = calculate_percentage(data1, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\upload-creator-RISCV.txt"
    data2 = process_file(file_path)
    total_time = data2["total_time"]
    percentages = calculate_percentage(data2, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\upload-user-mentions-X86.txt"
    data3 = process_file(file_path)
    total_time = data3["total_time"]
    percentages = calculate_percentage(data3, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\upload-user-mentions-RISCV.txt"
    data4 = process_file(file_path)
    total_time = data4["total_time"]
    percentages = calculate_percentage(data4, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\post-storage-X86.txt"
    data5 = process_file(file_path)
    total_time = data5["total_time"]
    percentages = calculate_percentage(data5, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\post-storage-RISCV.txt"
    data6 = process_file(file_path)
    total_time = data6["total_time"]
    percentages = calculate_percentage(data6, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\upload-home-timeline-X86.txt"
    data7 = process_file(file_path)
    total_time = data7["total_time"]
    percentages = calculate_percentage(data7, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\upload-home-timeline-RISCV.txt"
    data8 = process_file(file_path)
    total_time = data8["total_time"]
    percentages = calculate_percentage(data8, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\upload-user-timeline-X86.txt"
    data9 = process_file(file_path)
    total_time = data9["total_time"]
    percentages = calculate_percentage(data9, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\upload-user-timeline-RISCV.txt"
    data10 = process_file(file_path)
    total_time = data10["total_time"]
    percentages = calculate_percentage(data10, total_time)
    for call, percentage in percentages.items():
        print(f"{call}: {percentage:.2f}%")

    # plot_stacked_bars([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10])
    plot_stacked_bars([data1, data3, data5, data7, data9])


def plot_stacked_bars(data_list):
    labels = list(data_list[0].keys())
    # positions = np.arange(len(labels))
    positions = np.ones(len(data_list[0]))
    bar_width = 0.8
    opacity = 0.8

    # function_name = ["upload-creator", "upload-user-mentions", "post-storage", "upload-home-timeline",
    #                  "upload-user-timeline"]

    function_name = ["UC", "UUM", "PS", "UHT", "UUT"]

    plt.figure(figsize=(4, 3))

    for data in data_list:
        total_time = data['total_time']
        del data['total_time']

        percentages = [value / total_time * 100 for value in data.values()]
        bottom = np.zeros(len(labels))

        plt.bar(positions[0], 100, width=bar_width, bottom=bottom, color="#E8E8E8", alpha=opacity)

        index = 0
        for label, percentage in zip(labels, percentages):
            plt.bar(positions, percentage, width=bar_width, bottom=bottom, color=color[index % (len(color))],
                    alpha=opacity)
            index += 1
            bottom += percentage

        positions = positions + 1

    plt.rcParams["font.sans-serif"] = ["Times New Roman"]
    plt.xticks(list(range(1, len(data_list) + 1)), function_name)
    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    plt.margins(x=0.01)

    plt.xlabel('系统调用名称', fontsize=13, fontproperties='Simsun')
    plt.ylabel('时间占比(%)', fontsize=13, fontproperties='Simsun')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(bottom=0.3, left=0.2)
    plt.savefig("system_call_percent.pdf")
    plt.show()


if __name__ == "__main__":
    main()
