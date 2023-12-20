from collections import deque
print(chr(27)+'[2j')
print('\033c')
f = open('20.test', 'r')
f = open('20.test2', 'r')
f = open('20.input', 'r')
lines = [x.strip() for x in f.readlines()]
RED = '\033[91m'
RESET = '\033[0m'


def parse(lines):
    modules = {}
    for line in lines:
        if line.startswith('broadcast'):
            _, outputs = line.split(' -> ')
            modules['broadcaster'] = ('B', 0, outputs.split(', '))
        else:
            module, outputs = line.split(' -> ')
            mod_type = module[0]
            module = module[1:]
            modules[module] = (mod_type, 0, outputs.split(', '))
    return modules


def populate_memory(modules):
    memory = {}
    for m in modules:
        mod_type, _, outputs = modules[m]
        if mod_type != '&':
            continue
        memory[m] = {}
    for m in modules:
        mod_type, _, outputs = modules[m]
        for o in outputs:
            if o in memory:
                memory[o][m] = 0
    return memory


def button_press(modules, memory, search=None):
    counts = [0, 0]
    search_found = False

    queue = deque([])
    queue.append(('BUTTON', 'broadcaster', 0))
    while queue:
        inputer, mod, pulse = queue.popleft()
        counts[pulse] += 1
        if mod not in modules:
            continue
        if mod == search:
            if pulse == 1:
                search_found = True
                queue.clear()
        mod_type, value, outputs = modules[mod]

        if mod_type == '%':
            if pulse == 1:
                continue
            value = 1 - value
            modules[mod] = (mod_type, value, outputs)
            for output in outputs:
                queue.append((mod, output, value))
        elif mod_type == '&':
            memory[mod][inputer] = pulse
            new_value = 0
            for i in memory[mod]:
                if memory[mod][i] == 0:
                    new_value = 1
                    break

            for output in outputs:
                queue.append((mod, output, new_value))
        elif mod_type == 'B':
            for output in outputs:
                queue.append((mod, output, 0))
        else:
            raise Exception('Unknown mod_type: %s' % mod_type)
    return counts, search_found


def solve1(lines):
    modules = parse(lines)
    memory = populate_memory(modules)
    counts = (0, 0)
    times = 1000
    for _ in range(times):
        new_counts, _ = button_press(modules, memory)
        counts = (counts[0] + new_counts[0], counts[1] + new_counts[1])
    return counts[0]*counts[1]


def solve2(lines):
    modules = parse(lines)
    memory = populate_memory(modules)
    cycles = modules['broadcaster'][2]
    iterations = []
    result = 1
    for cycle in cycles:
        modules['broadcaster'] = ('B', 0, [cycle])
        i = 0
        while True:
            i += 1
            if i % 10000 == 0:
                break
            _, only_one = button_press(modules, memory, 'lx')
            if only_one:
                result *= i
                break
        iterations.append(i)
    return result


print('Part 1:', solve1(lines))
print('Part 2:', solve2(lines))
