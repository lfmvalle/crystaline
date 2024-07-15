import matplotlib.pyplot as plt
import numpy as np


class BandPlot:
    def __init__(self, title: str, x: list, y: list, e_fermi: float, ticks: list, fill_between: list = None):
        self.title = title
        self.x = np.array(x)
        self.y = np.array(y) * 27.21138  # convert energy unit: Hartree -> eV
        self.fill_between = np.array(fill_between) * 27.21138
        self.e_fermi = e_fermi
        self.ticks = ticks

    def create_graph(self):
        # set font sizes
        plt.rc('axes', labelsize=12)
        plt.rc('xtick', labelsize=12)
        plt.rc('ytick', labelsize=12)

        plt.axes()
        # make graph
        fig, ax = plt.subplots()

        # plot
        for y in self.y:
            ax.plot(self.x, y, linewidth=.5, color=(0, 0, 0))

        # fill between
        if self.fill_between.nonzero():
            ax.fill_between(self.x, self.fill_between[0], self.fill_between[1],
                            linewidth=0, color=(.75, .75, .75), alpha=.5)

        # x-axis configuration
        ax.set(xlim=(self.x.min(), self.x.max()),
               xticks=self.ticks,
               xticklabels=['Γ', 'L', 'FB', 'T', 'Γ'])

        ax.set(ylabel='Energy (eV)',
               ylim=(self.y.min(), self.y.max()))

        # y-axis configuration

        # Fermi energy - horizontal line
        ax.axhline(y=self.e_fermi, xmin=self.x.min(), xmax=self.x.max(), linewidth=.5, color=(1, .25, .25))

        # symmetry points - vertical lines
        for tick in self.ticks:
            ax.axvline(x=tick, ymin=self.y.min(), ymax=self.y.max(), linewidth=.5, color=(0, 0, 0))

        # save figure
        # plt.figure(num=1, figsize=(102, 8), dpi=300)
        plt.savefig(f'band-{self.title}.png')

        # show graph - requires PyQT6 library to be installed
        plt.show()
