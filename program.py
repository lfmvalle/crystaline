from initializer import Initializer
from file import File
from fort34_parser import Fort34Parser
from band_parser import BandParser
from band_plot import BandPlot
from doss_parser import DOSSParser


class Program:
    def __init__(self):
        self.print_logo()
        self.initializer = Initializer()
        self.file = File(self.initializer.get_fullpath())

    @staticmethod
    def print_logo():
        """
        Prints the c_ logo
        """
        # font styles used
        from colors import FontStyle
        blue_bold = FontStyle().color('blue').style('bold')
        blue = FontStyle().color('blue')
        cyan_bold = FontStyle().color('cyan').style('bold')
        cyan = FontStyle().color('cyan')
        nocolor = FontStyle()

        # print stylized logo
        logo = [
            f'{blue_bold} ______{nocolor}',
            f'{blue_bold}/\  ___\\{nocolor}',
            f'{blue_bold}\ \ \____   {cyan_bold} ______{nocolor}',
            f'{blue_bold} \ \_____\\  {cyan_bold}/\_____\\{nocolor}',
            f'{blue_bold}  \/_____/  {cyan_bold}\/_____/{nocolor}',
            f'{blue}C r y s t a {cyan}L i n e{nocolor}\n'
        ]

        for line in logo:
            print(f'\t{line}')

    def execute(self):
        """
        Execute c_
        """

        # get filename
        filename = self.file.name

        # file is fort.34
        if filename.endswith('.34'):
            print(f'Parsing fort.34')
            parser = Fort34Parser(self.file.content)
            parser.parse_file()
            return

        # file is BAND.DAT
        if 'BAND' in filename:
            print(f'Parsing BAND.DAT')
            parser = BandParser(self.file.content)
            parsing_results = parser.parse_file()
            print(f'Plotting Electronic Band Structure and generating images')
            for i in parsing_results:
                band = BandPlot(*i)
                band.create_graph()
            return

        # file is DOSS.DAT
        if 'DOSS' in filename:
            print(f'Parsing DOSS.DAT')
            parser = DOSSParser(self.file.content)
            parsing_results = parser.parse_file()
            print(f'Plotting DOSS')
            return
