from __future__ import annotations
from dataclasses import dataclass
import linecache
from pathlib import Path
import re
from typing import List, Tuple


@dataclass
class Node:
    """Treenode"""
    path: Path
    root: Path

    def get_title(self) -> str:
        raise NotImplementedError('Abstract.')

    def to_str(self, indent: int = 0) -> str:
        raise NotImplementedError('Abstract.')

    def rel_path(self) -> Path:
        return self.path.relative_to(self.root)


class File(Node):

    def get_title(self) -> str:
        return linecache.getline(str(self.path.resolve()), 1)[:-1]

    def to_str(self, indent: int = 0) -> str:
        return f'{"  "*indent}- [{self.get_title()}](./{self.rel_path()})'


class Directory(Node):

    @property
    def children(self) -> List[Node]:
        return self.get_file_children() + self.get_dir_children()

    def get_file_children(self) -> List[File]:
        return [File(path, root=self.root)
                for path in sorted(list(self.path.glob('*')))
                if (not path.is_dir()) and (path.suffix == '.md') and (path.name != 'README.md')]

    def get_dir_children(self) -> List[Directory]:
        return [Directory(path, root=self.root)
                for path in sorted(list(self.path.glob('*')))
                if (path.is_dir()) and (re.match('^[A-Z]+$', path.name))]

    def get_title(self) -> str:
        return File(self.path.joinpath('README.md'), root=self.root).get_title()

    def to_str(self, indent: int = 0) -> str:
        children_strs: List[str] = [child.to_str(indent=indent+2)
                                    for child in self.children]
        s: str = f'{"  "*indent}- [{self.get_title()}](./{self.rel_path()})'
        if len(children_strs) > 0:
            s += '\n'
            s += '\n'.join(children_strs)
        return s

    def write_to_readme(self, fake: bool = False) -> None:
        if not fake:
            with open(self.path.joinpath('README.md'), 'w') as fout:
                fout.write(self.to_str())
        else:
            print(self.to_str())
        for child in self.get_dir_children():
            child.write_to_readme(fake=fake)


if __name__ == '__main__':
    dirpath: Path = Path(__file__).resolve().parent.parent
    directory: Directory = Directory(dirpath, root=dirpath)
    directory.write_to_readme(fake=True)
