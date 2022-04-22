import shutil

from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = []

    def valid_extension(extension, self):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext: ".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

        class ResourceParser:
            extensions: [".jpg", ".png", ".gif", ".css", ".html"]
                                
