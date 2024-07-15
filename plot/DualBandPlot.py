import matplotlib.figure
import matplotlib.pyplot as plt
import numpy as np

from unit_conversion import *


class DualPlot:
    def __init__(self, energy_data, alpha_band, beta_band, alpha_doss, beta_doss):
        self.y = energy_data
        self.x1 = alpha_band
        self.x2 = alpha_doss
        self.x3 = beta_doss
        self.x4 = beta_band
        self.fig, self.axs = plt.subplots(1, 4, sharey=True)

    def JUST_DO_IT___MAKE_YOUR_DREAMS_COME_TRUE___DOOO_IIIIT(self):
        self.fig.set_size_inches(w=16*(1/2.54), h=12*(1/2.54), forward=False)
        self.axs[0].plot(self.x1)
        self.axs[1].plot(self.x2)
        self.axs[2].plot(self.x3)
        self.axs[3].plot(self.x4)
        for i in range(0, 4):
            self.axs[i].set(xlim=(0, 10), xticks=[0, 2.5, 5, 7.5, 10])
            self.axs[i].axhline(y=0, xmin=self.y.min(), xmax=self.y.max(), linewidth=1, color=(1, .25, .25))
            if i != 0:
                self.axs[i].tick_params(left=False)
            if i == 0 or i == 3:
                self.axs[i].set(xticklabels=['Γ', 'L', 'FB', 'T', 'Γ'])
                for n in [0, 2.5, 5, 7.5, 10]:
                    self.axs[i].axvline(x=n, ymin=self.y.min(), ymax=self.y.max(), linewidth=.5, color=(.25, .25, .25))
            else:
                self.axs[i].tick_params(bottom=False, labelbottom=False)
        self.fig.subplots_adjust(wspace=0.1)
        self.fig.savefig('matplotlib-test.png')


data_y = np.arange(0, 10, .5)
data_x1 = np.array(data_y)
data_x2 = data_x1 ** 2
data_x3 = - data_x1 ** 2
data_x4 = - data_x1

prot = DualPlot(data_y, data_x1, data_x2, data_x3, data_x4)
prot.JUST_DO_IT___MAKE_YOUR_DREAMS_COME_TRUE___DOOO_IIIIT()
