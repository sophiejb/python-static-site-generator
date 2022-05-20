import re
from yaml import load_parser
from yaml import FullLoader
import Mapping.collections.abc


def class Content(self.mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
