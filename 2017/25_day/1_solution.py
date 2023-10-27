print(chr(27)+'[2j')
print('\033c', end='')

lines = open('./25_day/input.txt').read().splitlines()
# lines = open('./25_day/test.txt').read().splitlines()

begin_state = lines[0][-2]
checksum_steps = int(lines[1].split()[-2])

states = {}
for i in range(3, len(lines), 10):
    state = lines[i][-2]
    states[state] = {}
    states[state]['0'] = {}
    states[state]['0']['write'] = int(lines[i+2][-2])
    states[state]['0']['move'] = 1 if lines[i+3][-6] == 'r' else -1
    states[state]['0']['next'] = lines[i+4][-2]
    states[state]['1'] = {}
    states[state]['1']['write'] = int(lines[i+6][-2])
    states[state]['1']['move'] = 1 if lines[i+7][-6] == 'r' else -1
    states[state]['1']['next'] = lines[i+8][-2]

for state in states:
    print(state, states[state])

min_tape = -2
max_tape = 2
tape = {}
cursor = 0
state = begin_state


def print_tape(count):
    print('...', end=' ')
    for i in range(min_tape, max_tape + 1):
        value = tape[i] if i in tape else '0'
        if cursor == i:
            print("[%s]" % value, end=' ')
        else:
            print(value, end=' ')
    print('...', end=' ')
    print('(after %d steps; about to run state %s)' % (count, state))


print_tape(0)
for r in range(checksum_steps):

    if cursor not in tape:
        tape[cursor] = '0'
    value = tape[cursor]
    s = states[state][value]
    write = str(s["write"])
    move = s["move"]
    nxt_state = s["next"]

    min_tape = min(min_tape, cursor - 1)
    max_tape = max(max_tape, cursor + 1)

    tape[cursor] = write
    cursor += move
    state = nxt_state

    # print_tape(r+1)
    if r % 100000 == 0:
        print("step %d" % r)

checksum = 0
for i in range(min_tape, max_tape):
    checksum += 1 if i in tape and tape[i] == '1' else 0

print("Diagnostic checksum:", checksum)
