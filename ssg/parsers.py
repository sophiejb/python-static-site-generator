import shutil

from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
  32
ssg/site.py
@@ -0,0 +1,32 @@
from pathlib import Path


class Site:
    def __init__(self, source, dest, parsers=None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            print("Not Implemented")

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)
