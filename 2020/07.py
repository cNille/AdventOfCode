# Read in groups from file
lines = [x.strip() for x in open('07.test', 'r').readlines() if x != '']
lines = [x.strip() for x in open('07.input', 'r').readlines() if x != '']

def part1():
    bags = {}
    for l in lines:
        bag, contains = l.split('contain')
        bag = bag.replace(' bags','')
        bags[bag] = contains

    q = ['shiny gold']                   # Work queue for traversing bags
    answer = set()
    while len(q) != 0:
        current = q.pop(0)
        for b in bags:
            if b in answer:             # Skip if already counted. 
                continue
            if current in bags[b]:      # If bag contains current-bag, 
                q.append(b)             # add to queue and answer
                answer.add(b)
    return len(answer)

def part1deepfunc():
    bags = {}
    for l in lines:
        bag, contains = l.split('contain')
        bag = bag.replace(' bags','')
        bags[bag] = contains

    def contains_shiny_gold(bag, bags):
        return set().union(*[
            set([b]).union(contains_shiny_gold(b, bags))
            for b in bags
            if bag in bags[b]
        ])
        
    total = contains_shiny_gold('shiny gold', bags)
    return len(total) 

def part1deep():
    bags = {}
    for l in lines:
        bag, contains = l.split('contain')
        bag = bag.replace(' bags','')
        bags[bag] = contains

    def contains_shiny_gold(bag, bags):
        contains = []
        for b in bags:
            if bag in bags[b]:
                # Add b to our list
                contains.append(b)

                # Add all children to b in our list
                contains.extend(contains_shiny_gold(b, bags))
        return set(contains)
        
    total = contains_shiny_gold('shiny gold', bags)
    return len(total) 

def part1deque():
    from collections import deque
    bags = {}
    for l in lines:
        bag, contains = l.split('contain')
        bag = bag.replace(' bags','')
        bags[bag] = contains

    q = deque(['shiny gold'])                # Work queue for traversing bags
    answer = set()
    while len(q) != 0:
        current = q.popleft()
        for b in bags:
            if b in answer:             # Skip if already counted. 
                continue
            if current in bags[b]:      # If bag contains current-bag, 
                q.append(b)             # add to queue and answer
                answer.add(b)
    return len(answer)

def part2():
    bags = {}
    q = []
    for l in lines:
        # Clean line from unnecessary words.
        l = l.replace('bags', '').replace('bag', '').replace('.','')
        
        bag, contains = l.split('contain')
        bag = bag.strip()

        if 'no other' in contains:
            bags[bag] = {}
            continue

        contains = contains.split(',')
        contain_dict = {}
        for c in [c.strip() for c in contains]:
            amount = c[:2]
            color = c[2:]
            contain_dict[color] = int(amount)
        bags[bag] = contain_dict 

    def recursive_count(bag, bags):
        contained_bags = bags[bag]
        count = 1
        for s in contained_bags:
            multiplier = contained_bags[s]
            count += multiplier * recursive_count(s, bags) 
        return count 
    
    # Minus one to not count the shiny gold bag itself
    return recursive_count('shiny gold', bags) - 1 

def part1recursive():
    bags = {}
    for l in lines:
        bag, contains = l.split('contain')
        bag = bag.replace(' bags','')
        bags[bag] = contains

    answer = set()
    def rec_count(color, bags):
        for b in bags:
            if color in bags[b]:
                rec_count(b, bags)
                answer.add(b)
    rec_count('shiny gold', bags)
    return len(answer)


import re
from collections import defaultdict
def regex():
    bags = defaultdict(dict)
    for l in lines:
        bag = re.match(r'(.*) bags contain', l).groups()[0]
        for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
            bags[bag][b] = int(count)

    def part1():
        answer = set()
        def search(color):
            for b in bags:
                if color in bags[b]:
                    answer.add(b)
                    search(b)
        search('shiny gold')
        return len(answer)
    print(part1())

    def part2():
        def search(bag):
            count = 1
            for s in bags[bag]:
                multiplier = bags[bag][s]
                count += multiplier * search(s) 
            return count 
        return search('shiny gold' ) - 1  # Rm one for shiny gold itself
    print(part2())


import re
from collections import defaultdict
import networkx as nx
def graph():
    bags = defaultdict(dict)
    for l in lines:
        bag = re.match(r'(.*) bags contain', l).groups()[0]
        for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
            bags[bag][b] = { 'weight': int(count)}

    # Create a graph in networkx
    G = nx.DiGraph(bags)

    def part1():
        # Reverse edges
        RG = G.reverse()
        # Get predecessors
        predecessors = nx.dfs_predecessors(RG, 'shiny gold')
        # Count predecessors
        for p in predecessors:
            print(p)
        return len(predecessors)

    print(part1())
    #print(nx.shortest_path(G, source='bright red', target='shiny gold'))

    def part2():
        def depth_search(node):
            cost = 1 
            # Iterate neighbors for node
            for n in G.neighbors(node):
                # Multiply weight with recursive search
                cost += G[node][n]['weight'] * depth_search(n)
            return cost
        return depth_search('shiny gold') - 1
    print(part2())
graph()
