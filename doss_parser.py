import re

class DOSSParser:
    def __init__(self, content: str):
        self.__content = content.split('\n')

    def parse_file(self):
        alpha_doss = None
        alpha_fermi = None
        beta_doss = None
        beta_fermi = None

        if not self.__content:
            raise IOError

        if len(self.__content) == 0:
            raise IOError

        for line in self.__content:
            a = re.compile(r'\d+.\d+')
            b = re.findall(a, line)
            print(b)
        return
