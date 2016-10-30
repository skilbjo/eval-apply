#!/usr/bin/env python3
import sys
import math
import operator as op

Env = dict          # An environment is a mapping of {variable: value}

Symbol = str          # A Scheme Symbol is implemented as a Python str
List   = list         # A Scheme List is implemented as a Python list
Number = (int, float) # A Scheme Number is implemented as a Python int or float

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args):
        return eval(self.body, Env(self.parms, args, self.env))

class Env(dict):
    "An environment: a dict of {'var':val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        "Find the innermost Env where var appears."
        return self if (var in self) else self.outer.find(var)

def standard_env():
  "An environment with some Scheme standard procedures."
  "https://docs.python.org/3/library/operator.html"
  env = Env()
  env.update(vars(math)) # sin, cos, sqrt, pi, ...
  env.update({
    '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv,
    '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq,
    'abs':     abs,
    'append':  op.add,
    # 'apply':   apply,
    'begin':   lambda *x: x[-1],
    'car':     lambda x: x[0],
    'cdr':     lambda x: x[1:],
    'cons':    lambda x,y: [x] + y,
    'eq?':     op.is_,
    'equal?':  op.eq,
    'length':  len,
    'list':    lambda *x: list(x),
    'list?':   lambda x: isinstance(x,list),
    'map':     map,
    'max':     max,
    'min':     min,
    'not':     op.not_,
    'null?':   lambda x: x == [],
    'number?': lambda x: isinstance(x, Number),
    'procedure?': callable,
    'round':   round,
    'symbol?': lambda x: isinstance(x, Symbol),
  })
  return env

global_env = standard_env()

# def eval(x, env=global_env):
  # "Evaluate an expression in an environment."
  # if isinstance(x, Symbol):      # variable reference
    # return env[x]
  # elif not isinstance(x, List):  # constant literal
    # return x
  # elif x[0] == 'if':             # conditional
    # (_, test, conseq, alt) = x
    # exp = (conseq if eval(test, env) else alt)
    # return eval(exp, env)
  # elif x[0] == 'define':         # definition
    # (_, var, exp) = x
    # env[var] = eval(exp, env)
  # else:                          # procedure call
    # proc = eval(x[0], env)
    # args = [eval(arg, env) for arg in x[1:]]
    # return proc(*args)

def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):      # variable reference
        return env.find(x)[x]
    elif not isinstance(x, List):  # constant literal
        return x
    elif x[0] == 'quote':          # quotation
        (_, exp) = x
        return exp
    elif x[0] == 'if':             # conditional
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'define':         # definition
        (_, var, exp) = x
        env[var] = eval(exp, env)
    elif x[0] == 'set!':           # assignment
        (_, var, exp) = x
        env.find(var)[var] = eval(exp, env)
    elif x[0] == 'lambda':         # procedure
        (_, parms, body) = x
        return Procedure(parms, body, env)
    else:                          # procedure call
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)
