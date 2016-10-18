#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring"""


import getpass
import authentication

def login(username, maxattempts=3):
    """fuction for name and password.

    Args:
        username(str): username in string to login.
        maxattempts(int, optional): maximum number of attempts in interger before
        turning false. defaults is 3.

    Returns:
        boolean: True or False in login.

    Examples:
        >>>import task_02
        >>>task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrent username or password. You have 2 attempts left.
    """

    authenticated = False
    attempts = 0
    question = 'Please enter your password:'
    errormsg = 'Incorrect username or password. You have {} attempts left.'

    while attempts < maxattempts:
        myval = getpass.getpass(question)
        if authentication.authenticate(username, myval):
            authenticated = True
            break
        else:
            attempts += 1
            errormsg.format(maxattempts - attempts)
    return authenticated
        
