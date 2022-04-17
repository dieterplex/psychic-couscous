import os
import sys
from typing import List, Optional
import numpy

from .tree import TreeNode, deserialize, draw
from .list import ListNode

__all__ = ['List', 'Optional'] + ['d', 'check'] + ['ListNode', 'TreeNode', 'deserialize', 'draw']


def d(msg: str):
    if os.getenv('UVA_DEBUG'):
        if isinstance(msg, List):
            msg = numpy.array(msg)
        print(msg, file=sys.stderr, flush=True)


def check(anything):
    d(f'{anything}')
    return anything
