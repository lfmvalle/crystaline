import os
import sys


class Initializer:
    def __init__(self):
        self.__file = None

        # file validation
        match len(sys.argv):
            case 2:
                self.__file = os.path.join(os.getcwd(), sys.argv[1])
                if not os.path.exists(self.__file):
                    raise FileNotFoundError(f'File \'{sys.argv[1]}\' was not found.')
                if not os.path.isfile(self.__file):
                    raise IOError(f'Path \'{self.__file}\' does not point to a file.')
            case _:
                raise IOError(f'Invalid number of arguments on script call.')

    def get_fullpath(self) -> str:
        return self.__file
