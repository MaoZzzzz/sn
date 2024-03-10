import matplotlib.pyplot as plt

f, axs = plt.subplots(ncols=2, sharex=True)

plt.xticks(range(6), [str(x) + "foo" for x in range(6)], rotation='45')

for i in range(2):
    ax = axs[i]
    ax.plot(range(6), range(6))

f.show()
