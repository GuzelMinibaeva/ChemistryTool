from collections import Counter
from .abc import MoleculeABC
from ..algorithms import Isomorphism
from ..periodictable.element import Element


class Molecule(Isomorphism, MoleculeABC):
    def add_atom(self, element: str, number: int):
        if number in self._atoms:
            raise KeyError
        else:
            self._atoms[number] = element
            self._bonds[number] = {}

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom not in self._atoms or end_atom not in self._atoms:
            raise KeyError
        elif start_atom in self._bonds[end_atom] or end_atom in self._bonds[start_atom]:
            raise KeyError
        elif start_atom == end_atom:
            raise KeyError
        else:
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[end_atom][start_atom] = bond_type

    def get_atom(self, number: int) -> Element:
        return self._atoms[number]

    def get_bond(self, start_atom: int, end_atom: int) -> int:
        return self._bonds[start_atom][end_atom]

    def update_atom(self, element: Element, number: int):
        if number not in self._atoms:
            raise KeyError
        else:
            self._atoms[number] = element

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom not in self._bonds[end_atom] or end_atom not in self._bonds[start_atom]:
            raise KeyError
        elif start_atom == end_atom:
            raise KeyError
        else:
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[end_atom][start_atom] = bond_type

    def delete_atom(self, number: int):
        del self._atoms[number]
        del self._bonds[number]
        for atom, subdict in self._bonds.items():
            for key, value in subdict.items():
                if key == number:
                    del self._bonds[atom][key]

    def delete_bond(self, start_atom: int, end_atom: int):
        del self._bonds[start_atom][end_atom]
        del self._bonds[end_atom][start_atom]

    def __enter__(self):
        self._atoms_res = self._atoms.copy()
        self._bonds_res = {}
        for i in self._bonds:
            self._bonds_res[i] = {}
        for key, value in self._bonds:
            self._bonds_res[key] = value.copy()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._atoms = self._atoms_res
            for key, value in self._bonds_res.items():
                self._bonds[key] = value
            del self._atoms_res
            del self._bonds_res
        else:
            del self._atoms_res
            del self._bonds_res

    def __str__(self):
        counter = Counter(self._atoms.values())
        out = list()
        for key, value in counter.items():
            out.append(key + str(value))
        return ''.join(out)


__all__ = ['Molecule']
