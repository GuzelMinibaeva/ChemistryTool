from .abc import MoleculeABC
from ..algorithms import Isomorphism, Components


class Molecule(Isomorphism, Components, MoleculeABC):
    __slots__ = ()


__all__ = ['Molecule']
