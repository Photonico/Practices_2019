#### Python Study

import timeit

re = timeit.__doc__

print(re)

"""
Tool for measuring execution time of small code snippets.

This module avoids a number of common traps for measuring execution
times.  See also Tim Peters' introduction to the Algorithms chapter in
the Python Cookbook, published by O'Reilly.

Library usage: see the Timer class.

Command line usage:
    python timeit.py [-n N] [-r N] [-s S] [-p] [-h] [--] [statement]

Options:
    -n/--number N: how many times to execute 'statement' (default: see below)
    -r/--repeat N: how many times to repeat the timer (default 5)
    -s/--setup S: statement to be executed once initially (default 'pass').
                Execution time of this setup statement is NOT timed.
    -p/--process: use time.process_time() (default is time.perf_counter())
    -v/--verbose: print raw timing results; repeat for more digits precision
    -u/--unit: set the output time unit (nsec, usec, msec, or sec)
    -h/--help: print this usage message and exit
    --: separate options from statement, use when statement starts with -
    statement: statement to be timed (default 'pass')

A multi-line statement may be given by specifying each line as a
separate argument; indented lines are possible by enclosing an
argument in quotes and using leading spaces.  Multiple -s options are
treated similarly.

If -n is not given, a suitable number of loops is calculated by trying
successive powers of 10 until the total time is at least 0.2 seconds.

Note: there is a certain baseline overhead associated with executing a
pass statement.  It differs between versions.  The code here doesn't try
to hide it, but you should be aware of it.  The baseline overhead can be
measured by invoking the program without arguments.

Classes:

    Timer

Functions:

    timeit(string, string) -> float
    repeat(string, string) -> list
    default_timer() -> float
"""

re = dir(timeit)
print(re)
    # ['Timer', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_globals', 'default_number', 'default_repeat', 'default_timer', 'dummy_src_name', 'gc', 'itertools', 'main', 'reindent', 'repeat', 'sys', 'template', 'time', 'timeit']

re = timeit.__all__ # from timeit import *
print(re)
    # ['Timer', 'timeit', 'repeat', 'default_timer']

re = timeit.__file__
print(re)
    # C:\Python\Python37\lib\timeit.py

help(timeit)