print(chr(27)+'[2j')
print('\033c')
f = open('07.test', 'r')
f = open('07.input', 'r')
lines = [x.strip() for x in f.readlines()]
from dataclasses import dataclass
from functools import cache
from typing import Any
import hashlib

@dataclass
class Entry:
    name: str
    absolute_path: str
    type: str
    size: int
    children: list 
    parent: Any

    # For caching in size-calculations.
    def __hash__(self) -> int:
        # Generate a string of numbers from the absolute_path & children-count
        seed = self.absolute_path + str(len(self.children))
        h = int(hashlib.sha1(seed.encode("utf-8")).hexdigest(), 16)
        return h 

root = Entry("/", "/", "dir", 0, [], None)
current = root

i = 0
while i < len(lines):
    line = lines[i]
    # print(i+1, line, "(pwd: %s)" % current.absolute_path)
    if line.startswith('$ cd /'):
        current = root;
        i += 1
    elif line.startswith('$ cd ..'):
        current = current.parent;
        i += 1
    elif line.startswith('$ cd '):
        dirname = line[5:]
        for child in current.children:
            if child.name == dirname:
                current = child
                break
        i += 1
    elif line.startswith('$ ls'):
        i += 1
        while i < len(lines) and not lines[i].startswith(('$')):
            line = lines[i]
            # print('LS: ', i+1, line)
            if line.startswith('dir'):
                name = line.split(' ')[1]
                childnames = [x.name for x in current.children]
                if name not in childnames:
                    current.children.append(Entry(
                        name,
                        current.absolute_path + name + "/",
                        'dir',
                        0,
                        [], 
                        current
                    ))
            else:
                size, name = line.split(' ')
                childnames = [x.name for x in current.children]
                if name not in childnames:
                    current.children.append(Entry(
                        name,
                        current.absolute_path + name + "/",
                        'file',
                        int(size),
                        [], 
                        current
                    ))
            i += 1
    
calc = 0
@cache
def get_size(curr: Entry):
    global calc
    calc += 1
    print("calc", calc)
    size = curr.size
    for child in curr.children:
        if child.type == 'dir':
            size += get_size(child)
        if child.type == 'file':
            size += child.size
    return size

tot = 0
sizes = []
def parse_tree(curr: Entry, indent: int, print_tree: bool = False):
    global tot, sizes
    # Get size
    size = get_size(curr)
    is_dir = curr.type == 'dir'

    # part 1
    if is_dir and size < 100000:
        tot += size
    # part 2
    if is_dir:
        sizes.append(size)

    # Print for debugging
    if print_tree:
        print(
            '  '*indent, 
            "- %s" % curr.name, 
            "(%s)" % curr.type,
            size,
        )
    # Recursion
    for child in curr.children:
        parse_tree(child, indent+1)
parse_tree(root, 0)

print('Solution part 1:', tot)

used = get_size(root)
total_disk_space = 70000000
disk_space_left = total_disk_space - used
disk_space_needed = 30000000
space_to_delete = disk_space_needed - disk_space_left
sizes = sorted(sizes)
for s in sizes:
    if s > space_to_delete:
        print("Solution part 2:", s)
        break
