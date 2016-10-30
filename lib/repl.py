#!/usr/bin/env python3
import parse
import eval

Symbol = str          # A Scheme Symbol is implemented as a Python str
List   = list         # A Scheme List is implemented as a Python list
Number = (int, float) # A Scheme Number is implemented as a Python int or float

def repl(prompt='lis.py> '):
    "A prompt-read-eval-print loop."
    while True:
        val = eval.eval(parse.parse(input(prompt)))
        if val is not None:
            print(schemestr(val))

def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, List):
        return '(' + ' '.join(map(schemestr, exp)) + ')'
    else:
        return str(exp)

repl()
