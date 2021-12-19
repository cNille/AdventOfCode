print(chr(27)+'[2j')
print('\033c')
f = open('19.input', 'r')
f = open('19.test', 'r')
data = [x.strip() for x in f.read().split('\n\n')]

print(data[:10])

scanners = []
for scanner in data:
    scanner = scanner.split('\n')
    beacons = []
    for beacon in scanner[1:]:
        x,y,z = map(int,beacon.split(','))
        beacons.append((x,y,z))
    scanners.append(beacons)



def get_orientations(beacons):
    orientations = []
    orientations.append([( x,  y,  z) for (x,y,z) in beacons])
    orientations.append([( x,  y, -z) for (x,y,z) in beacons])
    orientations.append([( x, -y,  z) for (x,y,z) in beacons])
    orientations.append([( x, -y, -z) for (x,y,z) in beacons])
    orientations.append([(-x,  y,  z) for (x,y,z) in beacons])
    orientations.append([(-x,  y, -z) for (x,y,z) in beacons])
    orientations.append([(-x, -y,  z) for (x,y,z) in beacons])
    orientations.append([(-x, -y, -z) for (x,y,z) in beacons])
    orientations.append([( y,  z,  x) for (x,y,z) in beacons])
    orientations.append([( y,  z, -x) for (x,y,z) in beacons])
    orientations.append([( y, -z,  x) for (x,y,z) in beacons])
    orientations.append([( y, -z, -x) for (x,y,z) in beacons])
    orientations.append([(-y,  z,  x) for (x,y,z) in beacons])
    orientations.append([(-y,  z, -x) for (x,y,z) in beacons])
    orientations.append([(-y, -z,  x) for (x,y,z) in beacons])
    orientations.append([(-y, -z, -x) for (x,y,z) in beacons])
    orientations.append([( z,  x,  y) for (x,y,z) in beacons])
    orientations.append([( z,  x, -y) for (x,y,z) in beacons])
    orientations.append([( z, -x,  y) for (x,y,z) in beacons])
    orientations.append([( z, -x, -y) for (x,y,z) in beacons])
    orientations.append([(-z,  x,  y) for (x,y,z) in beacons])
    orientations.append([(-z,  x, -y) for (x,y,z) in beacons])
    orientations.append([(-z, -x,  y) for (x,y,z) in beacons])
    orientations.append([(-z, -x, -y) for (x,y,z) in beacons])
    orientations.append([( x,  z,  y) for (x,y,z) in beacons])
    orientations.append([( x,  z, -y) for (x,y,z) in beacons])
    orientations.append([( x, -z,  y) for (x,y,z) in beacons])
    orientations.append([( x, -z, -y) for (x,y,z) in beacons])
    orientations.append([(-x,  z,  y) for (x,y,z) in beacons])
    orientations.append([(-x,  z, -y) for (x,y,z) in beacons])
    orientations.append([(-x, -z,  y) for (x,y,z) in beacons])
    orientations.append([(-x, -z, -y) for (x,y,z) in beacons])
    orientations.append([( z,  y,  x) for (x,y,z) in beacons])
    orientations.append([( z,  y, -x) for (x,y,z) in beacons])
    orientations.append([( z, -y,  x) for (x,y,z) in beacons])
    orientations.append([( z, -y, -x) for (x,y,z) in beacons])
    orientations.append([(-z,  y,  x) for (x,y,z) in beacons])
    orientations.append([(-z,  y, -x) for (x,y,z) in beacons])
    orientations.append([(-z, -y,  x) for (x,y,z) in beacons])
    orientations.append([(-z, -y, -x) for (x,y,z) in beacons])
    orientations.append([( y,  x,  z) for (x,y,z) in beacons])
    orientations.append([( y,  x, -z) for (x,y,z) in beacons])
    orientations.append([( y, -x,  z) for (x,y,z) in beacons])
    orientations.append([( y, -x, -z) for (x,y,z) in beacons])
    orientations.append([(-y,  x,  z) for (x,y,z) in beacons])
    orientations.append([(-y,  x, -z) for (x,y,z) in beacons])
    orientations.append([(-y, -x,  z) for (x,y,z) in beacons])
    orientations.append([(-y, -x, -z) for (x,y,z) in beacons])
    return orientations

beacons = set(scanners[0])
del scanners[0]
i = 0
scanner_pos = []
while len(scanners) > 0:
    scanner = scanners[i%len(scanners)]
    orientations = get_orientations(scanner)
    print("Round %d. Orientations %d, beacons %d" % (i, len(scanners), len(beacons)))


    for orientation in orientations:
        match_found = False

        for (x1,y1,z1) in orientation:
            for (x2,y2,z2) in beacons:
                dx,dy,dz = (x2-x1, y2-y1, z2-z1)

                count = 0
                for (x,y,z) in orientation:
                    if (x+dx, y+dy, z+dz) in beacons:
                        count += 1

                if (count >= 12):
                    match_found = True
                    print("Match found: ", i%len(scanners))
                    print("Scanner position", dx,dy,dz)
                    scanner_pos.append((dx,dy,dz))
                    del scanners[i%len(scanners)]
                    beacons.update([(x+dx, y+dy, z+dz) for (x,y,z) in orientation])
                    break
            if match_found:
                break
    i += 1


print("Round %d. Orientations %d, beacons %d" % (i, len(scanners), len(beacons)))

print(scanner_pos)
#scanner_pos = [(-28, 54, 1186), (4, -48, -1271), (20, 1153, 29), (-1162, 103, 1087), (-93, 1114, -1319), (1247, 98, -1298), (-1306, 1, -1249), (1088, 1209, -1319), (1129, -1159, -1235), (1096, 2479, -1243), (10, 2483, -106), (-10, 2418, 1070), (-1317, 2509, 1064), (-120, 48, 2433), (1170, 2391, -57), (-2335, 1200, 1178), (1210, 58, -2484), (-2414, 81, 1159), (-1197, -1276, 1092), (-1264, -2303, 1036), (-1180, -2362, 2390), (46, 1180, 1209), (-2341, -2427, 2430), (-2505, -3596, 2273)] 

dist = 0
for (x1,y1,z1) in scanner_pos:
    for (x2,y2,z2) in scanner_pos:
        manhattan = abs(x2-x1) + abs(y2-y1) + abs(z2-z1)
        dist = max(dist, manhattan)

print('Manhattan:', dist)

