from ase import Atoms
from ase.io import write

a0 = 5.6537

#CIF conventional cell was 8 atoms per unit cell, cant use easily therefore have to create unt cell
primitive = Atoms(
    symbols=['Al', 'As'],
    scaled_positions=[[0, 0, 0], [0.25, 0.25, 0.25]],
    cell=[a0, a0, a0],
    pbc=True
)

cation_layers = ['Al']*6 + ['Ga']*4 + ['Al']*6

layers = []
for i, cat in enumerate(cation_layers):
    atom = primitive.copy()
    atom[0].symbol = cat
    atom[1].symbol = 'As'
    atom.translate([0, 0, i * a0])
    layers.append(atom)

stacked = layers[0]
for l in layers[1:]:
    stacked += l

final = stacked.repeat((2, 2, 1))
final.center(vacuum=10, axis=2)

write('1QW_AlGaAs_128atoms.xyz', final)
write('1QW_AlGaAs_128atoms.cif', final)

print("Done!(GUI: ase gui 1QW_AlGaAs_128atoms.xyz)")
