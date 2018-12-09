import operator

# Sorting
def sort_dic_by_keys(d):
    return sorted(d.items(), key=operator.itemgetter(0))
def sort_dic_by_values(d):
    return sorted(d.items(), key=operator.itemgetter(1))

# -----------------------------------------------------------------------------

# Import data
data = [x.strip() for x in open('day_08_input.txt','r').readlines()]
data = [int(x) for x in data[0].split()]

# Part 1
def sum_meta_1(data):
    nbr_childs, nbr_meta = data[:2]
    data = data[2:]

    m = 0
    for j in range(nbr_childs):
        (c,data) = sum_meta_1(data)
        m += c

    meta = m + sum(data[:nbr_meta])
    return (meta, data[nbr_meta:])

(meta, d) = sum_meta_1(data)
print('-'*80)
print('ResultMeta: %d' % meta)
exit()

meta = 0
def sum_meta_2(i, depth):
    global meta
    nbr_childs = data[i]
    nbr_meta = data[i+1]

    child_start = i + 2
    node_length = 2 + nbr_meta


    child_sums = []
    for j in range(nbr_childs):
        (l, child_sum) = sum_meta_2(child_start, depth + 1)
        child_start += l
        node_length += l
        child_sums.append(child_sum)

    m = data[child_start:child_start+nbr_meta]
    if nbr_childs == 0:
        return (node_length, sum(m))

    meta_sum = 0
    for x in m:
        if x <= len(child_sums):
            meta_sum += child_sums[x-1]

    return (node_length, meta_sum)

(n, meta) = sum_meta_2(0,0)
print('-'*80)
print('ResultMeta: %d' % meta)
