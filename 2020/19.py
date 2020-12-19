from collections import defaultdict
import re
lines = [x.strip() for x in open('19.test', 'r').readlines() if x != '']
lines = [x.strip() for x in open('19.test2', 'r').readlines() if x != '']
lines = [x.strip() for x in open('19.input', 'r').readlines() if x != '']

stop = lines.index('')
rules = dict([r.split(': ') for r in lines[:stop]])
messages = lines[stop+1:]

def part1(rules, messages):
    def valid1(rule_key, msg, index):
        rule = rules[rule_key]
        if index >= len(msg):
            return []

        if rule == '"a"':
            return [index + 1] if msg[index] == 'a' else [index]
        elif rule == '"b"':
            return [index + 1] if msg[index] == 'b' else [index]

        valid_combinations = [] 
        for pipe in rule.split(' | '):
            rule_order = pipe.split(' ')
            combination_list = valid1(rule_order[0], msg, index)
            for current_rule in rule_order[1:]:
                if len(combination_list) == 0:
                    break
                tmp = []
                for new_index in combination_list:
                    if new_index != index:
                        tmp += valid1(current_rule, msg, new_index)
                combination_list = tmp
            valid_combinations += set(list(combination_list))

        return valid_combinations

    valid_count = 0 
    for i, msg in enumerate(messages):
        mem = {}
        v = valid1('0', msg, 0)
        is_valid = len(msg) in v
        #print i+1, "Is valid:", is_valid, msg
        if is_valid:
            valid_count += 1

    print "Part 1 solution: %d" % valid_count
part1(rules, messages)

# ===================================
# ===================================
# ===================================
def divide_in_half(str):
    halfpoint = (len(str)/2)
    return str[:halfpoint], str[halfpoint:]

def chunk_str(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]


def part2(rules, messages):
    def possible_combinations(rule_key, rules):
        rule = rules[rule_key]
        if rule in '"a"':
            return ['a'] 
        elif rule == '"b"':
            return ['b'] 

        valid_combinations = [] 
        for pipe in rule.split(' | '):
            rule_order = pipe.split(' ')
            combination_list = possible_combinations(rule_order[0], rules)
            for current_rule in rule_order[1:]:
                tmp = []
                for comb in combination_list:
                    new_combs = possible_combinations(current_rule, rules)
                    for nc in new_combs:
                        tmp.append(comb + nc)
                combination_list = list(set(tmp))
            valid_combinations += combination_list
        return valid_combinations

    def valid(msg, a, b, n):
        head = msg[:n]
        tail = msg[n+0:]
        if head not in a:
            return False
        if len(tail) <= n:
            return False
        
        tail = chunk_str(tail, n)
        left, right = divide_in_half(tail)
        is_valid = (
                len(left) == len(right) and 
                all([(x in a) for x in left]) and 
                all([(x in b) for x in right])
        )
        if is_valid:
            return True
        return valid(msg[n:], a,b,n)

    # Deferred rules from input
    a = possible_combinations('42', rules)
    b = possible_combinations('31', rules)

    valid_count = 0
    for i, m in enumerate(messages):
        is_valid = valid(m, a, b, len(a[0]))
        #print "Validating (%d):" % i, is_valid, valid_count, m
        if is_valid:
            valid_count += 1
    print "Part 2 solution: %d" % valid_count
part2(rules, messages)
