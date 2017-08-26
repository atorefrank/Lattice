# import ase
# from ase.cluster.cubic import FaceCenteredCubic
# from ase.visualize import view

# surfaces = [(1, 0, 0), (1, 1, 0), (1, 1, 1)]
# layers = [6, 9, 5]
# lc = 3.61000
# atoms = FaceCenteredCubic('Cu', surfaces, layers, latticeconstant=lc)
# view(atoms)
# print(atoms.get_positions())

# nx= 2
# ny= 2
# nz= 2
# for x in range(nx):
#    for y in range(ny):
#        for z in range(nz):
#            print(x, y, z)

import itertools, numpy

cube = numpy.array(list(itertools.product((0,0.8), (0,0.8), (0,0.8))))

x_dim = y_dim = z_dim = 2

for offset in itertools.product(*map(range, (x_dim, y_dim, z_dim))):
    print(cube+offset)



print(cube)