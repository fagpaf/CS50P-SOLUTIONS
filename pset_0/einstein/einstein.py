def relativity(m, c):
    e = m * c * c
    return e
mass = int(input())

E = relativity(mass, 300000000)
print(E)
