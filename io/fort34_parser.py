import re


class Fort34Parser:
    def __init__(self, file_content: str):
        self.__content = file_content.split('\n')

    def parse_file(self):
        cell = []
        for line in self.__content:
            coord_match = re.findall(r'(-?\d?\.?\d+)+', line)
            if len(coord_match) == 4:
                atom = int(coord_match[0])
                atom_x = float(coord_match[1])
                atom_y = float(coord_match[2])
                atom_z = float(coord_match[3])
                atom_coords = [atom_x, atom_y, atom_z]
                print(atom, atom_coords)

