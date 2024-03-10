# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    ai = "6086 5025 4736 2137 2330 4430 1526 1781 5603 1199"
    op = "2612 1200 1200 3229 868 2490 414 1440 2851 612"
    a = ai.split(" ")
    b = op.split(" ")

    suma = 0
    sumb = 0
    for i in range(len(a)):
        suma = suma + int(a[i])
    for i in range(len(b)):
        sumb = sumb + int(b[i])

    a = suma/10
    b = sumb/10
    print(suma/10)
    print(sumb/10)
    print(a/b)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
