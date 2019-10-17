from __future__ import annotations
import argparse
from dataclasses import dataclass
import linecache
from pathlib import Path
from typing import List, Tuple


parser = argparse.ArgumentParser(description='Auto outlines generator')
parser.add_argument('directory',
                    type=str,
                    help='directory')
parser.add_argument('-o',
                     '--output',
                     type=str,
                     nargs='?',
                     help='Path to output')


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
        return linecache.getline(str(self.path.resolve()), 1)

    def to_str(self, indent: int = 0) -> str:
        return f'{"  "*indent}- [{self.get_title()}](./{self.rel_path()})'


class Directory(Node):

    @property
    def children(self) -> List[Node]:
        return [Directory(path, root=self.root) if path.is_dir()
                else File(path, root=self.root)
                for path in self.path.iterdir()
                if path.name != 'README.md']

    def get_title(self) -> str:
        return File(self.path.joinpath('README.md'), root=self.root).get_title()

    def to_str(self, indent: int = 0) -> str:
        children_strs: List[str] = [child.to_str(indent=indent+2)
                                    for child in self.children]
        s: str = f'{"  "*indent}- [{self.get_title()}](./{self.rel_path()})'
        s += '\n'
        s += '\n'.join(children_strs)
        return s


if __name__ == '__main__':
    args = parser.parse_args()
    dirpath: Path = Path(args.directory[0])
    assert dirpath.is_dir(), f'{dirpath} is not a directory'
    directory: Directory = Directory(dirpath, root=dirpath)

    outfile: str = args.output
    if outfile is None:
        print(directory.to_str())
    else:
        with open(outfile, 'w') as fout:
            fout.write(directory.to_str())
