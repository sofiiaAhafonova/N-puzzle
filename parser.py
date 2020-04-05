def parse(filename):
    res = []
    lines = read(filename)
    lines = delete_comments(lines)
    if not lines[0].isdecimal:
        raise Exception('Error: first line must contain puzzle size and nothing else')
    size = int(lines[0])
    if len(lines) != size + 1:
        raise Exception(f'Error: puzzle contains {len(lines) - 1} raws, must be {size}')
    for index, l in enumerate(lines[1:]):
        elements = l.split(' ')
        res.extend(check_line(elements, size, index))
    if len(set(res)) != len(res):
        raise Exception('Error: duplicate numbers in puzzle')
    # return [res[i * size: size + size * i] for i in range(size)]
    return res, size


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
        raise Exception(f'Error: line {l_idx} contains {len(line)} elements, must be {size}')
    res = []
    for index, el in enumerate(line):
        try:
            el = int(el)
        except ValueError as e:
            raise ValueError(f'Error: line {l_idx} element {index}')
        if 0 > el > max_el:
            raise Exception(f'Error: line {l_idx} element {index}')
        res.append(el)
    return res
