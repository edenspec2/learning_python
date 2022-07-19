with open("file.xyz", 'w') as xyz_file:
    xyz_file.write("%d\n%s\n" % (len(molecule.atoms), title))
    for atom in molecule.atoms:
        xyz_file.write("{:4} {:11.6f} {:11.6f} {:11.6f}\n".format(
            atom.atomic_symbol, atom.coordinates.x, atom.coordinates.y, atom.coordinates.z))
