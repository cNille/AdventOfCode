print(chr(27)+'[2j')
print('\033c')
f = open('24.test', 'r')
f = open('24.input', 'r')
mtx = [x.strip() for x in f.readlines()]
print("Day 24")
import copy
from collections import deque
from colorama import Fore, Back, Style

start = (1,0)
end = (len(mtx[-1])-2,len(mtx)-2)

R = 0
D = 1
L = 2
U = 3
wind = [ 
    set(),
    set(),
    set(),
    set(),
]
for y,row in enumerate(mtx):
    for x,cell  in enumerate(row):
        if cell == '>':
            wind[R].add((x,y))
        if cell == '<':
            wind[L].add((x,y))
        if cell == 'v':
            wind[D].add((x,y))
        if cell == '^':
            wind[U].add((x,y))
W = len(mtx[0])-2
H = len(mtx)-2

def print_map(t, pos):
    for y, row in enumerate(mtx):
        line = ""
        for x, cell in enumerate(row):
            x2,y2 = x-1, y-1
            if pos == (x,y):
                line += Fore.RED + "E" + Style.RESET_ALL
                continue
            if 0==x or y==0 or x==len(row)-1 or y==len(mtx)-1:
                line += Fore.LIGHTBLACK_EX + cell + Style.RESET_ALL
                continue

             
            if ((x2-t)%W+1,y) in wind[R]:
                line += ">"
            elif ((x2+t)%W+1,y) in wind[L]:
                line += "<"
            elif (x,(y2+t)%H+1) in wind[U]:
                line += "^"
            elif (x,(y2-t)%H+1) in wind[D]:
                line += "v"
            #elif ((x-t)%W,y) in wind[L]:
            #    line += "^"
            #elif t%H in wind_v_b[x2]:
            #    line += "v"
            else:
                line += "."
        print(line)



def walk(T, start,end):
    print("WALK", start, "to", end, "with T=", T)
    verbose = T != 0
    verbose = False 
    q = deque()
    visited = []
    q.append((T,start, visited))
    DIR = [(1,0), (-1,0), (0,1), (0,-1)]
    states = set()
    while len(q) > 0:
        T, (x,y), visited = q.popleft()
        if (T, (x,y)) in states:
            continue
        states.add((T, (x,y)))
        #print("NXT", T, (x,y), len(q))
        if verbose:
            print_map(T, (x,y))
        visited = [x for x in visited] 
        visited.append((T,(x,y)))
        if (x,y) == end:
            print("Solution", T+1, "for", start, end)
            return T+1
            #for t, (x,y) in visited:
            #    print('-'*20)
            #    print(t, (x,y))

            #    print_map(t, (x,y))
        
        Ns = [(x+dx, y+dy) for dx,dy in DIR]
        Ns = [(nx,ny) for nx,ny in Ns if (
            0 < nx and nx < len(mtx[0])-1
            and 0 < ny and ny < len(mtx)-1
        )]
        Ns.append((x,y))

        t2 = T+1
        # Go to neighbours
        for (nx,ny) in Ns:
            x2 = nx-1
            y2 = ny-1
            if ((x2-t2)%W+1,ny) in wind[R]:
                continue
            elif ((x2+t2)%W+1,ny) in wind[L]:
                continue
            elif (nx,(y2+t2)%H+1) in wind[U]:
                continue
            elif (nx,(y2-t2)%H+1) in wind[D]:
                continue
            q.append((t2,(nx,ny), visited))


t1 = 0
t2 = walk(t1, start,end)
print("Walk 1:", t2)
end2 = (len(mtx[-1])-2,len(mtx)-1)
start2= (1,1)
t3 = walk(t2, end2, start2)
print("Walk 2:", t3)
t4 = walk(t3, start,end)
print("Walk 3:", t4)
