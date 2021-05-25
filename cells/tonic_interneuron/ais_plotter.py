from matplotlib import pyplot
import matplotlib.gridspec as gridspec
import calendar, time, math

def my_plotter(cell, data_x, data_y, data_header, data_legend):
    '''Dynamic plotter'''
    def do_plot(ax, data_x_row, data_y_row, data_header_item, data_legend_item):
        ax.plot(data_x_row, data_y_row, color='m')
        ax.set_title("AIS Distance(mu): {}".format(data_header_item),fontsize=12)
        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Potential (mV)')
        ax.axhline(data_legend[i], label="Rheobase: {}".format(data_legend_item), color="r")
        ax.legend(prop={'size': 6})
        pyplot.gca().spines['top'].set_visible(False)
        pyplot.gca().spines['right'].set_visible(False)
    N = len(data_x)
    cols = 4
    rows = int(math.ceil(N / (cols - 1)))
    k = 0
    gs = gridspec.GridSpec(rows, cols, wspace=0.3, hspace=0.7, width_ratios=[1]*(cols-1)+[5])

    #Add component plot
    fig = pyplot.figure(figsize=(16, 10))
    for i in range(cols):
        for j in range(rows):
            if k<=len(data_x)-1:
                ax = fig.add_subplot(gs[j, i])
                do_plot(ax, data_x[k], data_y[k], data_header[k], data_legend[k])
                k+=1

    #Add Summarizing Plot
    new_ax = fig.add_subplot(gs[0:, -1])
    new_ax.scatter(data_header, data_legend)
    new_ax.plot(data_header, data_legend)
    new_ax.set_title("Rheobase (pA) vs AIS Distance(mu):", fontsize=16)
    new_ax.set_xlabel('AIS Distance (mu)')
    new_ax.set_ylabel('Rheobase (pA)')
    for x, y in zip(data_header, data_legend):
        if y is None:
            continue
        label = "({},{})".format(x, y)
        new_ax.annotate(label,  # this is the text
                        (x, y),  # this is the point to label
                        textcoords="offset points",  # how to position the text
                        xytext=(0, 10),  # distance from text to points (x,y)
                        ha='center', fontsize=6)  # horizontal alignment can be left, right or center
    txt = "Simplified Cell Model: Dendrite Length {}, Dendrite Ra {}, Spacer Ra {}, Dendrite Rm {}, Spacer Rm {} Dendrite Cm {}, Spacer Cm {}, Dendrite g_pas {}, Spacer g_pas {} "
    pyplot.figtext(0.5, 0.01, txt.format(cell.dend.L, cell.dend.Ra, cell.spacer.Ra, 1/cell.dend.g_pas, 1/cell.spacer.g_pas, cell.dend.cm, cell.spacer.cm, cell.dend.g_pas, cell.spacer.g_pas), wrap=True, horizontalalignment='center',
                   fontsize=12, bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5})
    # Save graph
    gmt = time.gmtime()
    # ts stores timestamp
    ts = calendar.timegm(gmt)
    pyplot.savefig(
        'graphs/passive/simulation_plot_{}.png'.format(str(ts)), dpi=300)
    # pyplot.show()

def summary_plotter(data_x, data_y, data_header):
    fig, axes = pyplot.subplots(nrows=2, ncols=6, figsize=(20, 6))
    for i, ax in enumerate(axes.flatten()):
        ax.plot(data_x[i], data_y[i], color='m')
        ax.set_title("AIS Distance(mu): {}".format(data_header[i]))
        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Potential (mV)')
        ax.legend(prop={'size': 6})