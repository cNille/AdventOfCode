print(chr(27)+'[2j')
print('\033c')
f = open('19.input', 'r')
#f = open('19.test', 'r')
lines = f.read()

workflows, ratings = lines.split('\n\n')
workflows_arr = workflows.strip().split('\n')
ratings_arr = ratings.strip().split('\n')

workflows = {}
limits = {'x': [0, 4000], 'm': [0, 4000], 'a': [0, 4000], 's': [0, 4000]}
for w in workflows_arr:
    name, rules = w.split('{')
    rules = rules[:-1].split(',')
    workflows[name] = rules
    for rule in rules:
        rule = rule.strip().split(':')[0]
        n = rule[0]
        if n in ('x', 'm', 'a', 's') and '<' in rule or '>' in rule:
            limit = int(rule[2:])
            if '<' in rule:
                limit = limit - 1
            limits[n].append(limit)


ratings = []
for rating in ratings_arr:
    parts = rating[1:-1].split(',')
    rating = {}
    for p in parts:
        k, v = p.split('=')
        rating[k] = int(v)
    ratings.append(rating)


def solve_part1(workflows, rating):
    workflow = 'in'
    status = None
    while status is None:
        for rule in workflows[workflow]:
            if rule == 'A':
                status = 'A'
                break
            elif rule == 'R':
                status = 'R'
                break
            elif ':' not in rule:
                workflow = rule
                break

            match, dest = rule.split(':')
            greater = '>' in match
            less = '<' in match
            value = int(match[2:])
            match = match[0]
            if greater and rating[match] > value:
                if dest in ('A', 'R'):
                    status = dest
                    break
                workflow = dest
                break
            elif less and rating[match] < value:
                if dest in ('A', 'R'):
                    status = dest
                    break
                workflow = dest
                break
    if status == 'A':
        rating_sum = rating['x'] + rating['m'] + rating['a'] + rating['s']
        return rating_sum
    else:
        return 0


result = 0
for rating in ratings:
    result += solve_part1(workflows, rating)
print('Part 1:', result)

# =======================
# =======================
# Part 2


def range_differences(r1, r2):
    a, b = r1
    c, d = r2
    if c > b or a > d:
        return [r1]
    intersection = [max(a, c), min(b, d)]
    differences = []
    if a < intersection[0]:
        differences.append([a, intersection[0]])
    if intersection[1] < b:
        differences.append([intersection[1], b])
    if len(differences) == 0:
        return None
    return differences


def calc_ranges(ranges):
    matches = 1
    for r in ranges:
        a, b = ranges[r]
        b -= 1
        diff = (b - a) + 1
        matches *= diff
    return matches


def rec(workflow, in_ranges):
    ranges = in_ranges.copy()

    if workflow == 'A':
        return calc_ranges(ranges)
    elif workflow == 'R':
        return 0

    accepted = 0
    for rule in workflows[workflow]:
        if rule in ('A', 'R'):
            accepted += rec(rule, ranges)
            break
        elif rule in workflows:
            accepted += rec(rule, ranges)
            continue

        condition, dest = rule.split(':')
        op = ">" if '>' in condition else "<"
        new_ranges = ranges.copy()

        value = int(condition[2:])
        expr_rule = condition[0]
        r = ranges[expr_rule]
        for r in ranges:
            if r != expr_rule:
                new_ranges[r] = ranges[r]
            else:
                a, b = ranges[r]
                if op == '>':
                    new_ranges[r] = (max(a, value)+1, b)
                    accepted += rec(dest, new_ranges)
                elif op == '<':
                    new_ranges[r] = (a, min(b, value))
                    accepted += rec(dest, new_ranges)

        # Flip the ranges
        clean_ranges = {}
        for r in ranges:
            a, b = ranges[r]
            c, d = new_ranges[r]
            differences = range_differences([a, b], [c, d])
            if differences is None:
                clean_ranges[r] = ranges[r]
                continue
            for diff in differences:
                clean_ranges[r] = tuple(diff)
        new_ranges = clean_ranges
        ranges = new_ranges

    return accepted


ranges = {
    'x': (1, 4001),
    'm': (1, 4001),
    'a': (1, 4001),
    's': (1, 4001),
}
result = rec('in', ranges)
print('Part 2:', result)
assert(result == 125657431183201)
