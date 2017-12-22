import re

data = open('my.input','r').read()
particlesRegex = r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>'
particles = re.findall(particlesRegex, data)
min_acc = 9999

for idx, p in enumerate(particles):
    abs_acc = sum(map(abs, map(int, p[6:9])))
    if abs_acc < min_acc:
        curr_min = idx 
    if abs_acc == min_acc:
        print(idx,'Same', p)
    min_acc = min(min_acc, abs_acc)

print(curr_min, particles[curr_min])

