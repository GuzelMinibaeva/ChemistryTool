from .abc import MoleculeABC
from ..algorithms import Isomorphism


class Molecule(Isomorphism, MoleculeABC):
    def __init__(self, atoms, bonds):
        super(Molecule, self).__init__()
        self._atoms = atoms
        self._bonds = bonds

    def add_atom(self, element: str, number: int):
        if number in self._atoms:
            raise KeyError
        else:
            self._atoms[number] = element

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom in self._bonds and end_atom in self._bonds[start_atom]:
            raise KeyError
        elif start_atom in self._bonds:
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[end_atom][start_atom] = bond_type
        else:
            self._bonds[start_atom] = {end_atom: bond_type}
            self._bonds[end_atom] = {start_atom: bond_type}


__all__ = ['Molecule']
