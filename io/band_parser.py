import re
import numpy as np
import unit_conversion


class BandParser:
    def __init__(self, file_content: str):
        self.content = file_content.split('\n')

    def parse_file(self):
        title = ''
        plots = []
        ticks = []
        results = []
        for line in self.content:
            # get title
            title_match = re.findall(r'"\w+"', line)
            if title_match:
                title = title_match[0].replace('\"', '')
                print('Found plot:', title)

            # get ticks
            tick_match = re.findall(r'(@.+TICK.+,\s+\d+.\d+)', line)
            if tick_match:
                tick = re.findall(r'\d+.\d+', tick_match[0])
                ticks.append(float(tick[0]))

            # get data range
            data_range = re.findall(r'(-?\d+\.\d+E[+-]?\d+)+', line)
            if len(data_range) > 2:  # TODO: this check is a bad habit... must be avoided
                for n, data in enumerate(data_range):
                    data_range[n] = float(data_range[n])
                plots.append(data_range)

            # get Fermi Energy
            e_fermi_match = re.findall(r'# EFERMI.+\d+', line)
            if e_fermi_match:
                e_fermi = re.findall(r'-?\d+.\d+', e_fermi_match[0])
                e_fermi = float(e_fermi[0])
                print('Fermi Energy (Hartree):', e_fermi)
                print(f'{"(eV):":>23s}', round(unit_conversion.hartree_to_ev(e_fermi), 3))

                # end of first band data, save results and reset temporary lists
                np_plots = np.array(plots)
                np_plots = np_plots.transpose().tolist()

                x = np_plots[0]
                y = np_plots[1:]

                fill_between = []
                # if the number of plots is even
                if len(y) % 2 == 0:
                    # assuming number of VBs = number of CBs
                    cb = int(len(y)/2)  # first conduction band is N/2
                    vb = int(cb - 1)  # last valence band N/2 - 1
                    fill_between = [y[vb], y[cb]]

                print(f'Electronic Band Structure along {len(ticks)} symmetry points:')
                results.append((title, x, y, e_fermi, ticks, fill_between))
                title = ''
                plots = list()
                ticks = list()

        return results
