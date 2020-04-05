n = int(input())
total = 0
for i in range(n):
    s = input()
    if s == 'Tetrahedron':
        total += 4
    elif s == 'Cube':
        total += 6
    elif s == 'Octahedron':
        total += 8
    elif s == 'Dodecahedron':
        total += 12
    else:
        total += 20
print(total)
