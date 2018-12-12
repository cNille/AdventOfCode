data = 5093
grid_serial = data
mtx = []
for i in range(1,301):
    if i % 10 == 0:
        print('row %d...' % i)
    mtx.append([])
    for j in range(1,301):
        rackid = i + 10
        lvl = rackid * j
        value = (lvl + grid_serial) * rackid
        digit = (value / 100) % 10
        power_lvl = digit - 5
        mtx[i-1].append(power_lvl)

import operator
def sort_dic_by_values(d):
    return sorted(d.items(), key=operator.itemgetter(1))

max_power = 0
max_coor = None
m = {}
for size in range(1,301):
    for i in range(1,301 - size):
        for j in range(1,301 - size):
            value = 0
            for x in range(i,i+size):
                for y in range(j,j+size):
                    value += mtx[x-1][y-1]
            if value >= max_power:
                max_power = value
                max_coor = (i,j,size)
            m[(i,j)] = value

    print(sort_dic_by_values(m)[-5:])
    print('Iteration %d, Result is with power %d:' %(size, max_power), max_coor)
