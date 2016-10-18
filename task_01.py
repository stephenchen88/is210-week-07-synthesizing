#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_01 docstring"""


def get_matches(players):
    """Fuction to get list of matchup for players.

    Args:
        players(list): list of player names.

    Returns:
        list: tuples of list unique matchup.

    Examples:
        >>>task_01.get_matches(['Harry', 'Howard', 'Hugh']}
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """

    matchlist = []
    for player1 in players:
        if players.index(player1) < myind:
            pair = player1, player2
            newlist.append(pair)
    return matchlist
