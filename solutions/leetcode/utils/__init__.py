import os, sys

def d(msg: str):
    if os.getenv('UVA_DEBUG'):
        print(msg, file=sys.stderr)

def check(anything):
    d(f'{anything}')
    return anything
