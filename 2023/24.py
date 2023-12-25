from itertools import combinations
from z3 import Solver, Int
import numpy as np

print(chr(27)+'[2j')
print('\033c')
f = open('24.test', 'r')
f = open('24.input', 'r')
lines = [x.strip() for x in f.readlines()]

area = (7, 27)
area = (200000000000000, 400000000000000)


hailstones = []
for line in lines:
    pos, velocity = line.split(' @ ')
    pos = tuple([int(x) for x in pos.split(',')])
    velocity = tuple([int(x) for x in velocity.split(',')])
    hailstones.append((pos, velocity))


def line_from_particle(particle):
    (x0, y0, _), (vx, vy, _) = particle  # Extract x, y components, ignore z
    m = vy / vx if vx != 0 else float('inf')  # Handle vertical line case
    b = y0 - m * x0
    return m, b


def intersect(particle1, particle2):
    m1, b1 = line_from_particle(particle1)
    m2, b2 = line_from_particle(particle2)

    # Check for parallel lines
    if m1 == m2:
        return None

    A = np.array([[-m1, 1], [-m2, 1]])
    B = np.array([b1, b2])

    try:
        x, y = np.linalg.solve(A, B)
        return x, y
    except np.linalg.LinAlgError:  # No solution
        return None


def within_bounds(crossing, min_value, max_value):
    x, y = crossing
    return min_value <= x <= max_value and min_value <= y <= max_value


def is_front(crossing, h1):
    cx, cy = crossing
    (x1, y1, _), (vx1, vy1, _) = h1
    tx = (cx - x1) / vx1
    ty = (cy - y1) / vy1
    return tx >= 0 or ty >= 0


inside_crosses = set()
for h1, h2 in combinations(hailstones, 2):
    if h1 == h2:
        continue
    crossing = intersect(h1, h2)

    if crossing is not None:
        # Check if crossing is "in front" of both hailstones
        if not is_front(crossing, h1):
            continue
        if not is_front(crossing, h2):
            continue
        if not within_bounds(crossing, area[0], area[1]):
            continue

        # print(Fore.GREEN + 'Crossing: {}'.format(crossing) + Style.RESET_ALL)
        inside_crosses.add((h1, h2))

print('Part 1:', len(inside_crosses))

# Part 2
# I'm not good enough at linear algebra to solve this one, so I'm going to
# Z3 to solve the system of equations for me. I'm lazy, I know. Sue me.
solver = Solver()

# Declare the variables we're looking for
x0, y0, z0 = Int('x'), Int('y'), Int('z')
vx, vy, vz = Int('dx'), Int('dy'), Int('dz')

for i, ((hx, hy, hz), (hvx, hvy, hvz)) in enumerate(hailstones):
    t = Int(f't{i}')
    solver.add(hx + hvx * t == x0 + vx * t)
    solver.add(hy + hvy * t == y0 + vy * t)
    solver.add(hz + hvz * t == z0 + vz * t)

# Check that it adds up
solver.check()


# Evaluate the solution of x+y+z for the point.
model = solver.model()
print('Part 2:', model.eval(x0 + y0 + z0))
