from .abc import IsomorphismABC


class Isomorphism(IsomorphismABC):
    def get_mapping(self, other) -> Dict[int, int]:
        pass


__all__ = ['Isomorphism']