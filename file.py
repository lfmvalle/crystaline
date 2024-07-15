from colors import FontStyle
import os
import sys


class File:
    def __init__(self, filepath):
        self.__filepath = filepath
        self.__content = self.__get_content()

    @property
    def filepath(self):
        return self.__filepath

    @property
    def name(self) -> str:
        return os.path.basename(self.__filepath)

    @property
    def absolute_path(self) -> str:
        return os.path.abspath(self.__filepath)

    @property
    def directory(self) -> str:
        return os.path.dirname(os.path.realpath(self.__filepath))

    @property
    def content(self):
        return self.__content

    def __file_exists(self):
        if not os.path.exists(self.__filepath):
            raise FileNotFoundError

    def __get_content(self) -> str:
        self.__file_exists()
        with open(self.__filepath, 'r', encoding='utf-8') as file_object:
            return file_object.read()
