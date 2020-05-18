from itertools import tee
from .abc import ReactionABC, MoleculeListABC
from .molecule import Molecule


class MoleculeList(MoleculeListABC):
    def insert(self, i, molecule):
        if isinstance(molecule, Molecule):
            self._data.insert(i, molecule)
        else:
            raise TypeError('Only Molecule acceptable')

    def __getitem__(self, i):
        if isinstance(i, slice):
            ml = object.__new__(MoleculeList)
            ml._data = self._data[i]
            return ml
        return self._data[i]

    def __setitem__(self, i, molecule):
        if isinstance(i, slice):
            try:
                test, molecule = tee(molecule, 2)
                if all(isinstance(x, Molecule) for x in test):
                    self._data[i] = molecule
                else:
                    raise KeyError
            except TypeError:
                if isinstance(molecule, Molecule):
                    self._data[i] = molecule
        elif isinstance(molecule, Molecule):
            self._data[i] = molecule
        else:
            return TypeError


class Reaction(ReactionABC):
    def __init__(self):
        self._reactants = MoleculeList()
        self._products = MoleculeList()

    @property
    def reactants(self):
        return self._reactants

    @property
    def products(self):
        return self._products


__all__ = ['MoleculeList', 'Reaction']
