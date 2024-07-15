class FontStyle:
    def __init__(self):
        self.__color = '0'
        self.__style = '0'
        self.__style_string = f'\033[0;0m\033[{self.style};{self.color}m'

    def color(self, color: str = 'none'):
        color_case = {'none': '0',
                      'gray': '90',
                      'red': '91',
                      'green': '92',
                      'yellow': '93',
                      'blue': '94',
                      'purple': '95',
                      'cyan': '96',
                      'white': '97'}
        new_color = color_case.get(color)
        self.__color = new_color if new_color is not None else '0'
        return self

    def style(self, style: str = 'none'):
        style_case = {'none': '0',
                      'bold': '1',
                      'light': '2',
                      'italic': '3',
                      'underline': '4',
                      'blink': '5',
                      'blink_light': '6',
                      'inverse': '7',
                      'hidden': '8',
                      'stroke': '9'}
        new_style = style_case.get(style)
        match new_style:
            case None:
                pass
            case '0':
                self.__style = new_style
            case _:
                if self.__style == '0':
                    self.__style = new_style
                else:
                    self.__style += f';{new_style}'
        return self

    def __create_style_string(self):
        self.__style_string = f'\033[0;0m\033[{self.__style};{self.__color}m'

    def wrap(self, text: str) -> str:
        self.__create_style_string()
        return f'{self.__style_string}{text}\033[0;0m'

    def __str__(self):
        self.__create_style_string()
        return self.__style_string
