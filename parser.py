import numpy as np


def parse(filename):
    res = np.array([])
    lines = read(filename)
    lines = delete_comments(lines)
    if not lines[0].isdecimal:
        raise Exception('Error: first line must contain puzzle size and nothing else')
    size = int(lines[0])
    if len(lines) != size + 1:
        raise Exception('Error: puzzle contains {0} raws, must be {1}'.format(len(lines) - 1, size))
    for index, l in enumerate(lines[1:]):
        elems = l.split(' ')
        check_line(elems, size, index)
        res = np.append(res, np.array(elems), axis=0)
    if len(np.unique(res)) != len(res):
        raise Exception('Error: duplicate numbers in puzzle')
    res = np.reshape(res, (size, size))
    return res


def read(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().splitlines()
    except Exception:
        raise Exception('Error: opening file')


def delete_comments(lines):
    res = []
    for l in lines:
        if '#' in l:
            l = l.split('#')[0]
        if len(l) > 0:
            res.append(l)
    return res


def check_line(line, size, l_idx):
    max_el = size**2 - 1
    if len(line) != size:
        raise Exception('Error: line {0} contains {1} elements, must be {2}'.format(l_idx, len(line), size))
    for index, el in enumerate(line):
        if not(el.isdecimal() and 0 <= int(el) <= max_el):
            raise Exception('Error: line {0} element {1}'.format(l_idx, index))
