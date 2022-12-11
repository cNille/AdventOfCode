from dataclasses import dataclass
print(chr(27)+'[2j')
print('\033c')
f = open('11.test', 'r')
#f = open('11.input', 'r')
blocks = f.read().split('\n\n')

print("Day 11")

part1 = False
part1 = True

@dataclass
class Monkey:
    id: int
    items: list[int]
    op_operator: str 
    op_value: str
    test_value: int
    test_true: int
    test_false: int
    inspections: int

    def turn(self) -> tuple[int, int]:
        # Monkey inspect
        self.inspect()

        # Relief
        self.relief()

        # Throw
        send_to, item = self.test()
        return send_to, item

    def inspect(self):
        self.inspections += 1
        worry = self.items[0]
        new_worry = 0
        if self.op_operator == "+":
            if self.op_value == "old":
                 new_worry = worry + worry 
            else:
                 new_worry = worry + int(self.op_value)
        elif self.op_operator == "*": 
            if self.op_value == "old":
                 new_worry = worry * worry 
            else:
                 new_worry = worry * int(self.op_value)
        self.items[0] = new_worry
        

    def relief(self):
        worry = self.items[0]

        if part1:
            new_worry = int(worry / 3)
        else:
            new_worry = worry % mod 

        self.items[0] = new_worry

    def test(self) -> tuple[int, int]:
        worry = self.items.pop(0)
        divisible = (worry % self.test_value) == 0
        send_to = self.test_true if divisible else self.test_false
        return (send_to, worry)


monkeys = []

primes = []
for block in blocks:
    lines = block.split('\n')
    print("Parse", lines[0][:-1])
    monkey_id = int(lines[0].split(' ')[1][:-1])
    items = lines[1].split(': ')[1].split(', ')
    items = [int(x) for x in items]
    op_operator = lines[2].split(' ')[-2]
    op_value = lines[2].split(' ')[-1]
    test_value = int(lines[3].split(' ')[-1])
    primes.append(test_value)
    test_true = int(lines[4].split(' ')[-1])
    test_false = int(lines[5].split(' ')[-1])
    monkey = Monkey(
        monkey_id, items, op_operator, op_value,
        test_value, test_true, test_false, 0
    )
    monkeys.append(monkey)

mod = 1
for p in primes:
    mod *= p

#Monkey 0:
#  Starting items: 65, 78
#  Operation: new = old * 3
#  Test: divisible by 5
#    If true: throw to monkey 2
#    If false: throw to monkey 3
#    for line in lines:

def print_monkeys(monkeys):
    #for m in monkeys:
    #   print("Monkey %d:" % m.id, m.items)
    #total_inspections = 0
    for m in monkeys:
        print("Monkey %d has inspected %d" % (m.id, m.inspections))
        #total_inspections += m.inspections
    #print("TOTAL INSP:", total_inspections)


def go_round(monkeys):
    for m in monkeys:
        for _ in range(len(m.items)):
            send_to, item = m.turn()
            #print("M%d sends %d to M%d" % (m.id, item, send_to))
            monkeys[send_to].items.append(item)
    print_monkeys(monkeys)

if part1:
    ROUNDS = 20 
else:
    ROUNDS = 10000
worry = 0
print('-'*20)
print('Initial monkeys')
print_monkeys(monkeys)
for i in range(ROUNDS):
    print('-'*40)
    print('ROUND', i +1)
    go_round(monkeys)


insps = []
for m in monkeys:
    print("Monkey %d: %d inspections" % (m.id, m.inspections))
    insps.append(m.inspections)

insps.sort()
result = 1
for i in insps[-2:]:
    print(i)
    result *= i
print("Solution part 1:", result)
