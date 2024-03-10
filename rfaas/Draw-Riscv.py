from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

latency = [[0 for i in range(2)] for j in range(10)]
labels = ['riscv', 'x86']
fn_name = ["compose-post", "upload-media", "upload-creator", "upload-text", "upload-user-mentions", "upload-unique-id",
           "compose-and-upload", "post-storage", "upload-user-timeline", "upload-home-timeline"]


def get_label(flag):
    for i in range(len(fn_name)):
        if flag == fn_name[i]:
            return i


def get_latency(line, file_num):
    latencies = line.split(" ")
    for i in range(len(latencies)):
        if latencies[i][:-1] in fn_name:
            latency[get_label(latencies[i][:-1])][file_num] += float(latencies[i + 1])
            continue


def read_file():
    filepath = ['./log/riscv.log', './log/x86.log']

    for i in range(len(filepath)):
        f = open(filepath[i])
        line = f.readline()
        while line:
            get_latency(line, i)
            line = f.readline()
        f.close()


def draw_latency():
    for i in range(len(latency)):
        for j in range(len(latency[i])):
            latency[i][j] = latency[i][j] / 3

    fig, ax = plt.subplots(2, 5, sharex='col', sharey='row')

    plt.figure(figsize=(25, 5))
    for i in range(0, 10):
        draw_subplot(i)

    plt.savefig('./both.png')
    plt.show()


def draw_subplot(i):
    plt.subplot(2, 5, i + 1)
    plt.scatter(labels, latency[i], s=50, color='green')
    plt.plot(labels,
             latency[i],
             color='blue',
             markersize=10,
             linewidth=3)
    plt.ylabel('Latency(ms)')
    plt.xlabel('CPU freq(GHz)')
    plt.grid()
    plt.tight_layout()
    plt.title(fn_name[i])


# def draw_latency():
#     for i in range(len(latency)):
#         for j in range(len(latency[i])):
#             latency[i][j] = latency[i][j] / 1
#
#     print(latency)
#
#     fig, ax = plt.subplots()
#     plt.scatter(labels, latency[0], s=50)
#     plt.ylabel('Latency(ms)', fontdict={'size': 18})
#     plt.xlabel('Type', fontdict={'size': 18})
#     plt.tick_params(labelsize=18)
#     # plt.xticks(rotation=60)
#
#     plt.plot(labels, latency[0], color='g', markersize=10, linewidth=3)
#     plt.grid()
#
#     plt.ylim((0, 1))
#     ymajorLocator = MultipleLocator(0.1)
#     ax.yaxis.set_major_locator(ymajorLocator)
#
#     plt.tight_layout()
#     plt.savefig('./cpu_freq_fne.png')
#     plt.show()


if __name__ == '__main__':
    read_file()
    draw_latency()
