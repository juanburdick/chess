"""Main module."""
# pylint: disable=C0321
from typing import Dict, Callable

PIECES: Dict[str, type] = {}

class Chess:
    """State controller."""
    def __init__(self):
        pass

    def promotion(self, piece: 'Piece', selection: str) -> 'Piece':
        """Promote a piece to the selected type."""
        if selection in PIECES:
            return PIECES[selection]()
        raise NotImplementedError

    def move(self, piece: 'Piece', target):
        """Update the state."""
        pass

class Board:
    """Chessboard"""
    def __init__(self) -> None:
        pass

    def print_board(self) -> None:
        """Show the current boardstate."""
        pass

def register_pieces(piece_class: type) -> None:
    """Register a piece type."""
    name = piece_class.__name__.lower()
    PIECES[name] = piece_class

class Piece:
    """Parent class for pieces."""
