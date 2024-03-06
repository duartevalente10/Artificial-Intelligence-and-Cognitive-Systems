
'''Açoes possiveis'''

    # este   1  0
    # oeste -1  0
    # norte  0  1
    # sul    0 -1

from typing import Tuple

class Accao:
    def __init__(self, dx: int, dy: int):
        self._dx = dx
        self._dy = dy

    @property
    def dx(self) -> int:
        return self._dx

    @property
    def dy(self) -> int:
        return self._dy

    def __eq__(self, other: 'Accao') -> bool:
        return self._dx == other.dx and self._dy == other.dy

    def __hash__(self) -> int:
        return hash((self._dx, self._dy))
