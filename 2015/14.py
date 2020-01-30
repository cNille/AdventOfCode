data = [x.strip() for x in open('14.input', 'r').readlines()]

deers = {}
for d in data:
    d = d.split(' ')
    name = d[0]
    v = int(d[3])
    fly = int(d[6])
    rest = int(d[-2])

    print name, v, fly, rest 
    deers[name] = [v, fly, rest]

time = 2503
max_dist = 0
for d in deers:
    [v, fly, rest] = deers[d]
    
    round_time = fly + rest 
    whole_rounds = int( 1.0 * time / round_time) + 1
    
    part_round = 0
    if time % round_time < fly:
        whole_rounds -= 1
        part_round = (time % round_time) * v

    distance = whole_rounds * (fly*v) + part_round
    max_dist = max(max_dist, distance)

print "Part 1: %d" % max_dist

# Part 2
# for i in range(1,2504):
#     print i
#     for d in deers:
        
