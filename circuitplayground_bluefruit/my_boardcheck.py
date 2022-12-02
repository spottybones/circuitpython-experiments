"""
my_boardcheck - provides a function to check the board_id against
a list of one or more supported boards passed in, exiting if the
current board_id isn't in that list.
"""
try:
    from typing import Union, List
except ImportError:
    pass

import sys
from board import board_id


def check_board(supported_boards: Union[List, str], board_id: str = board_id) -> None:
    """
    check_board - compare the current board_id with a list of
    valid boards and exit the program if no match is found.
    """
    if type(supported_boards) == str:
        supported_boards = [supported_boards]
    if board_id not in supported_boards:
        print(f'board "{board_id}" not supported')
        sys.exit()
